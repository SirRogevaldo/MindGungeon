import math
import os
import pygame, sys
from playerSprite import GunnerSprite
from sprites import SpriteSheet
from bullet import Bullet
from all_bullets import All_Bullets
from player import Gunman
from commands import InputHandler

#Constants
WIDTH, HEIGHT = 1920, 1000
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

playerSp = GunnerSprite()

clock = pygame.time.Clock()

# bullet cooldown
cooldown = 500
now = 0

# animation
frame = 0
frame_counter = 0


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
                b = Bullet("orange", player.x+30, player.y+10, 20,20, 10, x,y)
                bullets.add(b)
    
    inHandler.handleInput(pygame.key.get_pressed(), player)

    # Move Bullets    
    bullets.move(WIDTH, HEIGHT)


    # Draw
    display.fill((12, 24, 36))
    pygame.draw.rect(display, (60,60,60), (WIDTH/10, HEIGHT/10, WIDTH*4/5, HEIGHT*4/5))  

    x,y = pygame.mouse.get_pos()
    angle = math.atan2(player.getX()-x, player.getY()-y)

    if angle < -2.7 or angle > 2.7:
        playerSp.updateType("DOWN")
    elif angle > -0.7 and angle < 0.7:
        playerSp.updateType("UP")
    elif  angle > -2.7 and angle < -0.7:
        playerSp.updateType("RIGHT")
    elif angle < 2.7 and angle > 0.7:
        playerSp.updateType("LEFT")
    else:
        playerSp.updateType("IDLE")


    # Draw Bullets
    bullets.draw(display)

    # Mouse
    x,y = pygame.mouse.get_pos()
    pygame.draw.circle(display, (255,0,0), (x, y), 15)
    pygame.draw.circle(display, (0,0,0), (x, y), 10)
    pygame.draw.circle(display, (255,0,0), (x, y), 5)

    # Change Sprite
    frame_last = pygame.time.get_ticks()
    if frame_last - frame_counter >= 100: 
        frame += 1

        frame_counter = pygame.time.get_ticks()
    if frame == playerSp.getCurrentLength():
        frame = 0

    display.blit(playerSp.getCurrentAnimation()[frame], (player.x, player.y))

    #update
    player.update()
    pygame.display.flip()

    clock.tick(60)