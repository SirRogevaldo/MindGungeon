import pygame


# read json
import json

from sprites import SpriteSheet
with open("map.json", "r") as f:
    levels = json.load(f)



for idx,row in enumerate(levels[0]):
            for idy,cell in enumerate(row):
                if cell == "c":
                    image = SpriteSheet.subsurface(*spritelocations["wall"])
                    #50*16=800
                    image = pygame.transform.scale(image, (50, 50))
                    tile = Tile(image, idy*50, idx*50)
                    sprites.add(tile)
                    walls.append(tile)