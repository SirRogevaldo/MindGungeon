import math
import random
import pygame
from enemySprites import EnemySprite
from subject import Subject
import audio_manager

class Monster(Subject):
    def __init__(self, x, y, health, speed):
        Subject.__init__(self)

        self.register("hit", self.get_shot)
        self.register("hit", audio_manager.Enemy_hit_play)

        self.health = health
        self.speed = speed
        self.hitBox = pygame.Rect(x, y, 50, 70)
        self.lastX, self.lastY = int(self.hitBox.x), int(self.hitBox.y)
        self.velX, self.velY = 0, 0
        self.cooldown = pygame.time.get_ticks()
        self.bulletType = "shotgun"
        self.enemySprite = EnemySprite("Shotgun")
        self.awake = False

        self.chamber = 6
        self.maxChamber = 6
        self.reloadSpeed = 1000

    def draw(self, display):
        self.enemySprite.draw(display, self.hitBox)

    def get_shot(self, entity):
        print("Enemy got shot")
        self.health -= entity.get_damage()

    def move(self, dx, dy):
        self.velX, self.velY = 0, 0
        self.last_x, self.last_y = self.hitBox.x, self.hitBox.y

        if dx != 0:
            self.hitBox.x += dx * self.speed
            self.velX = dx
        elif dy != 0:
            self.hitBox.y += dy * self.speed
            self.velY = dy

    def clone(self):
        raise NotImplementedError("Subclasses must implement this method")

    def moveDecision(self, playerRect):
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
    def __init__(self, x, y):
        super().__init__(x, y, 6, 1)
        self.register("shot", audio_manager.Shotgun_play)
        self.enemySprite = EnemySprite("Shotgun")
        self.bulletType = "shotgun"
        self.atkSpeed = 500
        self.aura = random.randint(700, 1000)
        self.awake = False

    def clone(self, x, y):
        return Shotgun(x, y)

    def moveDecision(self, playerRect):
        self.last_x, self.last_y = self.hitBox.x, self.hitBox.y
        xx, yy = playerRect.x - self.hitBox.x, playerRect.y - self.hitBox.y
        moveQueue = []

        rand = random.randint(1, 100)
        dist = math.sqrt((playerRect.x - self.hitBox.x) ** 2 + (playerRect.y - self.hitBox.y) ** 2)

        if dist < self.aura:
            self.awake = True

        if rand < 10:
            self.awake = False

        if self.awake:
            moveQueue.extend([(1, 0) if xx > 0 else (-1, 0), (0, 1) if yy > 0 else (0, -1)])
        else:
            moveQueue.append((0, 0))

        return moveQueue

    def fire(self):
        now = pygame.time.get_ticks()

        if now - self.cooldown < self.atkSpeed:
            return False

        if self.chamber > 0:
            self.cooldown, self.chamber = now, self.chamber - 1
            return True

        if now - self.cooldown >= self.reloadSpeed:
            self.cooldown, self.chamber = now, self.maxChamber
            return False

        return False

class Mage(Monster):
    def __init__(self, x, y):
        super().__init__(x, y, 4, 1)
        self.bulletType = "magic"
        self.aura = random.randint(1000, 1200)

    def clone(self, x, y):
        return Mage(x, y)

    def moveDecision(self, playerRect):
        self.last_x, self.last_y = self.hitBox.x, self.hitBox.y
        xx, yy = playerRect.x - self.hitBox.x, playerRect.y - self.hitBox.y
        moveQueue = []

        rand = random.randint(1, 100)
        dist = math.sqrt((playerRect.x - self.hitBox.x) ** 2 + (playerRect.y - self.hitBox.y) ** 2)

        if dist < self.aura:
            self.awake = True

        if rand < 5:
            self.awake = False

        if self.awake:
            dx = min(self.speed, abs(xx)) * (1 if xx > 0 else -1)
            dy = min(self.speed, abs(yy)) * (1 if yy > 0 else -1)

            moveQueue.extend([(dx, 0), (0, dy)])
        else:
            moveQueue.append((0, 0))

        return moveQueue

    def fire(self):
        if self.awake:
            now = pygame.time.get_ticks()
            if now - self.cooldown >= 2300:
                self.cooldown = now
                return True

        return False

class Sniper(Monster):
    def __init__(self, x, y):
        super().__init__(x, y, 6, 1)
        self.cooldown, self.aura = 30, random.randint(1000, 1200)
        self.bulletType = "sniper"

    def clone(self, x, y):
        return Sniper(x, y)

    def moveDecision(self, playerRect):
        self.last_x, self.last_y = self.hitBox.x, self.hitBox.y
        xx, yy = playerRect.x - self.hitBox.x, playerRect.y - self.hitBox.y
        moveQueue = []

        rand = random.randint(1, 100)
        dist = math.sqrt((playerRect.x - self.hitBox.x) ** 2 + (playerRect.y - self.hitBox.y) ** 2)

        if dist < self.aura:
            self.awake = True

        if rand < 50:
            self.awake = False

        if self.awake:
            moveQueue.extend([(1, 0) if xx > 0 else (-1, 0), (0, 1) if yy > 0 else (0, -1)])
        else:
            moveQueue.append((0, 0))

        return moveQueue

    def fire(self):
        if self.awake:
            now = pygame.time.get_ticks()
            if now - self.cooldown >= 2000:
                self.cooldown = now
                return True

        return False
    

class Shade(Monster):
    def __init__(self, x, y):
        super().__init__(x, y, 45, 5)
        self.cooldown, self.aura = 30, 5000
        self.bulletType = "boss"
        self.awake = False
        self.next_change_direction = pygame.time.get_ticks() + random.randint(2000, 5000)
        self.enemySprite = EnemySprite("Shade")
        self.hitBox = pygame.Rect(x, y, 80, 120)

    def clone(self, x, y):
        return Shade(x, y)

    def moveDecision(self, playerRect):
        self.last_x, self.last_y = self.hitBox.x, self.hitBox.y
        moveQueue = []

        rand = random.randint(1, 100)
        dist = math.sqrt((playerRect.x - self.hitBox.x) ** 2 + (playerRect.y - self.hitBox.y) ** 2)

        if dist < self.aura:
            self.awake = True

        if self.awake:
            # Introduce periodic changes in direction
            now = pygame.time.get_ticks()
            if now > self.next_change_direction:
                self.next_change_direction = now + random.randint(2000, 5000)
                moveQueue.extend([(random.choice([-1, 1]), 0), (0, random.choice([-1, 1]))])
            else:
                moveQueue.extend([(1, 0) if random.choice([True, False]) else (-1, 0),
                                  (0, 1) if random.choice([True, False]) else (0, -1)])
        else:
            moveQueue.append((0, 0))
        
        #! REMOVER
        moveQueue = []
        moveQueue.append((0, 0))

        return moveQueue

    def fire(self):
        if self.awake:
            now = pygame.time.get_ticks()
            if now - self.cooldown >= 2000:
                self.cooldown = now
                return True

        return False

class Smiley(Monster):
    def __init__(self, x, y):
        super().__init__(x, y, 45, 5)
        self.cooldown, self.aura = 30, 5000
        self.bulletType = "boss"
        self.awake = False
        self.next_change_direction = pygame.time.get_ticks() + random.randint(2000, 5000)
        self.enemySprite = EnemySprite("Smiley")
        self.hitBox = pygame.Rect(x, y, 80, 120)

    def clone(self, x, y):
        return Smiley(x, y)

    def moveDecision(self, playerRect):
        self.last_x, self.last_y = self.hitBox.x, self.hitBox.y
        moveQueue = []

        rand = random.randint(1, 100)
        dist = math.sqrt((playerRect.x - self.hitBox.x) ** 2 + (playerRect.y - self.hitBox.y) ** 2)

        if dist < self.aura:
            self.awake = True

        if self.awake:
            # Introduce periodic changes in direction
            now = pygame.time.get_ticks()
            if now > self.next_change_direction:
                self.next_change_direction = now + random.randint(2000, 5000)
                moveQueue.extend([(random.choice([-1, 1]), 0), (0, random.choice([-1, 1]))])
            else:
                moveQueue.extend([(1, 0) if random.choice([True, False]) else (-1, 0),
                                  (0, 1) if random.choice([True, False]) else (0, -1)])
        else:
            moveQueue.append((0, 0))
        
        #! REMOVER
        moveQueue = []
        moveQueue.append((0, 0))

        return moveQueue

    def fire(self):
        if self.awake:
            now = pygame.time.get_ticks()
            if now - self.cooldown >= 2000:
                self.cooldown = now
                return True

        return False
    
class Target(Monster):
    def __init__(self, x, y):
        super().__init__(x, y, 1, 0)
        self.bulletType = "none"

    def clone(self, x, y):
        return Target(x, y)

    def moveDecision(self, playerRect):
        moveQueue = []
        moveQueue.append((0, 0))
        return moveQueue

    def fire(self):
        pass


class Spawner:
    def spawnMonster(self, prototype, x, y) -> Monster:
        return prototype.clone(x, y)
    
