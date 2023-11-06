import math
import os
import pygame, sys
from playerSprite import GunnerSprite
from sprites import SpriteSheet
from bullet import Bullet
from all_bullets import All_Bullets
from player import Gunman
from commands import InputHandler
from map_load import map_load, Tile

#Constants
WIDTH, HEIGHT = 1920, 1020
TITLE = "Mind Gungeon"

#pygame initialization
pygame.init()
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

inHandler = InputHandler()

bullets = All_Bullets()

pygame.mouse.set_visible(False)

#Player Initialization
player = Gunman(WIDTH/2, HEIGHT/2)

# bullet cooldown
cooldown = 500
now = 0

tiles,walls = map_load()

#Main Loop
while True:

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()

            # if not on cooldown
            last = pygame.time.get_ticks()
            if last - now >= cooldown:
                # shoot
                now = pygame.time.get_ticks()
                b = Bullet("orange", player.getX()+30, player.getY()+10, 20,20, 10, x,y)
                bullets.add(b)
    
    inHandler.handleInput(pygame.key.get_pressed(), player)
    inHandler.handleMouse(pygame.mouse.get_pos(), player)
    # Move Bullets    
    bullets.move(WIDTH, HEIGHT)

    #update
    player.update()

    for wall in walls:
        if wall.collides(player.rect):

            if player.velX < 0:
                player.set_rect_left(wall.getHitBox().right)
            if player.velX > 0:
                player.set_rect_right(wall.getHitBox().left)
            if player.velY < 0:
                player.set_rect_top(wall.getHitBox().bottom)
            if player.velY > 0:
                player.set_rect_bottom(wall.getHitBox().top)

    # Draw
    display.fill((12, 24, 36))
    #pygame.draw.rect(display, (60,60,60), (WIDTH/10, HEIGHT/10, WIDTH*4/5, HEIGHT*4/5))
    for tile in tiles:
        display.blit(tile.image, (tile.x, tile.y))

    # Draw Bullets
    bullets.draw(display)

    # Mouse
    x,y = pygame.mouse.get_pos()
    pygame.draw.circle(display, (255,0,0), (x, y), 15)
    pygame.draw.circle(display, (0,0,0), (x, y), 10)
    pygame.draw.circle(display, (255,0,0), (x, y), 5)

    player.draw(display)
    pygame.display.flip()

    clock.tick(60)