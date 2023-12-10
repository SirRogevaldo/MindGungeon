import pygame, os
from sprites import SpriteSheet

"""

    Enemy Sprites:

    - This file contains the class responsible for drawing the enemy sprites, inherits the SpriteSheet class from sprites.py

"""

class EnemySprite(pygame.sprite.Sprite):
    def __init__(self, enemy):
        super().__init__()

        if enemy == "Shade":
            sprite_sheet_image = pygame.image.load(os.path.join('Assets', 'Shade_Boss.png')).convert_alpha()
        elif enemy == "Smiley":
            sprite_sheet_image = pygame.image.load(os.path.join('Assets', 'Smiley_Boss.png')).convert_alpha()
        else:
            sprite_sheet_image = pygame.image.load(os.path.join('Assets', 'BulletKin.png')).convert_alpha()

        self.sprite_sheet = SpriteSheet(sprite_sheet_image)

        # animation
        self.frame = 0
        self.frame_counter = 0

        self.frame_image = []

        if enemy == "Shade":
            # RIGHT 0-6
            self.frame_image.append(self.sprite_sheet.get_image(5,  381, 23, 39, 3, (0, 152, 239)))
            self.frame_image.append(self.sprite_sheet.get_image(33, 381, 27, 39, 3, (0, 152, 239)))
            self.frame_image.append(self.sprite_sheet.get_image(65, 381, 27, 39, 3, (0, 152, 239)))
            self.frame_image.append(self.sprite_sheet.get_image(97, 381, 24, 39, 3, (0, 152, 239)))
            self.frame_image.append(self.sprite_sheet.get_image(126, 381, 25, 39, 3, (0, 152, 239)))
            self.frame_image.append(self.sprite_sheet.get_image(158, 381, 27, 39, 3, (0, 152, 239)))
        elif enemy == "Smiley":
            self.frame_image.append(self.sprite_sheet.get_image(5,  373, 23, 39, 3, (0, 152, 239)))
            self.frame_image.append(self.sprite_sheet.get_image(31, 373, 27, 39, 3, (0, 152, 239)))
            self.frame_image.append(self.sprite_sheet.get_image(63, 373, 27, 39, 3, (0, 152, 239)))
            self.frame_image.append(self.sprite_sheet.get_image(94, 373, 24, 39, 3, (0, 152, 239)))
            self.frame_image.append(self.sprite_sheet.get_image(120, 373, 25, 39, 3, (0, 152, 239)))
            self.frame_image.append(self.sprite_sheet.get_image(152, 373, 27, 39, 3, (0, 152, 239)))
        else:
            self.frame_image.append(self.sprite_sheet.get_image(6,  53, 11, 22, 3, (0, 152, 239)))
            self.frame_image.append(self.sprite_sheet.get_image(21, 53, 14, 22, 3, (0, 152, 239)))
            self.frame_image.append(self.sprite_sheet.get_image(39, 54, 14, 21, 3, (0, 152, 239)))
            self.frame_image.append(self.sprite_sheet.get_image(57, 53, 11, 22, 3, (0, 152, 239)))
            self.frame_image.append(self.sprite_sheet.get_image(72, 52, 15, 23, 3, (0, 152, 239)))
            self.frame_image.append(self.sprite_sheet.get_image(90, 54, 16, 21, 3, (0, 152, 239)))

    def update(self):

        # Change Sprite
        frame_last = pygame.time.get_ticks()
        if frame_last - self.frame_counter >= 100: 
            self.frame += 1

            self.frame_counter = pygame.time.get_ticks()
        if self.frame == len(self.frame_image):
            self.frame = 0

    def draw(self, display, hitBox):
        display.blit(self.frame_image[self.frame%len(self.frame_image)], (hitBox.x, hitBox.y))