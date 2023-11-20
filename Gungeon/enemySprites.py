import pygame, os
from sprites import SpriteSheet

animation_dict = {
    "RIGHT": (0,6),
    "LEFT": (6,12),
    "DOWN": (12,18),
    "UP":  (18,24),
    "IDLE": (24,28)
}

class EnemySprite(pygame.sprite.Sprite):
    def __init__(self, enemy):
        super().__init__()

        if enemy == "Shotgun":
            sprite_sheet_image = pygame.image.load(os.path.join('Assets', 'BulletKin.png')).convert_alpha()
        else:
            sprite_sheet_image = pygame.image.load(os.path.join('Assets', 'BulletKin.png')).convert_alpha()

        self.sprite_sheet = SpriteSheet(sprite_sheet_image)

        # animation
        self.frame = 0
        self.frame_counter = 0

        self.frame_image = []
        # RIGHT 0-6
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