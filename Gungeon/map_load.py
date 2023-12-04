import pygame
import json
import os
from sprites import SpriteSheet

class Tile:
    def __init__(self, image, x, y, tile_type):
        self.image = image
        self.hitBox = pygame.Rect(x,y,50,50)
        self.x = x
        self.y = y
        self.tile_type = tile_type
    def getX(self):
        return self.x

    def getY(self):
        return self.y
    
    def getHitBox(self):
        return self.hitBox
    
    def getType(self):
        return self.tile_type
    
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
-----------------------
PowerUps:
1 = Increased Max HP        (heals 1 heart)
2 = Increase Reload Speed   (-100, idk)
3 = Increase Speed          (+1 Speed)

4 = Crossbow                (Slower, + Damage)
5 = Magic Missle            (Descresed Area, faster)
6 = Cannon                  (Increased Area)

7 = Extra Blank
8 = Increased Max HP        (heals 1 heart)
9 = Surprise                ( Doggo? )

0 = Golden Gun              (3 Damage, Incresed Size, Less Ammo, Super slow)

F = Fountain (Restores Health)

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
    "F": (195, 178, 11, 12),
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
    fountain = None

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
            elif cell=="1" or cell=="2" or cell=="3" or cell=="4" or cell=="5" or cell=="6" or cell=="7" or cell=="8" or cell=="9" or cell=="0":
                image = sprite_sheet.get_image_wsize(sprite_locations["f"][0], sprite_locations["f"][1], sprite_locations["f"][2], sprite_locations["f"][3],48,48,(0,0,0))
                tile = Tile(image, idy*50, idx*50, cell)
                tiles.append(tile)

                image = sprite_sheet.get_image(sprite_locations["c"][0], sprite_locations["c"][1], sprite_locations["c"][2], sprite_locations["c"][3],3,(0,0,0))
                tile2 = Tile(image, idy*50, idx*50, cell)
                tiles.append(tile2)
                chests.append(tile2)
            elif cell=="F":
                image = sprite_sheet.get_image_wsize(sprite_locations["f"][0], sprite_locations["f"][1], sprite_locations["f"][2], sprite_locations["f"][3],48,48,(0,0,0))
                tile = Tile(image, idy*50, idx*50, cell)
                tiles.append(tile)

                image = sprite_sheet.get_image_wsize(sprite_locations[cell][0], sprite_locations[cell][1], sprite_locations[cell][2], sprite_locations[cell][3],48,48,(0,0,0))
                tile = Tile(image, idy*50, idx*50, cell)
                tiles.append(tile)
                fountain = tile
                
    return tiles, walls, spawners, chests, fountain