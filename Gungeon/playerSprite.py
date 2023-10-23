import pygame, os
from sprites import SpriteSheet

class GunnerSprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        sprite_sheet_image = pygame.image.load(os.path.join('Assets', 'TheHunter.png')).convert_alpha()
        self.sprite_sheet = SpriteSheet(sprite_sheet_image)
        self.currLength = 0
        self.currentAnimation = []

        # pygame.transform.flip(Surface, xbool, ybool) 

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
        self.frame_image.append(self.sprite_sheet.get_image(22, 162, 16, 28, 3, (236, 216, 192)))
        self.frame_image.append(self.sprite_sheet.get_image(38, 162, 16, 28, 3, (236, 216, 192)))
        self.frame_image.append(self.sprite_sheet.get_image(54, 162, 16, 28, 3, (236, 216, 192)))
        self.frame_image.append(self.sprite_sheet.get_image(70, 162, 16, 28, 3, (236, 216, 192)))
        self.frame_image.append(self.sprite_sheet.get_image(86, 162, 16, 28, 3, (236, 216, 192)))
        self.frame_image.append(self.sprite_sheet.get_image(102,162, 16, 28, 3, (236, 216, 192)))
        # UP 18-24
        self.frame_image.append(self.sprite_sheet.get_image(22, 221, 16, 28, 3, (236, 216, 192)))
        self.frame_image.append(self.sprite_sheet.get_image(38, 221, 16, 28, 3, (236, 216, 192)))
        self.frame_image.append(self.sprite_sheet.get_image(54, 221, 16, 28, 3, (236, 216, 192)))
        self.frame_image.append(self.sprite_sheet.get_image(70, 221, 16, 28, 3, (236, 216, 192)))
        self.frame_image.append(self.sprite_sheet.get_image(86, 221, 16, 28, 3, (236, 216, 192)))
        self.frame_image.append(self.sprite_sheet.get_image(102,221, 16, 28, 3, (236, 216, 192)))
        # IDLE 24-28
        self.frame_image.append(self.sprite_sheet.get_image(22, 39, 16, 28, 3, (236, 216, 192)))
        self.frame_image.append(self.sprite_sheet.get_image(38, 39, 16, 28, 3, (236, 216, 192)))
        self.frame_image.append(self.sprite_sheet.get_image(54, 39, 16, 28, 3, (236, 216, 192)))
        self.frame_image.append(self.sprite_sheet.get_image(70, 39, 16, 28, 3, (236, 216, 192)))

        self.currentAnimation = self.frame_image[24:28]
        self.currLength = 4

    def updateType(self,type):
        if type == "RIGHT":
            self.currentAnimation = self.frame_image[0:6]
            self.currLength = 6
        elif type == "LEFT":
            self.currentAnimation = self.frame_image[6:12]
            self.currLength = 6
        elif type == "DOWN":
            self.currentAnimation = self.frame_image[12:18]
            self.currLength = 6
        elif type == "UP":
            self.currentAnimation = self.frame_image[18:24]
            self.currLength = 6
        else:
            self.currentAnimation = self.frame_image[24:28]
            self.currLength = 4
    
    def getCurrentAnimation(self):
        return self.currentAnimation
    
    def getCurrentLength(self):
        return self.currLength
