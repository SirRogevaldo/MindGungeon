import math
import time, copy, time, random
import pygame
from enemySprites import EnemySprite
from subject import Subject
import audio_manager

# Class Creation
class Monster(Subject):
    # Constructor:
    def __init__(self, x, y, health, speed):
        # Base attributes
        Subject.__init__(self)

        self.register("hit",self.get_shot)
        self.register("hit",audio_manager.Enemy_hit_play)

        self.health = health
        self.speed = speed
        self.hitBox = pygame.Rect(x, y, 50, 70)
        self.lastX = int(self.hitBox.x)
        self.lastY = int(self.hitBox.y)
        self.velX = 0
        self.velY = 0
        self.cooldown = pygame.time.get_ticks()
        self.bulletType = "shotgun"
        self.enemySprite = EnemySprite("Shotgun")

    def draw(self, display):
        self.enemySprite.draw(display, self.hitBox)

    def get_shot(self, entity):

        #print(entity)
        print("Enemy got shot")
        self.health -= entity.get_damage()
    
    def move(self, dx,dy):

        self.velX = 0
        self.velY = 0

        self.last_x = self.hitBox.x
        self.last_y = self.hitBox.y

        # Move the rect
        if (dx != 0):
            self.hitBox.x += dx * self.speed
            self.velX = dx
        elif (dy != 0):
            self.hitBox.y += dy * self.speed
            self.velY = dy

    # Clone Method:
    def clone(self):
        raise NotImplementedError("Subclasses must implement this method")
    
    def moveDecision(self,playerRect):
        raise NotImplementedError("Subclasses must implement this method")

    def fire(self):
        raise NotImplementedError("Subclasses must implement this method")
    
    def get_rect(self):
        return self.hitBox

    def getVelX(self):
        return self.velX

    def getVelY(self):
        return self.velY
    
    def getBulletType(self):
        return self.bulletType

    def get_health(self):
        return self.health

    def setX(self, x):
        self.hitBox.x = x
    
    def setY(self, y):
        self.hitBox.y = y
    
    
class Shotgun(Monster):
    def __init__(self,x,y):
        super().__init__(x,y,6, 1)

        self.register("shot",audio_manager.Shotgun_play)

        self.enemySprite = EnemySprite("Shotgun")
        self.recoil = 30
        self.atkSpeed = 10
        self.aura = random.randint(700,1000)
        self.awake = False
    
    def clone(self, x, y):
        return Shotgun(x, y)  
    
    def moveDecision(self, playerRect):

        self.last_x = self.hitBox.x
        self.last_y = self.hitBox.y

        xx = playerRect.x - self.hitBox.x # enemy to left of player
        yy = playerRect.y - self.hitBox.y # enemy to above of player
        moveQueue = []

        rand = random.randint(1,100)
        dist = math.sqrt((playerRect.x-self.hitBox.x)**2 + (playerRect.y-self.hitBox.y)**2)
        if(dist < self.aura):
            self.awake = True
        
        if(rand < 10):
            self.awake = False

        if(self.awake):
            if(xx > 0):
                moveQueue.append((1,0))
            elif(xx < 0):
                moveQueue.append((-1,0))
            if(yy > 0):
                moveQueue.append((0,1))
            elif(yy < 0):
                moveQueue.append((0,-1))
        else:
            moveQueue.append((0,-0))

        return moveQueue
    
    def fire(self):

        if(self.awake):
            now = pygame.time.get_ticks()
            if now - self.cooldown >= 1000:
                self.cooldown = pygame.time.get_ticks()
                self.notify(self,"shot")
                return True

        return False

class Mage(Monster):
    def __init__(self,x,y):
        super().__init__(x,y,4, 6)

        self.mana = 360
        self.manaRegen = 1

    def clone(self,x,y):
        return Mage(x,y)
    
    def fire(self):
        return 
    
class Sniper(Monster):
    def __init__(self,x,y):
        super().__init__(x,y,6, 4)
        
        self.cooldown = 30

    def clone(self,x,y):
        return Sniper(x,y)
    
    def moveDecision(self, playerRect):
        pass

    def fire(self):
        pass
    
class Spawner:
    def spawnMonster(self, prototype,x,y) -> Monster:
        return prototype.clone(x,y)