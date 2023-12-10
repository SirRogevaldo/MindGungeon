import pygame, sys, os
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
from powerups import *
from cursor import *

"""
    Main file for the game
    Contains the main game loop and the main game logic
"""
#Constants
WIDTH, HEIGHT = 1800, 900
TITLE = "Mind Gungeon"

#pygame initialization
pygame.init()
pygame.font.get_init()

display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)

def Title_Screen(screen):
    intro = True

    Text_font = pygame.font.Font(os.path.join('Assets', 'Eight-Bit_Madness.ttf'), 70)
    Title_font = pygame.font.Font(os.path.join('Assets', 'Eight-Bit_Madness.ttf'), 200)

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    intro = False
        display.fill((0,0,0))

        match screen:
            case "main":
                
                title_image = pygame.image.load(os.path.join('Assets', 'Title.jpg')).convert_alpha()
                display.blit(title_image, (0,0))

                title_text = Title_font.render("MIND GUNGEON", False, (255, 204, 255))
                display.blit(title_text, (WIDTH/4, HEIGHT/5))

                start_text = Text_font.render("PRESS SPACE TO START", False, (255,255,255))
                display.blit(start_text, (WIDTH/3, HEIGHT/2))
            case "win":

                victory_image = pygame.image.load(os.path.join('Assets', 'Victory.jpg')).convert_alpha()
                victory_image = pygame.transform.scale(victory_image, (WIDTH, HEIGHT))
                display.blit(victory_image, (0,0))

                player_idle = pygame.image.load(os.path.join('Assets', 'PlayerIdle.png')).convert_alpha()
                player_idle = pygame.transform.scale(player_idle, (16 * 13, 28 * 10))
                player_idle.set_colorkey((236, 216, 192))
                
                display.blit(player_idle, (WIDTH/2-100, HEIGHT/2-50))

                #start_text = Text_font.render("YOU WIN", False, (255,255,255))
                #display.blit(start_text, (WIDTH/3, HEIGHT/2))
            case "lose":

                defeat_image = pygame.image.load(os.path.join('Assets', 'Lose.jpeg')).convert_alpha()
                defeat_image = pygame.transform.scale(defeat_image, (WIDTH, HEIGHT))
                display.blit(defeat_image, (0,0))

                start_text = Text_font.render("THE GUN IS STILL WAITING TO BE FOUND, PRESS SPACE TO RESTART", False, (255,255,255))
                display.blit(start_text, (0, HEIGHT - HEIGHT/10))
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
    player.register("hit", player.got_shot)

    # InputHandler (Controls)
    inHandler = InputHandler()

    #stats ui
    stats_ui = Stats_ui()

    lNames = map_names()

    for level in lNames:

        print(str(level))

        bullets.wipe(entity=None)

        powerup = False

        tiles,walls,spawnPoints,chests,fountain = map_load(str(level))

        #DEFINE SPAWN POINT
        player.setX(WIDTH/10)
        player.setY(HEIGHT/2)

        #Enemies and spawner
        shotgun = Shotgun(0,0)
        mage    = Mage(0,0)
        sniper  = Sniper(0,0)
        target  = Target(0,0)
        shade   = Shade(0,0)
        smiley  = Smiley(0,0)
        spawner = Spawner()
        enemies = All_Enemies()

        # spawn enemies
        for t, cell in spawnPoints:
            if(cell == 's'):
                enemies.add(spawner.spawnMonster(shotgun,t.getX(),t.getY()))
            elif(cell == 'S'):
                enemies.add(spawner.spawnMonster(sniper,t.getX(),t.getY()))
            elif(cell == 'm'):
                enemies.add(spawner.spawnMonster(mage,t.getX(),t.getY()))
            elif(cell == 'T'):
                enemies.add(spawner.spawnMonster(target,t.getX(),t.getY()))
            elif(cell == 'Y'):
                enemies.add(spawner.spawnMonster(shade,t.getX(),t.getY()))
            elif(cell == 'y'):
                enemies.add(spawner.spawnMonster(smiley,t.getX(),t.getY()))
            else:
                enemies.add(spawner.spawnMonster(shotgun,t.getX(),t.getY()))

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
                        bullets.add([Bullet(player.getX(), player.getY()+35,x,y,player.getGun())])
                        audio_manager.Player_shot_play(entity=None)
            
            #CHECK IF ALL ENEMIES ARE DEAD
            if (len(enemies.get_enemies()) == 0):
                break
            
            #ENEMY ATTACKING
            bullets.add(enemies.attack(player))
            
            #MOVING
            for command in inHandler.handleInput(pygame.key.get_pressed()):
                command.pressed(player)
                collision_detector.collision_entity_walls(player,walls)
                
            # Check chest collision
            if chests != []:
                powerup,powerup_text = check_player_powerups(player, chests)
                if powerup:
                    tiles = [x for x in tiles if x not in chests]
                    chests = []
            if fountain != None:
                if player.rect.colliderect(fountain.getHitBox()):
                    player.health = min(player.health + player.max_health / 3, player.max_health)
                    tiles = [x for x in tiles if x != fountain]
                    fountain = None

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
            drawCursor(player.getGun(), display)

            # DEBUG HITBOXES
            #pygame.draw.rect(display, (255,0,0), player.rect,2)
            #for enemy in enemies.get_enemies():
            #    pygame.draw.rect(display, (255,0,0), enemy.get_rect(),2)

            player.draw(display)

            # Draw Bullets
            bullets.draw(display)

            stats_ui.draw(display,player,level)
            # Display powerup text
            if powerup:
                display.blit(powerup_text, (WIDTH/3, 700))

            pygame.display.flip()

            clock.tick(60)

    return True

if __name__ == "__main__":
    Title_Screen("main")
    over = False

    while(not over):
        win = game()
        if win:
            Title_Screen("win")
            over = True
        else:
            Title_Screen("lose")
    
    pygame.quit()
    sys.exit()