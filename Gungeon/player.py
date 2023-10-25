import pygame
from FSM import FSM
from actor import Actor
from playerSprite import GunnerSprite
import math


#Gunman Class
class Gunman(Actor):
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        self.rect = pygame.Rect(self.x, self.y, 32, 32)
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
    
    def update(self):
        self.velX = 0
        self.velY = 0
        if self.left_pressed and not self.right_pressed:
            self.velX = -self.speed
        if self.right_pressed and not self.left_pressed:
            self.velX = self.speed
        if self.up_pressed and not self.down_pressed:
            self.velY = -self.speed
        if self.down_pressed and not self.up_pressed:
            self.velY = self.speed
        
        self.x += self.velX
        self.y += self.velY

        angle = math.atan2(self.x-self.mouse_pos[0], self.y-self.mouse_pos[1])

        walk = (self.left_pressed or self.right_pressed or self.up_pressed or self.down_pressed)

        self.player_sprite.update(angle,walk)
    
    def draw(self, display):
        self.player_sprite.draw(display,self.x, self.y)

    # getters and setters

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y

    def get_left_pressed(self):
        return self.left_pressed

    def get_right_pressed(self):
        return self.right_pressed

    def get_up_pressed(self):
        return self.up_pressed

    def get_down_pressed(self):
        return self.down_pressed

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
    