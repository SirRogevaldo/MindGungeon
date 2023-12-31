import math
import pygame
import collision_detector
from subject import Subject
from bullet import Bullet
import audio_manager

"""
    All_Enemies class:

    -Singleton class
    -This class is used to store all the enemies in the game. It is used to move, draw, and make all enemies attack in the game.

"""

class All_Enemies(Subject):
    def __init__(self):
        self.enemies = []

    def add(self, enemy):
        self.enemies.append(enemy)

    def remove(self, enemy):
        self.enemies.remove(enemy)

    def update(self):
        for enemy in self.enemies:
            if enemy.get_health() <= 0:
                self.remove(enemy)
    
    def move(self, walls, player):
        for enemy in self.enemies:
            decision = enemy.moveDecision(player.get_rect())
            for command in decision:
                enemy.move(command[0],command[1])
                collision_detector.collision_entity_walls(enemy,walls)
    
    def attack(self, player):
        bullets = []
        shot = False
        for enemy in self.enemies:
            if enemy.fire():
                bullets.append(Bullet(enemy.hitBox.x, enemy.hitBox.y, player.getX(), player.getY(), enemy.getBulletType()))
                shot = True
        if shot:
            audio_manager.Shotgun_play(entity=None)
        return bullets

    def draw(self, display):
        for enemy in self.enemies:
            enemy.draw(display)
            enemy.enemySprite.update()


    def get_enemies(self):
        return self.enemies