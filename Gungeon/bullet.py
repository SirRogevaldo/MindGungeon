import math
import pygame

bullet_types = {
    'normal': {
        'color' : "orange",
        'width' : 10,
        'height': 10,
        'speed' : 10,
        'damage': 1,
        'friendly' : True
    },
    'crossbow': {
        'color' : "brown",
        'width' : 10,
        'height': 10,
        'speed' : 10,
        'damage': 2,
        'friendly' : True
    },
    'missile': {
        'color' : "red",
        'width' : 5,
        'height': 5,
        'speed' : 15,
        'damage': 1,
        'friendly' : True
    },
    'cannon': {
        'color' : "dark grey",
        'width' : 25,
        'height': 25,
        'speed' : 10,
        'damage': 1,
        'friendly' : True
    },
    'golden': {
        'color' : "yellow",
        'width' : 30,
        'height': 30,
        'speed' : 5,
        'damage': 3,
        'friendly' : True
    },
    'shotgun': {
        'color' : "blue",
        'width' : 10,
        'height': 10,
        'speed' : 3,
        'damage': 1,
        'friendly' : False
    },
    'magic': {
        'color' : "light blue",
        'width' : 5,
        'height': 5,
        'speed' : 15,
        'damage': 1,
        'friendly' : False
    },
    'sniper': {
        'color' : "light gray",
        'width' : 25,
        'height': 25,
        'speed' : 12,
        'damage': 2,
        'friendly' : False
    },
    'boss': {
        'color' : "red",
        'width' : 45,
        'height': 45,
        'speed' : 3,
        'damage': 2,
        'friendly' : False
    },
    'none': { # might want to troll my making target shoot
        'color' : "gray",
        'width' : 5,
        'height': 5,
        'speed' : 1,
        'damage': 1,
        'friendly' : False
    }
}

class Bullet:
    def __init__(self, x, y, targetx, targety, type):
        self.type = type
        self.rect = pygame.Rect(x,y,bullet_types[type].get('width'),bullet_types[type].get('height'))
        self.color = bullet_types[type].get('color')
        self.speed = bullet_types[type].get('speed')
        angle = math.atan2(targety-y, targetx-x) #get angle to target in radians
        #print('Angle in degrees:', int(angle*180/math.pi))
        self.dx = math.cos(angle)*self.speed
        self.dy = math.sin(angle)*self.speed
        self.x = x
        self.y = y

        #
        self.friendly = bullet_types[type].get('friendly')
        self.damage = bullet_types[type].get('damage')

    def is_friendly(self):
        return self.friendly

    def get_rect(self):
        return self.rect

    def draw(self, surface):
        pygame.draw.circle(surface, "black", (self.x, self.y), bullet_types[self.type].get('width') + 2)
        pygame.draw.circle(surface, self.color, (self.x, self.y), bullet_types[self.type].get('width'))
    
    def get_damage(self):
        return self.damage
        
    #Override
    def move(self):
        #self.x and self.y are floats (decimals) so I get more accuracy
        #if I change self.x and y and then convert to an integer for
        #the rectangle.
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)