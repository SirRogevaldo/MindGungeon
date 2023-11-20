import pygame
from FSM import FSM
from actor import Actor
from playerSprite import GunnerSprite
from subject import Subject
import math


#Gunman Class
class Gunman(Actor,Subject):
    def __init__(self, x, y):
        Subject.__init__(self)

        self.register("hit", self.got_shot)

        self.rect = pygame.Rect(int(x), int(y), 50, 70)
        self.last_x = int(x)
        self.last_y = int(y)
        self.velX = 0
        self.velY = 0
        self.color = (92, 64, 51)

        self.health = 6
        self.speed = 4

        # Player sprite
        self.player_sprite = GunnerSprite()
        #self.player_fsm = FSM() invinc frames

    def move(self, dx, dy):

        self.velX = 0
        self.velY = 0

        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.last_x = self.rect.x
            self.velX = dx
            # Move the rect
            self.rect.x += dx * self.speed
        elif dy != 0:
            self.last_y = self.rect.y
            self.velY = dy
            # Move the rect
            self.rect.y += dy * self.speed

    def update(self):

        xx,yy = pygame.mouse.get_pos()

        angle = math.atan2(self.rect.x - xx, self.rect.y - yy)

        walk = (self.velX != 0 or self.velY != 0)

        self.player_sprite.update(angle,walk)
    
    def got_shot(self, entity):
        print("Oof")
        self.health -= entity.get_damage()
        if self.health <= 0:
            print("You died")
            pygame.quit()
        
    
    def draw(self, display):
        self.player_sprite.draw(display,self.rect.x, self.rect.y)

    # getters and setters
    def getX(self):
        return self.rect.x
    
    def getY(self):
        return self.rect.y
    
    def get_rect(self):
        return self.rect
    
    def getVelX(self):
        return self.velX
    
    def getVelY(self):
        return self.velY

    #-------------------

    def setX(self, x):
        self.rect.x = x
    
    def setY(self, y):
        self.rect.y = y

    def setVelX(self, x):
        self.rect.x = x
    
    def setVelY(self, y):
        self.rect.y = y
    
    def set_rect(self, rect):
        self.rect = rect
    
    def set_rect_left(self, left):
        self.rect.left = left
    
    def set_rect_right(self, right):
        self.rect.right = right
    
    def set_rect_top(self, top):
        self.rect.top = top
    
    def set_rect_bottom(self, bottom):
        self.rect.bottom = bottom
    
    