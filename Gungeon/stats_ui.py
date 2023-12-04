from sprites import SpriteSheet
import pygame
import os

class Stats_ui():

    def __init__(self):
        sprite_sheet_image = pygame.image.load(os.path.join('Assets', 'stats.png')).convert_alpha()
        self.sprite_sheet = SpriteSheet(sprite_sheet_image)

        pygame.font.get_init()
        self.Text_font = pygame.font.Font(os.path.join('Assets', 'Eight-Bit_Madness.ttf'), 80)

        scale = 1

        self.full_heart = self.sprite_sheet.get_image(16, 20, 51, 44, scale, (0, 0, 0))
        self.empty_heart = self.sprite_sheet.get_image(80, 20, 51, 44, scale, (0, 0, 0))

        self.bullet_wipe = self.sprite_sheet.get_image(15, 75, 41, 40, scale, (0, 0, 0))

        self.bullet = self.sprite_sheet.get_image(135, 131, 40, 40, scale, (0, 0, 0))

    def draw(self, display, player,level):

        for i in range(player.max_health):
            if i < player.health:
                display.blit(self.full_heart, (i * 57, 0))
            else:
                display.blit(self.empty_heart, (i * 57, 0))
        
        for i in range(player.wipe_uses):
            display.blit(self.bullet_wipe, (i*50, 50))
        
        display.blit(self.bullet, (0, 100))
        bullet_text = self.Text_font.render(str(player.chamber), False, (255,255,255))
        display.blit(bullet_text, (50, 100))

        #level_text = self.Text_font.render("Level:", False, (255,255,255))
        level_name = self.Text_font.render(str(level), False, (255,255,255))
        #display.blit(level_text, (0, 150))
        display.blit(level_name, (0, 150))
        


