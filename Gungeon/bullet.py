import math
import pygame

class Bullet:
    def __init__(self, color, x, y, width, height, speed, targetx,targety):
        self.rect = pygame.Rect(x,y,width,height)
        self.color = color
        self.speed = speed
        angle = math.atan2(targety-y, targetx-x) #get angle to target in radians
        #print('Angle in degrees:', int(angle*180/math.pi))
        self.dx = math.cos(angle)*speed
        self.dy = math.sin(angle)*speed
        self.x = x
        self.y = y

        #
        self.friendly = True

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        
    #Override
    def move(self):
        #self.x and self.y are floats (decimals) so I get more accuracy
        #if I change self.x and y and then convert to an integer for
        #the rectangle.
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)