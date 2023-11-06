import pygame

class SpriteSheet():
    def __init__(self, image):
        self.sheet = image

    def get_image(self, x, y, width, height, scale, colour):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), (x, y, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(colour)
        return image
    
    def get_image_wsize(self, x, y, width, height, wx, wy, colour):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), (x, y, width, height))
        image = pygame.transform.scale(image, (wx, wy))
        image.set_colorkey(colour)
        return image
