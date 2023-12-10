import pygame, os
from sprites import SpriteSheet

"""
    Player Sprites:

    - This file contains the class responsible for drawing the player sprite, inherits the SpriteSheet class from sprites.py

"""

animation_dict = {
    "RIGHT": (0,6),
    "LEFT": (6,12),
    "DOWN": (12,18),
    "UP":  (18,24),
    "IDLE": (24,28)
}

class GunnerSprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        sprite_sheet_image = pygame.image.load(os.path.join('Assets', 'TheHunter.png')).convert_alpha()
        self.sprite_sheet = SpriteSheet(sprite_sheet_image)
        self.currentAnimation = []

        # animation
        self.frame = 0
        self.frame_counter = 0

        self.frame_image = []
        # RIGHT 0-6
        self.frame_image.append(self.sprite_sheet.get_image(20, 191, 16, 28, 3, (236, 216, 192)))
        self.frame_image.append(self.sprite_sheet.get_image(38, 191, 16, 28, 3, (236, 216, 192)))
        self.frame_image.append(self.sprite_sheet.get_image(54, 191, 16, 28, 3, (236, 216, 192)))
        self.frame_image.append(self.sprite_sheet.get_image(70, 191, 16, 28, 3, (236, 216, 192)))
        self.frame_image.append(self.sprite_sheet.get_image(86, 191, 16, 28, 3, (236, 216, 192)))
        self.frame_image.append(self.sprite_sheet.get_image(102,191, 16, 28, 3, (236, 216, 192)))
        # LEFT 6-12
        for i in range(6):
            a = pygame.transform.flip(self.frame_image[i], True, False)
            a.set_colorkey((236, 216, 192))
            self.frame_image.append(a)
        # Down 12-18
        for i in range(6):
            self.frame_image.append(self.sprite_sheet.get_image(22+ i*16, 162, 16, 28, 3, (236, 216, 192)))
        # UP 18-24
        for i in range(6):
            self.frame_image.append(self.sprite_sheet.get_image(22+ i*16, 221, 16, 28, 3, (236, 216, 192)))
        # IDLE 24-28
        for i in range(4):
            self.frame_image.append(self.sprite_sheet.get_image(20 + i*16, 39, 16, 28, 3, (236, 216, 192)))

        self.currentAnimation = self.frame_image[24:28]

    def updateType(self,type):

        if animation_dict.get(type) != None:
            self.currentAnimation = self.frame_image[animation_dict.get(type)[0]:animation_dict.get(type)[1]]
        # If incorrect type, set to idle
        else:
            self.currentAnimation = self.frame_image[24:28]

    def update(self,angle,walk):

        if not walk:
            self.updateType("IDLE")
        elif angle < -2.7 or angle > 2.7:
            self.updateType("DOWN")
        elif angle > -0.7 and angle < 0.7:
            self.updateType("UP")
        elif  angle > -2.7 and angle < -0.7:
            self.updateType("RIGHT")
        elif angle < 2.7 and angle > 0.7:
            self.updateType("LEFT")

        # Change Sprite
        frame_last = pygame.time.get_ticks()
        if frame_last - self.frame_counter >= 100: 
            self.frame += 1

            self.frame_counter = pygame.time.get_ticks()
        if self.frame == self.getCurrentLength():
            self.frame = 0

    def draw(self, display, x, y):
        display.blit(self.currentAnimation[self.frame%self.getCurrentLength()], (x, y))

    def getCurrentAnimation(self):
        return self.currentAnimation
    
    def getCurrentLength(self):
        return len(self.currentAnimation)
