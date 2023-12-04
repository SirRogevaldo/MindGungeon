import pygame, sys
from bullet import Bullet
from all_bullets import All_Bullets
from all_enemies import All_Enemies
from player import Gunman
from commands import InputHandler
from map_load import map_load, map_names
import collision_detector
from enemies import *
import audio_manager
from stats_ui import Stats_ui

import os

#Constants
WIDTH, HEIGHT = 1800, 900
TITLE = "Mind Gungeon"

#pygame initialization
pygame.init()
pygame.font.get_init()

display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()


def main_menu():
    intro = True

    Text_font = pygame.font.Font(os.path.join('Assets', 'Eight-Bit_Madness.ttf'), 80)

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    intro = False
        display.fill((0,0,0))
        start_text = Text_font.render("PRESS SPACE TO START", False, (255,255,255))
        display.blit(start_text, (WIDTH/3, HEIGHT/2))
        pygame.display.flip()
        clock.tick(60)


def game_over():
    end = True

    Text_font = pygame.font.Font(os.path.join('Assets', 'Eight-Bit_Madness.ttf'), 80)

    while end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    end = False
        display.fill((0,0,0))
        start_text = Text_font.render("YOU DIED", False, (255,255,255))
        display.blit(start_text, (WIDTH/3, HEIGHT/2))
        pygame.display.flip()
        clock.tick(60)

def game_win():
    win = True

    Text_font = pygame.font.Font(os.path.join('Assets', 'Eight-Bit_Madness.ttf'), 80)

    while win:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    win = False
        display.fill((0,0,0))
        start_text = Text_font.render("YOU WIN", False, (255,255,255))
        display.blit(start_text, (WIDTH/3, HEIGHT/2))
        pygame.display.flip()
        clock.tick(60)



def game():

    #audio
    audio_manager.music_play()

    bullets = All_Bullets()

    #Player Initialization
    player = Gunman(WIDTH/10, HEIGHT/2)
    #player event registers 
    player.register("wipe",bullets.wipe)
    player.register("wipe",audio_manager.Player_wipe_play)

    # InputHandler (Controls)
    inHandler = InputHandler()

    #stats ui
    stats_ui = Stats_ui()

    lNames = map_names()

    for level in lNames:

        print(str(level))

        bullets.wipe(entity=None)

        pygame.mouse.set_visible(False)

        tiles,walls,spawnPoints = map_load(str(level))

        #! DEFINE SPAWN POINT
        player.setX(WIDTH/10)
        player.setY(HEIGHT/2)

        #Enemies and spawner
        shotgun = Shotgun(0,0)
        mage = Mage(0,0)
        sniper = Sniper(0,0)
        target = Target(0,0)
        spawner = Spawner()
        enemies = All_Enemies()

        # spawn enemies
        test=0
        for t, cell in spawnPoints:
            if(cell == 's'):
                enemies.add(spawner.spawnMonster(shotgun,t.getX(),t.getY()))
            elif(cell == 'S'):
                enemies.add(spawner.spawnMonster(sniper,t.getX(),t.getY()))
            elif(cell == 'm'):
                enemies.add(spawner.spawnMonster(mage,t.getX(),t.getY()))
            elif(cell == 'T'):
                enemies.add(spawner.spawnMonster(target,t.getX(),t.getY()))
            else:
                enemies.add(spawner.spawnMonster(shotgun,t.getX(),t.getY()))
            test += 1

        #Main Loop
        while True:

            # EVENTS
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    
                    if player.fire():
                        # shoot
                        x,y = pygame.mouse.get_pos()
                        bullets.add(Bullet(player.getX(), player.getY()+35,x,y,"normal"))
            
            #CHECK IF ALL ENEMIES ARE DEAD
            if (len(enemies.get_enemies()) == 0):
                break
            
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
            #end of game loop
            if player.health <= 0:
                print("You died")
                return False

            enemies.update()
            
            # Draw
            display.fill((12, 24, 36))
            for tile in tiles:
                display.blit(tile.image, (tile.x, tile.y))

            enemies.draw(display)

            # Mouse
            x,y = pygame.mouse.get_pos()
            pygame.draw.circle(display, (255,0,0), (x, y), 15)
            pygame.draw.circle(display, (0,  0,0), (x, y), 10)
            pygame.draw.circle(display, (255,0,0), (x, y),  5)

            pygame.draw.rect(display, (255,0,0), player.rect,2)

            for enemy in enemies.get_enemies():
                pygame.draw.rect(display, (255,0,0), enemy.get_rect(),2)

            player.draw(display)

            # Draw Bullets
            bullets.draw(display)

            stats_ui.draw(display,player,level)

            pygame.display.flip()

            clock.tick(60)

    return True

if __name__ == "__main__":
    main_menu()
    win = game()
    if win:
        game_win()
    else:
        game_over()
    
    pygame.quit()
    sys.exit()