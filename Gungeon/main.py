import math
import os
import pygame, sys
from playerSprite import GunnerSprite
from sprites import SpriteSheet
from bullet import Bullet
from all_bullets import All_Bullets
from all_enemies import All_Enemies
from player import Gunman
from commands import InputHandler
from map_load import map_load, Tile
import collision_detector
from enemies import *
import audio_manager

#Constants
WIDTH, HEIGHT = 1920, 1020
TITLE = "Mind Gungeon"

#pygame initialization
pygame.init()
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

# InputHandler (Controls)
inHandler = InputHandler()

bullets = All_Bullets()

pygame.mouse.set_visible(False)

#Player Initialization
player = Gunman(WIDTH/10, HEIGHT/2)

# bullet cooldown
cooldown = 500
now = 0

tiles,walls,spawnPoints = map_load()

#Enemies and spawner
shotgun = Shotgun(0,0)
mage = Mage(0,0)
sniper = Sniper(0,0)
spawner = Spawner()
enemies = All_Enemies()


#audio
audio_manager.music_play()


player.register("wipe",bullets.wipe)
player.register("wipe",audio_manager.Player_wipe_play)

#Main Loop
while True:

    # EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            # if not on cooldown
            last = pygame.time.get_ticks()
            if last - now >= cooldown:
                # shoot
                x,y = pygame.mouse.get_pos()
                now = pygame.time.get_ticks()
                b = Bullet(player.getX()+30, player.getY()+10,x,y,"normal")
                bullets.add(b)
            
    # SPAWNING    
    if (len(enemies.get_enemies()) == 0):
        for i in spawnPoints:
            enemies.add(spawner.spawnMonster(shotgun,i.getX(),i.getY()))
    
    #ENEMY ATTACKING
    for enemy in enemies.get_enemies():
        if enemy.fire():
            bullets.add(Bullet(enemy.hitBox.x, enemy.hitBox.y, player.getX(), player.getY(), enemy.getBulletType()))

    #MOVING
    for command in inHandler.handleInput(pygame.key.get_pressed()):
        command.pressed(player)
        collision_detector.collision_entity_walls(player,walls)

    # Move Enemies
    enemies.move(walls,player)

    # Move Bullets    
    bullets.move(walls,enemies.get_enemies(),player)


    #update
    player.update()
    enemies.update()
    
    # Draw
    display.fill((12, 24, 36))
    for tile in tiles:
        display.blit(tile.image, (tile.x, tile.y))

    enemies.draw(display)

    # Draw Bullets
    bullets.draw(display)

    # Mouse
    x,y = pygame.mouse.get_pos()
    pygame.draw.circle(display, (255,0,0), (x, y), 15)
    pygame.draw.circle(display, (0,  0,0), (x, y), 10)
    pygame.draw.circle(display, (255,0,0), (x, y), 5)

    pygame.draw.rect(display, (255,0,0), player.rect,2)

    for enemy in enemies.get_enemies():
        pygame.draw.rect(display, (255,0,0), enemy.get_rect(),2)

    player.draw(display)
    pygame.display.flip()

    clock.tick(60)