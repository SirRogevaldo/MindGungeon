import math
import pygame
import collision_detector

"""

    All_Bullets class:

    -Singleton class
    -This class is used to store all the bullets in the game. It is used to move and draw all the bullets in the game.

"""
class All_Bullets:
    def __init__(self):
        self.bullets = []

    def add(self, bullet):
        for b in bullet:
            self.bullets.append(b)
    
    def wipe(self,entity):
        self.bullets = []
    
    def move(self, walls,enemies, player):
        # Move Bullets    
        bullets_on_screen = []
        
        for b in self.bullets:
            b.move()
            if collision_detector.collision_bullet_walls(b, walls):
                pass
            elif collision_detector.collision_bullet_enemies(b, enemies):
                pass
            elif collision_detector.collision_bullet_player(b, player):
                pass
            else:
                bullets_on_screen.append(b)
        self.bullets = bullets_on_screen

    def draw(self, display):
        for b in self.bullets:
            b.draw(display)

    def get_bullets(self):
        return self.bullets