import pygame
from FSM import FSM
from actor import Actor
from playerSprite import GunnerSprite
import math


#Gunman Class
class Gunman(Actor):
    def __init__(self, x, y):
        self.rect = pygame.Rect(int(x), int(y), 48, 70)
        self.last_x = int(x)
        self.last_y = int(y)
        self.color = (92, 64, 51)
        self.velX = 0
        self.velY = 0
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.mouse_pos = (0,0)

        self.speed = 4

        # Player sprite
        self.player_sprite = GunnerSprite()
        #self.player_fsm = FSM() invinc frames

    def move(self, dx, dy):
        
        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.last_x = self.rect.x
            # Move the rect
            self.rect.x += dx * self.speed
        if dy != 0:
            self.last_y = self.rect.y
            # Move the rect
            self.rect.y += dy * self.speed

    
    def update(self):
        angle = math.atan2(self.rect.x-self.mouse_pos[0], self.rect.y-self.mouse_pos[1])

        walk = (self.left_pressed or self.right_pressed or self.up_pressed or self.down_pressed)

        self.player_sprite.update(angle,walk)
    
    def draw(self, display):
        self.player_sprite.draw(display,self.rect.x, self.rect.y)

    # getters and setters
    def getX(self):
        return self.rect.x
    
    def getY(self):
        return self.rect.y
    
    def get_rect(self):
        return self.rect

    def get_left_pressed(self):
        return self.left_pressed

    def get_right_pressed(self):
        return self.right_pressed

    def get_up_pressed(self):
        return self.up_pressed

    def get_down_pressed(self):
        return self.down_pressed

    def setX(self, x):
        self.rect.x = x
    
    def setY(self, y):
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

    def set_left_pressed(self, pressed):
        self.left_pressed = pressed
    
    def set_right_pressed(self, pressed):
        self.right_pressed = pressed
    
    def set_up_pressed(self, pressed):
        self.up_pressed = pressed
    
    def set_down_pressed(self, pressed):
        self.down_pressed = pressed
    
    def get_mouse_pos(self):
        return self.mouse_pos

    def set_mouse_pos(self, pos):
        self.mouse_pos = pos
    