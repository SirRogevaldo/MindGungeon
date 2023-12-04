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

        self.coolTimer = pygame.time.get_ticks()

        # stats
        self.max_health = 6
        self.health = 6
        self.speed = 4
        self.chamber = 6
        self.maxChamber = 6
        self.cooldown = 300
        self.reloadSpeed = 800

        #wipe ability
        self.wipe_cooldown = 200
        self.wipe_timer = 0
        self.wipe_uses = 2

        self.player_gun = "normal"

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
        
    def wipe(self):
        if self.wipe_uses > 0 and pygame.time.get_ticks() - self.wipe_timer >= self.wipe_cooldown:
            self.wipe_timer = pygame.time.get_ticks()
            self.wipe_uses -= 1
            print("Wipe")
            self.notify(self,"wipe")
        else:
            print("No more wipes")

    def fire(self):
        now = pygame.time.get_ticks()

        # Check if enough time has passed since the last shot or reload
        if now - self.cooldown < 300:
            return False

        # Check if there are bullets in the chamber
        if self.chamber > 0:
            self.cooldown = now
            self.chamber -= 1
            return True

        # Check if enough time has passed since the last reload
        if now - self.cooldown >= self.reloadSpeed:
            self.cooldown = now
            self.chamber = self.maxChamber
            return False

        return False

        
        
    
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

    def getGun(self):
        return self.player_gun

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
    
    def setGun(self, gun):
        self.player_gun = gun
    
    