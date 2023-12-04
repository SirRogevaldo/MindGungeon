import pygame
import json
import os
from sprites import SpriteSheet

class Tile:
    def __init__(self, image, x, y, direction):
        self.image = image
        self.hitBox = pygame.Rect(x,y,50,50)
        self.x = x
        self.y = y
        self.direction = direction
    def getX(self):
        return self.x

    def getY(self):
        return self.y
    
    def getHitBox(self):
        return self.hitBox
    
    def getDirection(self):
        return self.direction
    
    def collides(self, rect):
        if self.hitBox.colliderect(rect):
            return True
        return False
"""
f = floor (walkable)
L = left corner  (wall)
R = right corner  (wall)
l = left wall  (wall)
r = right wall  (wall)
W = up wall  (wall)
w = down wall  (wall)
b = box (walkable)
c = chest (walkable)

"""
sprite_locations ={
    "f": (449, 97, 14, 14),
    "L": (293, 44, 16, 16),
    "l": (293, 19, 16, 16),
    "R": (331, 44, 16, 16),
    "r": (331, 19, 16, 16),
    "W": (308, 12, 16, 16),
    "w": (308, 44, 16, 16),
    "b": (81, 108, 14, 19),
    "c": (224, 176, 15, 15),
    "C": (224, 192, 15, 15),
}

def map_names():
    with open("map.json", "r") as f:
        level_file = json.load(f)
    return level_file.keys()


def map_load(level):
    with open("map.json", "r") as f:
        level_file = json.load(f)
    sprite_sheet = SpriteSheet(pygame.image.load(os.path.join('Assets', 'tileset.png')).convert_alpha())
    tiles = []
    walls = []
    chests = []
    spawners = []

    for idx,row in enumerate(level_file[level]):
        for idy,cell in enumerate(row):
            if cell == "f":
                image = sprite_sheet.get_image_wsize(sprite_locations[cell][0], sprite_locations[cell][1], sprite_locations[cell][2], sprite_locations[cell][3],48,48,(0,0,0))
                tile = Tile(image, idy*50, idx*50, cell)
                tiles.append(tile)
            if cell == "s" or cell == "S" or cell == "m" or cell == "M" or cell == "T":
                image = sprite_sheet.get_image_wsize(sprite_locations["f"][0], sprite_locations["f"][1], sprite_locations["f"][2], sprite_locations["f"][3],48,48,(0,0,0))
                tile = Tile(image, idy*50, idx*50, cell)
                tiles.append(tile)
                spawners.append((tile,cell))
            elif cell == "L" or cell == "l" or cell=="R" or cell=="r" or cell=="W" or cell=="w":
                image = sprite_sheet.get_image(sprite_locations[cell][0], sprite_locations[cell][1], sprite_locations[cell][2], sprite_locations[cell][3],3,(0,0,0))
                tile = Tile(image, idy*50, idx*50, cell)
                tiles.append(tile)
                walls.append(tile)
            elif cell == "b":
                image = sprite_sheet.get_image_wsize(sprite_locations[cell][0], sprite_locations[cell][1], sprite_locations[cell][2], sprite_locations[cell][3],48,48,(0,0,0))
                tile = Tile(image, idy*50, idx*50, cell)
                tiles.append(tile)
                walls.append(tile)
            elif cell=="c" or cell=="C":
                image = sprite_sheet.get_image(sprite_locations["f"][0], sprite_locations["f"][1], sprite_locations["f"][2], sprite_locations["f"][3],3,(0,0,0))
                tile = Tile(image, idy*50, idx*50, cell)
                tiles.append(tile)

                image = sprite_sheet.get_image(sprite_locations[cell][0], sprite_locations[cell][1], sprite_locations[cell][2], sprite_locations[cell][3],3,(0,0,0))
                tile2 = Tile(image, idy*50, idx*50, cell)
                tiles.append(tile2)
                chests.append(tile2)
    
    return tiles, walls, spawners

# 
# 