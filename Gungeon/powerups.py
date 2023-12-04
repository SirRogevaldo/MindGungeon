import pygame
import os

def check_player_powerups(player, chests):
    powerup = False

    Text_font = pygame.font.Font(os.path.join('Assets', 'Eight-Bit_Madness.ttf'), 80)
    Text = Text_font.render(str(""), False, (255,255,255))

    for chest in chests:
        if player.rect.colliderect(chest.getHitBox()):

            match chest.getType():
                case "1":
                    player.max_health += 1
                    player.health += 1
                    print("Health increased!")
                    Text = Text_font.render(str("Health increased by 1!"), False, (255,255,255))
                case "2":
                    player.reloadSpeed -= 100
                    print("Reload speed increased!")
                    Text = Text_font.render(str("Reload speed increased!"), False, (255,255,255))
                case "3":
                    player.speed += 1
                    print("Speed increased!")
                    Text = Text_font.render(str("Speed increased!"), False, (255,255,255))
                case "4":
                    player.player_gun = "crossbow"
                    print("Crossbow obtained!")
                    Text = Text_font.render(str("Crossbow obtained!"), False, (255,255,255))
                case "5":
                    player.player_gun = "missile"
                    print("Magic Missile obtained!")
                    Text = Text_font.render(str("Magic Missile obtained!"), False, (255,255,255))
                case "6":
                    player.player_gun = "cannon"
                    print("Cannon obtained!")
                    Text = Text_font.render(str("Cannon obtained!"), False, (255,255,255))
                case "7":
                    player.wipe_uses += 2
                    print("Extra 2 blanks obtained!")
                    Text = Text_font.render(str("Extra 2 blanks obtained!"), False, (255,255,255))
                case "8":
                    print("Surprise! Nothing happened!")
                    Text = Text_font.render(str("Surprise! Nothing happened!"), False, (255,255,255))
                case "9":
                    print("Surprise! Nothing happened!")
                    Text = Text_font.render(str("Surprise! Nothing happened!"), False, (255,255,255))
                case "0":
                    player.player_gun = "golden"
                    print("Golden Gun obtained!")
                    Text = Text_font.render(str("Golden Gun obtained!"), False, (255,255,255))

            powerup = True
            break
    
    return powerup, Text