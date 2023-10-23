import math
import pygame

class All_Bullets:
    def __init__(self):
        self.bullets = []

    def add(self, bullet):
        self.bullets.append(bullet)

    def move(self, WIDTH, HEIGHT):
        # Move Bullets    
        bullets_on_screen = []
        
        for b in self.bullets:
            b.move()
            if 0 <= b.x <= WIDTH and 0 <= b.y <= HEIGHT:
                bullets_on_screen.append(b)
        self.bullets = bullets_on_screen

    def draw(self, display):
        for b in self.bullets:
            b.draw(display)