'''
2D pixelart demake with minor tweaks of the competitive Mario Party 7 minigame Light Speed
https://www.mariowiki.com/Light_Speed
Code and graphics by Kevin Spathmann (Pfeifenreiniger on GitHub: https://github.com/Pfeifenreiniger)
Fonts used: "Mario Kart DS" by David (https://www.dafont.com/mario-kart-ds.font)
            "Super Mario 64 DS" by David (https://www.dafont.com/super-mario-64-ds.font)
Musics, SFX, and voices used from Nintendo™ originals (like Mario Party 3, 5, and 7, Super Smash Bros. 64 or Super Mario 64) and freesfx.co.uk
Original Game (included in Mario Party 7) by Hudson Soft™ and Nintendo™
'''

import pygame, sys, math
from background import Background, LightColumn
from tile import Tile
from player import Player, UP, LEFT, RIGHT, DOWN
from time_limit import display_time_limit
import cpu_opponent, menu
if __name__ == "__main__":
    pygame.init()
    start_ticks = pygame.time.get_ticks()  # starter tick

    ##----------------------------DISPLAY SCREEN----------------------------##

    SCREEN = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Light Speed 2D Demake")
    ICON = pygame.image.load("graphics/game_icon.png").convert_alpha()
    pygame.display.set_icon(ICON)
    clock = pygame.time.Clock()
    FPS = 30

    ##----------------------------BACKGROUND----------------------------##

    bg = Background()
    light_columns = [
        LightColumn("up"),
        LightColumn("left"),
        LightColumn("right"),
        LightColumn("down")
    ]

    ##----------------------------TILES----------------------------##

    p1_tile_r1c1 = Tile("red", 1, 1)
    p1_tile_r1c2 = Tile("red", 1, 2)
    p1_tile_r1c3 = Tile("red", 1, 3)
    p1_tile_r1c4 = Tile("red", 1, 4)
    p1_tile_r1c5 = Tile("red", 1, 5)
    p1_tile_r1c6 = Tile("red", 1, 6)
    p1_tile_r2c1 = Tile("red", 2, 1)
    p1_tile_r2c2 = Tile("red", 2, 2)
    p1_tile_r2c3 = Tile("red", 2, 3)
    p1_tile_r2c4 = Tile("red", 2, 4)
    p1_tile_r2c5 = Tile("red", 2, 5)
    p1_tile_r2c6 = Tile("red", 2, 6)
    p1_tile_r3c1 = Tile("red", 3, 1)
    p1_tile_r3c2 = Tile("red", 3, 2)
    p1_tile_r3c3 = Tile("red", 3, 3)
    p1_tile_r3c4 = Tile("red", 3, 4)
    p1_tile_r3c5 = Tile("red", 3, 5)
    p1_tile_r3c6 = Tile("red", 3, 6)
    p1_tile_r4c1 = Tile("red", 4, 1)
    p1_tile_r4c2 = Tile("red", 4, 2)
    p1_tile_r4c3 = Tile("red", 4, 3)
    p1_tile_r4c4 = Tile("red", 4, 4)
    p1_tile_r4c5 = Tile("red", 4, 5)
    p1_tile_r4c6 = Tile("red", 4, 6)
    p1_tile_r5c1 = Tile("red", 5, 1)
    p1_tile_r5c2 = Tile("red", 5, 2)
    p1_tile_r5c3 = Tile("red", 5, 3)
    p1_tile_r5c4 = Tile("red", 5, 4)
    p1_tile_r5c5 = Tile("red", 5, 5)
    p1_tile_r5c6 = Tile("red", 5, 6)
    p1_tile_r6c1 = Tile("red", 6, 1)
    p1_tile_r6c2 = Tile("red", 6, 2)
    p1_tile_r6c3 = Tile("red", 6, 3)
    p1_tile_r6c4 = Tile("red", 6, 4)
    p1_tile_r6c5 = Tile("red", 6, 5)
    p1_tile_r6c6 = Tile("red", 6, 6)
    p1_tiles = [
        p1_tile_r1c1, p1_tile_r1c2, p1_tile_r1c3, p1_tile_r1c4, p1_tile_r1c5, p1_tile_r1c6,
        p1_tile_r2c1, p1_tile_r2c2, p1_tile_r2c3, p1_tile_r2c4, p1_tile_r2c5, p1_tile_r2c6,
        p1_tile_r3c1, p1_tile_r3c2, p1_tile_r3c3, p1_tile_r3c4, p1_tile_r3c5, p1_tile_r3c6,
        p1_tile_r4c1, p1_tile_r4c2, p1_tile_r4c3, p1_tile_r4c4, p1_tile_r4c5, p1_tile_r4c6,
        p1_tile_r5c1, p1_tile_r5c2, p1_tile_r5c3, p1_tile_r5c4, p1_tile_r5c5, p1_tile_r5c6,
        p1_tile_r6c1, p1_tile_r6c2, p1_tile_r6c3, p1_tile_r6c4, p1_tile_r6c5, p1_tile_r6c6
    ]

    p2_tile_r1c1 = Tile("blue", 1, 1)
    p2_tile_r1c2 = Tile("blue", 1, 2)
    p2_tile_r1c3 = Tile("blue", 1, 3)
    p2_tile_r1c4 = Tile("blue", 1, 4)
    p2_tile_r1c5 = Tile("blue", 1, 5)
    p2_tile_r1c6 = Tile("blue", 1, 6)
    p2_tile_r2c1 = Tile("blue", 2, 1)
    p2_tile_r2c2 = Tile("blue", 2, 2)
    p2_tile_r2c3 = Tile("blue", 2, 3)
    p2_tile_r2c4 = Tile("blue", 2, 4)
    p2_tile_r2c5 = Tile("blue", 2, 5)
    p2_tile_r2c6 = Tile("blue", 2, 6)
    p2_tile_r3c1 = Tile("blue", 3, 1)
    p2_tile_r3c2 = Tile("blue", 3, 2)
    p2_tile_r3c3 = Tile("blue", 3, 3)
    p2_tile_r3c4 = Tile("blue", 3, 4)
    p2_tile_r3c5 = Tile("blue", 3, 5)
    p2_tile_r3c6 = Tile("blue", 3, 6)
    p2_tile_r4c1 = Tile("blue", 4, 1)
    p2_tile_r4c2 = Tile("blue", 4, 2)
    p2_tile_r4c3 = Tile("blue", 4, 3)
    p2_tile_r4c4 = Tile("blue", 4, 4)
    p2_tile_r4c5 = Tile("blue", 4, 5)
    p2_tile_r4c6 = Tile("blue", 4, 6)
    p2_tile_r5c1 = Tile("blue", 5, 1)
    p2_tile_r5c2 = Tile("blue", 5, 2)
    p2_tile_r5c3 = Tile("blue", 5, 3)
    p2_tile_r5c4 = Tile("blue", 5, 4)
    p2_tile_r5c5 = Tile("blue", 5, 5)
    p2_tile_r5c6 = Tile("blue", 5, 6)
    p2_tile_r6c1 = Tile("blue", 6, 1)
    p2_tile_r6c2 = Tile("blue", 6, 2)
    p2_tile_r6c3 = Tile("blue", 6, 3)
    p2_tile_r6c4 = Tile("blue", 6, 4)
    p2_tile_r6c5 = Tile("blue", 6, 5)
    p2_tile_r6c6 = Tile("blue", 6, 6)
    p2_tiles = [
        p2_tile_r1c1, p2_tile_r1c2, p2_tile_r1c3, p2_tile_r1c4, p2_tile_r1c5, p2_tile_r1c6,
        p2_tile_r2c1, p2_tile_r2c2, p2_tile_r2c3, p2_tile_r2c4, p2_tile_r2c5, p2_tile_r2c6,
        p2_tile_r3c1, p2_tile_r3c2, p2_tile_r3c3, p2_tile_r3c4, p2_tile_r3c5, p2_tile_r3c6,
        p2_tile_r4c1, p2_tile_r4c2, p2_tile_r4c3, p2_tile_r4c4, p2_tile_r4c5, p2_tile_r4c6,
        p2_tile_r5c1, p2_tile_r5c2, p2_tile_r5c3, p2_tile_r5c4, p2_tile_r5c5, p2_tile_r5c6,
        p2_tile_r6c1, p2_tile_r6c2, p2_tile_r6c3, p2_tile_r6c4, p2_tile_r6c5, p2_tile_r6c6
    ]

    def tile_placement():
        # player 1 places tiles
        if p1_tile_r1c1.active != True and p2_tile_r1c1.active != True and p1.rect.colliderect(p1_tile_r1c1):
            p1_tile_r1c1.active = True
            p1.cells["r1c1"] = True
        elif p1_tile_r1c2.active != True and p2_tile_r1c2.active != True and p1.rect.colliderect(p1_tile_r1c2):
            p1_tile_r1c2.active = True
            p1.cells["r1c2"] = True
        elif p1_tile_r1c3.active != True and p2_tile_r1c3.active != True and p1.rect.colliderect(p1_tile_r1c3):
            p1_tile_r1c3.active = True
            p1.cells["r1c3"] = True
        elif p1_tile_r1c4.active != True and p2_tile_r1c4.active != True and p1.rect.colliderect(p1_tile_r1c4):
            p1_tile_r1c4.active = True
            p1.cells["r1c4"] = True
        elif p1_tile_r1c5.active != True and p2_tile_r1c5.active != True and p1.rect.colliderect(p1_tile_r1c5):
            p1_tile_r1c5.active = True
            p1.cells["r1c5"] = True
        elif p1_tile_r1c6.active != True and p2_tile_r1c6.active != True and p1.rect.colliderect(p1_tile_r1c6):
            p1_tile_r1c6.active = True
            p1.cells["r1c6"] = True
        elif p1_tile_r2c1.active != True and p2_tile_r2c1.active != True and p1.rect.colliderect(p1_tile_r2c1):
            p1_tile_r2c1.active = True
            p1.cells["r2c1"] = True
        elif p1_tile_r2c2.active != True and p2_tile_r2c2.active != True and p1.rect.colliderect(p1_tile_r2c2):
            p1_tile_r2c2.active = True
            p1.cells["r2c2"] = True
        elif p1_tile_r2c3.active != True and p2_tile_r2c3.active != True and p1.rect.colliderect(p1_tile_r2c3):
            p1_tile_r2c3.active = True
            p1.cells["r2c3"] = True
        elif p1_tile_r2c4.active != True and p2_tile_r2c4.active != True and p1.rect.colliderect(p1_tile_r2c4):
            p1_tile_r2c4.active = True
            p1.cells["r2c4"] = True
        elif p1_tile_r2c5.active != True and p2_tile_r2c5.active != True and p1.rect.colliderect(p1_tile_r2c5):
            p1_tile_r2c5.active = True
            p1.cells["r2c5"] = True
        elif p1_tile_r2c6.active != True and p2_tile_r2c6.active != True and p1.rect.colliderect(p1_tile_r2c6):
            p1_tile_r2c6.active = True
            p1.cells["r2c6"] = True
        if p1_tile_r3c1.active != True and p2_tile_r3c1.active != True and p1.rect.colliderect(p1_tile_r3c1):
            p1_tile_r3c1.active = True
            p1.cells["r3c1"] = True
        elif p1_tile_r3c2.active != True and p2_tile_r3c2.active != True and p1.rect.colliderect(p1_tile_r3c2):
            p1_tile_r3c2.active = True
            p1.cells["r3c2"] = True
        elif p1_tile_r3c3.active != True and p2_tile_r3c3.active != True and p1.rect.colliderect(p1_tile_r3c3):
            p1_tile_r3c3.active = True
            p1.cells["r3c3"] = True
        elif p1_tile_r3c4.active != True and p2_tile_r3c4.active != True and p1.rect.colliderect(p1_tile_r3c4):
            p1_tile_r3c4.active = True
            p1.cells["r3c4"] = True
        elif p1_tile_r3c5.active != True and p2_tile_r3c5.active != True and p1.rect.colliderect(p1_tile_r3c5):
            p1_tile_r3c5.active = True
            p1.cells["r3c5"] = True
        elif p1_tile_r3c6.active != True and p2_tile_r3c6.active != True and p1.rect.colliderect(p1_tile_r3c6):
            p1_tile_r3c6.active = True
            p1.cells["r3c6"] = True
        if p1_tile_r4c1.active != True and p2_tile_r4c1.active != True and p1.rect.colliderect(p1_tile_r4c1):
            p1_tile_r4c1.active = True
            p1.cells["r4c1"] = True
        elif p1_tile_r4c2.active != True and p2_tile_r4c2.active != True and p1.rect.colliderect(p1_tile_r4c2):
            p1_tile_r4c2.active = True
            p1.cells["r4c2"] = True
        elif p1_tile_r4c3.active != True and p2_tile_r4c3.active != True and p1.rect.colliderect(p1_tile_r4c3):
            p1_tile_r4c3.active = True
            p1.cells["r4c3"] = True
        elif p1_tile_r4c4.active != True and p2_tile_r4c4.active != True and p1.rect.colliderect(p1_tile_r4c4):
            p1_tile_r4c4.active = True
            p1.cells["r4c4"] = True
        elif p1_tile_r4c5.active != True and p2_tile_r4c5.active != True and p1.rect.colliderect(p1_tile_r4c5):
            p1_tile_r4c5.active = True
            p1.cells["r4c5"] = True
        elif p1_tile_r4c6.active != True and p2_tile_r4c6.active != True and p1.rect.colliderect(p1_tile_r4c6):
            p1_tile_r4c6.active = True
            p1.cells["r4c6"] = True
        if p1_tile_r5c1.active != True and p2_tile_r5c1.active != True and p1.rect.colliderect(p1_tile_r5c1):
            p1_tile_r5c1.active = True
            p1.cells["r5c1"] = True
        elif p1_tile_r5c2.active != True and p2_tile_r5c2.active != True and p1.rect.colliderect(p1_tile_r5c2):
            p1_tile_r5c2.active = True
            p1.cells["r5c2"] = True
        elif p1_tile_r5c3.active != True and p2_tile_r5c3.active != True and p1.rect.colliderect(p1_tile_r5c3):
            p1_tile_r5c3.active = True
            p1.cells["r5c3"] = True
        elif p1_tile_r5c4.active != True and p2_tile_r5c4.active != True and p1.rect.colliderect(p1_tile_r5c4):
            p1_tile_r5c4.active = True
            p1.cells["r5c4"] = True
        elif p1_tile_r5c5.active != True and p2_tile_r5c5.active != True and p1.rect.colliderect(p1_tile_r5c5):
            p1_tile_r5c5.active = True
            p1.cells["r5c5"] = True
        elif p1_tile_r5c6.active != True and p2_tile_r5c6.active != True and p1.rect.colliderect(p1_tile_r5c6):
            p1_tile_r5c6.active = True
            p1.cells["r5c6"] = True
        if p1_tile_r6c1.active != True and p2_tile_r6c1.active != True and p1.rect.colliderect(p1_tile_r6c1):
            p1_tile_r6c1.active = True
            p1.cells["r6c1"] = True
        elif p1_tile_r6c2.active != True and p2_tile_r6c2.active != True and p1.rect.colliderect(p1_tile_r6c2):
            p1_tile_r6c2.active = True
            p1.cells["r6c2"] = True
        elif p1_tile_r6c3.active != True and p2_tile_r6c3.active != True and p1.rect.colliderect(p1_tile_r6c3):
            p1_tile_r6c3.active = True
            p1.cells["r6c3"] = True
        elif p1_tile_r6c4.active != True and p2_tile_r6c4.active != True and p1.rect.colliderect(p1_tile_r6c4):
            p1_tile_r6c4.active = True
            p1.cells["r6c4"] = True
        elif p1_tile_r6c5.active != True and p2_tile_r6c5.active != True and p1.rect.colliderect(p1_tile_r6c5):
            p1_tile_r6c5.active = True
            p1.cells["r6c5"] = True
        elif p1_tile_r6c6.active != True and p2_tile_r6c6.active != True and p1.rect.colliderect(p1_tile_r6c6):
            p1_tile_r6c6.active = True
            p1.cells["r6c6"] = True

        # player 2 places tiles
        if p2_tile_r1c1.active != True and p1_tile_r1c1.active != True and p2.rect.colliderect(p2_tile_r1c1):
            p2_tile_r1c1.active = True
            p2.cells["r1c1"] = True
        elif p2_tile_r1c2.active != True and p1_tile_r1c2.active != True and p2.rect.colliderect(p2_tile_r1c2):
            p2_tile_r1c2.active = True
            p2.cells["r1c2"] = True
        elif p2_tile_r1c3.active != True and p1_tile_r1c3.active != True and p2.rect.colliderect(p2_tile_r1c3):
            p2_tile_r1c3.active = True
            p2.cells["r1c3"] = True
        elif p2_tile_r1c4.active != True and p1_tile_r1c4.active != True and p2.rect.colliderect(p2_tile_r1c4):
            p2_tile_r1c4.active = True
            p2.cells["r1c4"] = True
        elif p2_tile_r1c5.active != True and p1_tile_r1c5.active != True and p2.rect.colliderect(p2_tile_r1c5):
            p2_tile_r1c5.active = True
            p2.cells["r1c5"] = True
        elif p2_tile_r1c6.active != True and p1_tile_r1c6.active != True and p2.rect.colliderect(p2_tile_r1c6):
            p2_tile_r1c6.active = True
            p2.cells["r1c6"] = True
        elif p2_tile_r2c1.active != True and p1_tile_r2c1.active != True and p2.rect.colliderect(p2_tile_r2c1):
            p2_tile_r2c1.active = True
            p2.cells["r2c1"] = True
        elif p2_tile_r2c2.active != True and p1_tile_r2c2.active != True and p2.rect.colliderect(p2_tile_r2c2):
            p2_tile_r2c2.active = True
            p2.cells["r2c2"] = True
        elif p2_tile_r2c3.active != True and p1_tile_r2c3.active != True and p2.rect.colliderect(p2_tile_r2c3):
            p2_tile_r2c3.active = True
            p2.cells["r2c3"] = True
        elif p2_tile_r2c4.active != True and p1_tile_r2c4.active != True and p2.rect.colliderect(p2_tile_r2c4):
            p2_tile_r2c4.active = True
            p2.cells["r2c4"] = True
        elif p2_tile_r2c5.active != True and p1_tile_r2c5.active != True and p2.rect.colliderect(p2_tile_r2c5):
            p2_tile_r2c5.active = True
            p2.cells["r2c5"] = True
        elif p2_tile_r2c6.active != True and p1_tile_r2c6.active != True and p2.rect.colliderect(p2_tile_r2c6):
            p2_tile_r2c6.active = True
            p2.cells["r2c6"] = True
        if p2_tile_r3c1.active != True and p1_tile_r3c1.active != True and p2.rect.colliderect(p2_tile_r3c1):
            p2_tile_r3c1.active = True
            p2.cells["r3c1"] = True
        elif p2_tile_r3c2.active != True and p1_tile_r3c2.active != True and p2.rect.colliderect(p2_tile_r3c2):
            p2_tile_r3c2.active = True
            p2.cells["r3c2"] = True
        elif p2_tile_r3c3.active != True and p1_tile_r3c3.active != True and p2.rect.colliderect(p2_tile_r3c3):
            p2_tile_r3c3.active = True
            p2.cells["r3c3"] = True
        elif p2_tile_r3c4.active != True and p1_tile_r3c4.active != True and p2.rect.colliderect(p2_tile_r3c4):
            p2_tile_r3c4.active = True
            p2.cells["r3c4"] = True
        elif p2_tile_r3c5.active != True and p1_tile_r3c5.active != True and p2.rect.colliderect(p2_tile_r3c5):
            p2_tile_r3c5.active = True
            p2.cells["r3c5"] = True
        elif p2_tile_r3c6.active != True and p1_tile_r3c6.active != True and p2.rect.colliderect(p2_tile_r3c6):
            p2_tile_r3c6.active = True
            p2.cells["r3c6"] = True
        if p2_tile_r4c1.active != True and p1_tile_r4c1.active != True and p2.rect.colliderect(p2_tile_r4c1):
            p2_tile_r4c1.active = True
            p2.cells["r4c1"] = True
        elif p2_tile_r4c2.active != True and p1_tile_r4c2.active != True and p2.rect.colliderect(p2_tile_r4c2):
            p2_tile_r4c2.active = True
            p2.cells["r4c2"] = True
        elif p2_tile_r4c3.active != True and p1_tile_r4c3.active != True and p2.rect.colliderect(p2_tile_r4c3):
            p2_tile_r4c3.active = True
            p2.cells["r4c3"] = True
        elif p2_tile_r4c4.active != True and p1_tile_r4c4.active != True and p2.rect.colliderect(p2_tile_r4c4):
            p2_tile_r4c4.active = True
            p2.cells["r4c4"] = True
        elif p2_tile_r4c5.active != True and p1_tile_r4c5.active != True and p2.rect.colliderect(p2_tile_r4c5):
            p2_tile_r4c5.active = True
            p2.cells["r4c5"] = True
        elif p2_tile_r4c6.active != True and p1_tile_r4c6.active != True and p2.rect.colliderect(p2_tile_r4c6):
            p2_tile_r4c6.active = True
            p2.cells["r4c6"] = True
        if p2_tile_r5c1.active != True and p1_tile_r5c1.active != True and p2.rect.colliderect(p2_tile_r5c1):
            p2_tile_r5c1.active = True
            p2.cells["r5c1"] = True
        elif p2_tile_r5c2.active != True and p1_tile_r5c2.active != True and p2.rect.colliderect(p2_tile_r5c2):
            p2_tile_r5c2.active = True
            p2.cells["r5c2"] = True
        elif p2_tile_r5c3.active != True and p1_tile_r5c3.active != True and p2.rect.colliderect(p2_tile_r5c3):
            p2_tile_r5c3.active = True
            p2.cells["r5c3"] = True
        elif p2_tile_r5c4.active != True and p1_tile_r5c4.active != True and p2.rect.colliderect(p2_tile_r5c4):
            p2_tile_r5c4.active = True
            p2.cells["r5c4"] = True
        elif p2_tile_r5c5.active != True and p1_tile_r5c5.active != True and p2.rect.colliderect(p2_tile_r5c5):
            p2_tile_r5c5.active = True
            p2.cells["r5c5"] = True
        elif p2_tile_r5c6.active != True and p1_tile_r5c6.active != True and p2.rect.colliderect(p2_tile_r5c6):
            p2_tile_r5c6.active = True
            p2.cells["r5c6"] = True
        if p2_tile_r6c1.active != True and p1_tile_r6c1.active != True and p2.rect.colliderect(p2_tile_r6c1):
            p2_tile_r6c1.active = True
            p2.cells["r6c1"] = True
        elif p2_tile_r6c2.active != True and p1_tile_r6c2.active != True and p2.rect.colliderect(p2_tile_r6c2):
            p2_tile_r6c2.active = True
            p2.cells["r6c2"] = True
        elif p2_tile_r6c3.active != True and p1_tile_r6c3.active != True and p2.rect.colliderect(p2_tile_r6c3):
            p2_tile_r6c3.active = True
            p2.cells["r6c3"] = True
        elif p2_tile_r6c4.active != True and p1_tile_r6c4.active != True and p2.rect.colliderect(p2_tile_r6c4):
            p2_tile_r6c4.active = True
            p2.cells["r6c4"] = True
        elif p2_tile_r6c5.active != True and p1_tile_r6c5.active != True and p2.rect.colliderect(p2_tile_r6c5):
            p2_tile_r6c5.active = True
            p2.cells["r6c5"] = True
        elif p2_tile_r6c6.active != True and p1_tile_r6c6.active != True and p2.rect.colliderect(p2_tile_r6c6):
            p2_tile_r6c6.active = True
            p2.cells["r6c6"] = True

        # player 1 overwrites player 2 tiles
        if p2_tile_r1c1.active and p1.rect.colliderect(p2_tile_r1c1.rect):
            p2_tile_r1c1.active = False
            p2.cells["r1c1"] = False
            p1_tile_r1c1.active = True
            p1.cells["r1c1"] = True
        elif p2_tile_r1c2.active and p1.rect.colliderect(p2_tile_r1c2.rect):
            p2_tile_r1c2.active = False
            p2.cells["r1c2"] = False
            p1_tile_r1c2.active = True
            p1.cells["r1c2"] = True
        elif p2_tile_r1c3.active and p1.rect.colliderect(p2_tile_r1c3.rect):
            p2_tile_r1c3.active = False
            p2.cells["r1c3"] = False
            p1_tile_r1c3.active = True
            p1.cells["r1c3"] = True
        elif p2_tile_r1c4.active and p1.rect.colliderect(p2_tile_r1c4.rect):
            p2_tile_r1c4.active = False
            p2.cells["r1c4"] = False
            p1_tile_r1c4.active = True
            p1.cells["r1c4"] = True
        elif p2_tile_r1c5.active and p1.rect.colliderect(p2_tile_r1c5.rect):
            p2_tile_r1c5.active = False
            p2.cells["r1c5"] = False
            p1_tile_r1c5.active = True
            p1.cells["r1c5"] = True
        elif p2_tile_r1c6.active and p1.rect.colliderect(p2_tile_r1c6.rect):
            p2_tile_r1c6.active = False
            p2.cells["r1c6"] = False
            p1_tile_r1c6.active = True
            p1.cells["r1c6"] = True
        elif p2_tile_r2c1.active and p1.rect.colliderect(p2_tile_r2c1.rect):
            p2_tile_r2c1.active = False
            p2.cells["r2c1"] = False
            p1_tile_r2c1.active = True
            p1.cells["r2c1"] = True
        elif p2_tile_r2c2.active and p1.rect.colliderect(p2_tile_r2c2.rect):
            p2_tile_r2c2.active = False
            p2.cells["r2c2"] = False
            p1_tile_r2c2.active = True
            p1.cells["r2c2"] = True
        elif p2_tile_r2c3.active and p1.rect.colliderect(p2_tile_r2c3.rect):
            p2_tile_r2c3.active = False
            p2.cells["r2c3"] = False
            p1_tile_r2c3.active = True
            p1.cells["r2c3"] = True
        elif p2_tile_r2c4.active and p1.rect.colliderect(p2_tile_r2c4.rect):
            p2_tile_r2c4.active = False
            p2.cells["r2c4"] = False
            p1_tile_r2c4.active = True
            p1.cells["r2c4"] = True
        elif p2_tile_r2c5.active and p1.rect.colliderect(p2_tile_r2c5.rect):
            p2_tile_r2c5.active = False
            p2.cells["r2c5"] = False
            p1_tile_r2c5.active = True
            p1.cells["r2c5"] = True
        elif p2_tile_r2c6.active and p1.rect.colliderect(p2_tile_r2c6.rect):
            p2_tile_r2c6.active = False
            p2.cells["r2c6"] = False
            p1_tile_r2c6.active = True
            p1.cells["r2c6"] = True
        elif p2_tile_r3c1.active and p1.rect.colliderect(p2_tile_r3c1.rect):
            p2_tile_r3c1.active = False
            p2.cells["r3c1"] = False
            p1_tile_r3c1.active = True
            p1.cells["r3c1"] = True
        elif p2_tile_r3c2.active and p1.rect.colliderect(p2_tile_r3c2.rect):
            p2_tile_r3c2.active = False
            p2.cells["r3c2"] = False
            p1_tile_r3c2.active = True
            p1.cells["r3c2"] = True
        elif p2_tile_r3c3.active and p1.rect.colliderect(p2_tile_r3c3.rect):
            p2_tile_r3c3.active = False
            p2.cells["r3c3"] = False
            p1_tile_r3c3.active = True
            p1.cells["r3c3"] = True
        elif p2_tile_r3c4.active and p1.rect.colliderect(p2_tile_r3c4.rect):
            p2_tile_r3c4.active = False
            p2.cells["r3c4"] = False
            p1_tile_r3c4.active = True
            p1.cells["r3c4"] = True
        elif p2_tile_r3c5.active and p1.rect.colliderect(p2_tile_r3c5.rect):
            p2_tile_r3c5.active = False
            p2.cells["r3c5"] = False
            p1_tile_r3c5.active = True
            p1.cells["r3c5"] = True
        elif p2_tile_r3c6.active and p1.rect.colliderect(p2_tile_r3c6.rect):
            p2_tile_r3c6.active = False
            p2.cells["r3c6"] = False
            p1_tile_r3c6.active = True
            p1.cells["r3c6"] = True
        elif p2_tile_r4c1.active and p1.rect.colliderect(p2_tile_r4c1.rect):
            p2_tile_r4c1.active = False
            p2.cells["r4c1"] = False
            p1_tile_r4c1.active = True
            p1.cells["r4c1"] = True
        elif p2_tile_r4c2.active and p1.rect.colliderect(p2_tile_r4c2.rect):
            p2_tile_r4c2.active = False
            p2.cells["r4c2"] = False
            p1_tile_r4c2.active = True
            p1.cells["r4c2"] = True
        elif p2_tile_r4c3.active and p1.rect.colliderect(p2_tile_r4c3.rect):
            p2_tile_r4c3.active = False
            p2.cells["r4c3"] = False
            p1_tile_r4c3.active = True
            p1.cells["r4c3"] = True
        elif p2_tile_r4c4.active and p1.rect.colliderect(p2_tile_r4c4.rect):
            p2_tile_r4c4.active = False
            p2.cells["r4c4"] = False
            p1_tile_r4c4.active = True
            p1.cells["r4c4"] = True
        elif p2_tile_r4c5.active and p1.rect.colliderect(p2_tile_r4c5.rect):
            p2_tile_r4c5.active = False
            p2.cells["r4c5"] = False
            p1_tile_r4c5.active = True
            p1.cells["r4c5"] = True
        elif p2_tile_r4c6.active and p1.rect.colliderect(p2_tile_r4c6.rect):
            p2_tile_r4c6.active = False
            p2.cells["r4c6"] = False
            p1_tile_r4c6.active = True
            p1.cells["r4c6"] = True
        elif p2_tile_r5c1.active and p1.rect.colliderect(p2_tile_r5c1.rect):
            p2_tile_r5c1.active = False
            p2.cells["r5c1"] = False
            p1_tile_r5c1.active = True
            p1.cells["r5c1"] = True
        elif p2_tile_r5c2.active and p1.rect.colliderect(p2_tile_r5c2.rect):
            p2_tile_r5c2.active = False
            p2.cells["r5c2"] = False
            p1_tile_r5c2.active = True
            p1.cells["r5c2"] = True
        elif p2_tile_r5c3.active and p1.rect.colliderect(p2_tile_r5c3.rect):
            p2_tile_r5c3.active = False
            p2.cells["r5c3"] = False
            p1_tile_r5c3.active = True
            p1.cells["r5c3"] = True
        elif p2_tile_r5c4.active and p1.rect.colliderect(p2_tile_r5c4.rect):
            p2_tile_r5c4.active = False
            p2.cells["r5c4"] = False
            p1_tile_r5c4.active = True
            p1.cells["r5c4"] = True
        elif p2_tile_r5c5.active and p1.rect.colliderect(p2_tile_r5c5.rect):
            p2_tile_r5c5.active = False
            p2.cells["r5c5"] = False
            p1_tile_r5c5.active = True
            p1.cells["r5c5"] = True
        elif p2_tile_r5c6.active and p1.rect.colliderect(p2_tile_r5c6.rect):
            p2_tile_r5c6.active = False
            p2.cells["r5c6"] = False
            p1_tile_r5c6.active = True
            p1.cells["r5c6"] = True
        elif p2_tile_r6c1.active and p1.rect.colliderect(p2_tile_r6c1.rect):
            p2_tile_r6c1.active = False
            p2.cells["r6c1"] = False
            p1_tile_r6c1.active = True
            p1.cells["r6c1"] = True
        elif p2_tile_r6c2.active and p1.rect.colliderect(p2_tile_r6c2.rect):
            p2_tile_r6c2.active = False
            p2.cells["r6c2"] = False
            p1_tile_r6c2.active = True
            p1.cells["r6c2"] = True
        elif p2_tile_r6c3.active and p1.rect.colliderect(p2_tile_r6c3.rect):
            p2_tile_r6c3.active = False
            p2.cells["r6c3"] = False
            p1_tile_r6c3.active = True
            p1.cells["r6c3"] = True
        elif p2_tile_r6c4.active and p1.rect.colliderect(p2_tile_r6c4.rect):
            p2_tile_r6c4.active = False
            p2.cells["r6c4"] = False
            p1_tile_r6c4.active = True
            p1.cells["r6c4"] = True
        elif p2_tile_r6c5.active and p1.rect.colliderect(p2_tile_r6c5.rect):
            p2_tile_r6c5.active = False
            p2.cells["r6c5"] = False
            p1_tile_r6c5.active = True
            p1.cells["r6c5"] = True
        elif p2_tile_r6c6.active and p1.rect.colliderect(p2_tile_r6c6.rect):
            p2_tile_r6c6.active = False
            p2.cells["r6c6"] = False
            p1_tile_r6c6.active = True
            p1.cells["r6c6"] = True

        # player 2 collides with player 1 tiles
        if p1_tile_r1c1.active and p2.rect.colliderect(p1_tile_r1c1.rect):
            p1_tile_r1c1.active = False
            p1.cells["r1c1"] = False
            p2_tile_r1c1.active = True
            p2.cells["r1c1"] = True
        elif p1_tile_r1c2.active and p2.rect.colliderect(p1_tile_r1c2.rect):
            p1_tile_r1c2.active = False
            p1.cells["r1c2"] = False
            p2_tile_r1c2.active = True
            p2.cells["r1c2"] = True
        elif p1_tile_r1c3.active and p2.rect.colliderect(p1_tile_r1c3.rect):
            p1_tile_r1c3.active = False
            p1.cells["r1c3"] = False
            p2_tile_r1c3.active = True
            p2.cells["r1c3"] = True
        elif p1_tile_r1c4.active and p2.rect.colliderect(p1_tile_r1c4.rect):
            p1_tile_r1c4.active = False
            p1.cells["r1c4"] = False
            p2_tile_r1c4.active = True
            p2.cells["r1c4"] = True
        elif p1_tile_r1c5.active and p2.rect.colliderect(p1_tile_r1c5.rect):
            p1_tile_r1c5.active = False
            p1.cells["r1c5"] = False
            p2_tile_r1c5.active = True
            p2.cells["r1c5"] = True
        elif p1_tile_r1c6.active and p2.rect.colliderect(p1_tile_r1c6.rect):
            p1_tile_r1c6.active = False
            p1.cells["r1c6"] = False
            p2_tile_r1c6.active = True
            p2.cells["r1c6"] = True
        elif p1_tile_r2c1.active and p2.rect.colliderect(p1_tile_r2c1.rect):
            p1_tile_r2c1.active = False
            p1.cells["r2c1"] = False
            p2_tile_r2c1.active = True
            p2.cells["r2c1"] = True
        elif p1_tile_r2c2.active and p2.rect.colliderect(p1_tile_r2c2.rect):
            p1_tile_r2c2.active = False
            p1.cells["r2c2"] = False
            p2_tile_r2c2.active = True
            p2.cells["r2c2"] = True
        elif p1_tile_r2c3.active and p2.rect.colliderect(p1_tile_r2c3.rect):
            p1_tile_r2c3.active = False
            p1.cells["r2c3"] = False
            p2_tile_r2c3.active = True
            p2.cells["r2c3"] = True
        elif p1_tile_r2c4.active and p2.rect.colliderect(p1_tile_r2c4.rect):
            p1_tile_r2c4.active = False
            p1.cells["r2c4"] = False
            p2_tile_r2c4.active = True
            p2.cells["r2c4"] = True
        elif p1_tile_r2c5.active and p2.rect.colliderect(p1_tile_r2c5.rect):
            p1_tile_r2c5.active = False
            p1.cells["r2c5"] = False
            p2_tile_r2c5.active = True
            p2.cells["r2c5"] = True
        elif p1_tile_r2c6.active and p2.rect.colliderect(p1_tile_r2c6.rect):
            p1_tile_r2c6.active = False
            p1.cells["r2c6"] = False
            p2_tile_r2c6.active = True
            p2.cells["r2c6"] = True
        elif p1_tile_r3c1.active and p2.rect.colliderect(p1_tile_r3c1.rect):
            p1_tile_r3c1.active = False
            p1.cells["r3c1"] = False
            p2_tile_r3c1.active = True
            p2.cells["r3c1"] = True
        elif p1_tile_r3c2.active and p2.rect.colliderect(p1_tile_r3c2.rect):
            p1_tile_r3c2.active = False
            p1.cells["r3c2"] = False
            p2_tile_r3c2.active = True
            p2.cells["r3c2"] = True
        elif p1_tile_r3c3.active and p2.rect.colliderect(p1_tile_r3c3.rect):
            p1_tile_r3c3.active = False
            p1.cells["r3c3"] = False
            p2_tile_r3c3.active = True
            p2.cells["r3c3"] = True
        elif p1_tile_r3c4.active and p2.rect.colliderect(p1_tile_r3c4.rect):
            p1_tile_r3c4.active = False
            p1.cells["r3c4"] = False
            p2_tile_r3c4.active = True
            p2.cells["r3c4"] = True
        elif p1_tile_r3c5.active and p2.rect.colliderect(p1_tile_r3c5.rect):
            p1_tile_r3c5.active = False
            p1.cells["r3c5"] = False
            p2_tile_r3c5.active = True
            p2.cells["r3c5"] = True
        elif p1_tile_r3c6.active and p2.rect.colliderect(p1_tile_r3c6.rect):
            p1_tile_r3c6.active = False
            p1.cells["r3c6"] = False
            p2_tile_r3c6.active = True
            p2.cells["r3c6"] = True
        elif p1_tile_r4c1.active and p2.rect.colliderect(p1_tile_r4c1.rect):
            p1_tile_r4c1.active = False
            p1.cells["r4c1"] = False
            p2_tile_r4c1.active = True
            p2.cells["r4c1"] = True
        elif p1_tile_r4c2.active and p2.rect.colliderect(p1_tile_r4c2.rect):
            p1_tile_r4c2.active = False
            p1.cells["r4c2"] = False
            p2_tile_r4c2.active = True
            p2.cells["r4c2"] = True
        elif p1_tile_r4c3.active and p2.rect.colliderect(p1_tile_r4c3.rect):
            p1_tile_r4c3.active = False
            p1.cells["r4c3"] = False
            p2_tile_r4c3.active = True
            p2.cells["r4c3"] = True
        elif p1_tile_r4c4.active and p2.rect.colliderect(p1_tile_r4c4.rect):
            p1_tile_r4c4.active = False
            p1.cells["r4c4"] = False
            p2_tile_r4c4.active = True
            p2.cells["r4c4"] = True
        elif p1_tile_r4c5.active and p2.rect.colliderect(p1_tile_r4c5.rect):
            p1_tile_r4c5.active = False
            p1.cells["r4c5"] = False
            p2_tile_r4c5.active = True
            p2.cells["r4c5"] = True
        elif p1_tile_r4c6.active and p2.rect.colliderect(p1_tile_r4c6.rect):
            p1_tile_r4c6.active = False
            p1.cells["r4c6"] = False
            p2_tile_r4c6.active = True
            p2.cells["r4c6"] = True
        elif p1_tile_r5c1.active and p2.rect.colliderect(p1_tile_r5c1.rect):
            p1_tile_r5c1.active = False
            p1.cells["r5c1"] = False
            p2_tile_r5c1.active = True
            p2.cells["r5c1"] = True
        elif p1_tile_r5c2.active and p2.rect.colliderect(p1_tile_r5c2.rect):
            p1_tile_r5c2.active = False
            p1.cells["r5c2"] = False
            p2_tile_r5c2.active = True
            p2.cells["r5c2"] = True
        elif p1_tile_r5c3.active and p2.rect.colliderect(p1_tile_r5c3.rect):
            p1_tile_r5c3.active = False
            p1.cells["r5c3"] = False
            p2_tile_r5c3.active = True
            p2.cells["r5c3"] = True
        elif p1_tile_r5c4.active and p2.rect.colliderect(p1_tile_r5c4.rect):
            p1_tile_r5c4.active = False
            p1.cells["r5c4"] = False
            p2_tile_r5c4.active = True
            p2.cells["r5c4"] = True
        elif p1_tile_r5c5.active and p2.rect.colliderect(p1_tile_r5c5.rect):
            p1_tile_r5c5.active = False
            p1.cells["r5c5"] = False
            p2_tile_r5c5.active = True
            p2.cells["r5c5"] = True
        elif p1_tile_r5c6.active and p2.rect.colliderect(p1_tile_r5c6.rect):
            p1_tile_r5c6.active = False
            p1.cells["r5c6"] = False
            p2_tile_r5c6.active = True
            p2.cells["r5c6"] = True
        elif p1_tile_r6c1.active and p2.rect.colliderect(p1_tile_r6c1.rect):
            p1_tile_r6c1.active = False
            p1.cells["r6c1"] = False
            p2_tile_r6c1.active = True
            p2.cells["r6c1"] = True
        elif p1_tile_r6c2.active and p2.rect.colliderect(p1_tile_r6c2.rect):
            p1_tile_r6c2.active = False
            p1.cells["r6c2"] = False
            p2_tile_r6c2.active = True
            p2.cells["r6c2"] = True
        elif p1_tile_r6c3.active and p2.rect.colliderect(p1_tile_r6c3.rect):
            p1_tile_r6c3.active = False
            p1.cells["r6c3"] = False
            p2_tile_r6c3.active = True
            p2.cells["r6c3"] = True
        elif p1_tile_r6c4.active and p2.rect.colliderect(p1_tile_r6c4.rect):
            p1_tile_r6c4.active = False
            p1.cells["r6c4"] = False
            p2_tile_r6c4.active = True
            p2.cells["r6c4"] = True
        elif p1_tile_r6c5.active and p2.rect.colliderect(p1_tile_r6c5.rect):
            p1_tile_r6c5.active = False
            p1.cells["r6c5"] = False
            p2_tile_r6c5.active = True
            p2.cells["r6c5"] = True
        elif p1_tile_r6c6.active and p2.rect.colliderect(p1_tile_r6c6.rect):
            p1_tile_r6c6.active = False
            p1.cells["r6c6"] = False
            p2_tile_r6c6.active = True
            p2.cells["r6c6"] = True

        p1_tile_r1c1.draw()
        p1_tile_r1c2.draw()
        p1_tile_r1c3.draw()
        p1_tile_r1c4.draw()
        p1_tile_r1c5.draw()
        p1_tile_r1c6.draw()
        p1_tile_r2c1.draw()
        p1_tile_r2c2.draw()
        p1_tile_r2c3.draw()
        p1_tile_r2c4.draw()
        p1_tile_r2c5.draw()
        p1_tile_r2c6.draw()
        p1_tile_r3c1.draw()
        p1_tile_r3c2.draw()
        p1_tile_r3c3.draw()
        p1_tile_r3c4.draw()
        p1_tile_r3c5.draw()
        p1_tile_r3c6.draw()
        p1_tile_r4c1.draw()
        p1_tile_r4c2.draw()
        p1_tile_r4c3.draw()
        p1_tile_r4c4.draw()
        p1_tile_r4c5.draw()
        p1_tile_r4c6.draw()
        p1_tile_r5c1.draw()
        p1_tile_r5c2.draw()
        p1_tile_r5c3.draw()
        p1_tile_r5c4.draw()
        p1_tile_r5c5.draw()
        p1_tile_r5c6.draw()
        p1_tile_r6c1.draw()
        p1_tile_r6c2.draw()
        p1_tile_r6c3.draw()
        p1_tile_r6c4.draw()
        p1_tile_r6c5.draw()
        p1_tile_r6c6.draw()

        p2_tile_r1c1.draw()
        p2_tile_r1c2.draw()
        p2_tile_r1c3.draw()
        p2_tile_r1c4.draw()
        p2_tile_r1c5.draw()
        p2_tile_r1c6.draw()
        p2_tile_r2c1.draw()
        p2_tile_r2c2.draw()
        p2_tile_r2c3.draw()
        p2_tile_r2c4.draw()
        p2_tile_r2c5.draw()
        p2_tile_r2c6.draw()
        p2_tile_r3c1.draw()
        p2_tile_r3c2.draw()
        p2_tile_r3c3.draw()
        p2_tile_r3c4.draw()
        p2_tile_r3c5.draw()
        p2_tile_r3c6.draw()
        p2_tile_r4c1.draw()
        p2_tile_r4c2.draw()
        p2_tile_r4c3.draw()
        p2_tile_r4c4.draw()
        p2_tile_r4c5.draw()
        p2_tile_r4c6.draw()
        p2_tile_r5c1.draw()
        p2_tile_r5c2.draw()
        p2_tile_r5c3.draw()
        p2_tile_r5c4.draw()
        p2_tile_r5c5.draw()
        p2_tile_r5c6.draw()
        p2_tile_r6c1.draw()
        p2_tile_r6c2.draw()
        p2_tile_r6c3.draw()
        p2_tile_r6c4.draw()
        p2_tile_r6c5.draw()
        p2_tile_r6c6.draw()

    def reset_tiles():
        for tile in p1_tiles:
            tile.active = False
        for tile in p2_tiles:
            tile.active = False

    ##----------------------------GAME MUSIC----------------------------##
    game_music = pygame.mixer.Sound("music/mparty7_Cool_as_a_Cucumber.mp3")
    game_music.set_volume(0.8)

    ##----------------------------PLAYER----------------------------##

    def player_overlapping():
        if p1.return_row_number() - p2.return_row_number() > 0:  # p2 overlaps p1
            p1.update()
            p2.update()
        else:  # p1 overlaps p2
            p2.update()
            p1.update()


    def player_start_movement():
        global start
        p1.right = True
        p1.key_direction = RIGHT
        p1.key_pressed = True

        p2.left = True
        p2.key_direction = LEFT
        p2.key_pressed = True

        start = True

    def player_collision_bounce():
        global horizontal_collision, vertical_collision

        if horizontal_collision:
            # p1 left, p2 right
            if (p1.rect.right > p2.rect.left) and (p1.rect.left < p2.rect.left):
                if p1.key_direction == RIGHT:
                    if p1.column0 != True:
                        p1.right = False
                        p1.left = True
                        p1.key_direction = LEFT
                if p2.key_direction == LEFT:
                    if p2.column7 != True:
                        p2.left = False
                        p2.right = True
                        p2.key_direction = RIGHT
            # p2 left, p1 right
            elif (p2.rect.right > p1.rect.left) and (p2.rect.left < p1.rect.left):
                if p2.key_direction == RIGHT:
                    if p2.column0 != True:
                        p2.right = False
                        p2.left = True
                        p2.key_direction = LEFT
                if p1.key_direction == LEFT:
                    if p1.column7 != True:
                        p1.left = False
                        p1.right = True
                        p1.key_direction = RIGHT
            horizontal_collision = False

        if vertical_collision:
            # p1 up, p2 down
            if (p1.rect.bottom > p2.rect.top) and (p1.rect.top < p2.rect.top):
                if p1.key_direction == DOWN:
                    if p1.row7 != True:
                        p1.down = False
                        p1.up = True
                        p1.key_direction = UP
                if p2.key_direction == UP:
                    if p2.row0 != True:
                        p2.up = False
                        p2.down = True
                        p2.key_direction = DOWN
            # p2 up, p1 down
            elif (p2.rect.bottom > p1.rect.top) and (p2.rect.top < p1.rect.top):
                if p2.key_direction == DOWN:
                    if p2.row7 != True:
                        p2.down = False
                        p2.up = True
                        p2.key_direction = UP
                if p1.key_direction == UP:
                    if p1.row0 != True:
                        p1.up = False
                        p1.down = True
                        p1.key_direction = DOWN
            vertical_collision = False

        # crash sfx
        p1.crash_sfx.play()
        p2.crash_sfx.play()



    def player_collision():
        global horizontal_collision, vertical_collision
        # horizontal collisions
        if p1.row1 and p2.row1:
            if (math.hypot(p1.x - p2.x, p1.y - p2.y) < 75):
                horizontal_collision = True
                player_collision_bounce()
        elif p1.row2 and p2.row2:
            if (math.hypot(p1.x - p2.x, p1.y - p2.y) < 65):
                horizontal_collision = True
                player_collision_bounce()
        elif p1.row3 and p2.row3:
            if (math.hypot(p1.x - p2.x, p1.y - p2.y) < 63):
                horizontal_collision = True
                player_collision_bounce()
        elif p1.row4 and p2.row4:
            if (math.hypot(p1.x - p2.x, p1.y - p2.y) < 60):
                horizontal_collision = True
                player_collision_bounce()
        elif p1.row5 and p2.row5:
            if (math.hypot(p1.x - p2.x, p1.y - p2.y) < 58):
                horizontal_collision = True
                player_collision_bounce()
        elif p1.row6 and p2.row6:
            if (math.hypot(p1.x - p2.x, p1.y - p2.y) < 56):
                horizontal_collision = True
                player_collision_bounce()
        # vertical collision
        elif p1.return_row_number() - p2.return_row_number() == 1 or p1.return_row_number() - p2.return_row_number() == -1:
            if (math.hypot(p1.x - p2.x, p1.y - p2.y) < 55):
                vertical_collision = True
                player_collision_bounce()

        # unblock teleports
        if (p1.row1 and p1.column0) and (p2.row1 and p2.column1):
            p2.up = False
            p2.left = False
            p2.right = True
            p2.down = False
            p2.key_direction = RIGHT
            p2.key_pressed = True
        elif (p2.row1 and p2.column0) and (p1.row1 and p1.column1):
            p1.up = False
            p1.left = False
            p1.right = True
            p1.down = False
            p1.key_direction = RIGHT
            p1.key_pressed = True
        elif (p1.row6 and p1.column7) and (p2.row6 and p2.column6):
            p2.up = False
            p2.left = True
            p2.right = False
            p2.down = False
            p2.key_direction = LEFT
            p2.key_pressed = True
        elif (p2.row6 and p2.column7) and (p1.row6 and p1.column6):
            p1.up = False
            p1.left = True
            p1.right = False
            p1.down = False
            p1.key_direction = LEFT
            p1.key_pressed = True
        elif (p1.row7 and p1.column1) and (p2.row6 and p2.column1):
            p2.up = False
            p2.left = False
            p2.right = False
            p2.down = True
            p2.key_direction = DOWN
            p2.key_pressed = True
        elif (p2.row7 and p2.column1) and (p1.row6 and p1.column1):
            p1.up = False
            p1.left = False
            p1.right = False
            p1.down = True
            p1.key_direction = DOWN
            p1.key_pressed = True
        elif (p1.row0 and p1.column6) and (p2.row1 and p2.column6):
            p2.up = True
            p2.left = False
            p2.right = False
            p2.down = False
            p2.key_direction = UP
            p2.key_pressed = True
        elif (p2.row0 and p2.column6) and (p1.row1 and p1.column6):
            p1.up = True
            p1.left = False
            p1.right = False
            p1.down = False
            p1.key_direction = UP
            p1.key_pressed = True


    def move_cpu_opponent(difficulty: str, p1: Player, p2: Player):
        direction = cpu_opponent.check_surrounding_tiles(difficulty, p1, p2)
        if p2.key_pressed != True:
            if direction == "up":
                p2.up = True
                p2.left = False
                p2.right = False
                p2.down = False
                p2.key_direction = UP
                p2.key_pressed = True
            elif direction == "left":
                p2.up = False
                p2.left = True
                p2.right = False
                p2.down = False
                p2.key_direction = LEFT
                p2.key_pressed = True
            elif direction == "right":
                p2.up = False
                p2.left = False
                p2.right = True
                p2.down = False
                p2.key_direction = RIGHT
                p2.key_pressed = True
            elif direction == "down":
                p2.up = False
                p2.left = False
                p2.right = False
                p2.down = True
                p2.key_direction = DOWN
                p2.key_pressed = True


    def game_restart():
        global start, game_active, menu, start_ticks
        start_ticks = pygame.time.get_ticks()
        start = False
        menu.title_music.stop()
        menu.score_music.stop()
        menu.title_music_played = False
        menu.score_music_played = False
        menu.menu_change()
        menu.sfx_score_screen_played = False
        game_active = True
        p1.player_reset()
        p2.player_reset()
        reset_tiles()


    ##----------------------------GAMELOOP----------------------------##

    horizontal_collision = False
    vertical_collision = False
    start = False
    numb_of_players = menu.numb_of_players
    p2_as_cpu = False
    first_start = True
    resetted = False
    game_active = False
    running = True


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            # non-active game -> browsing the menus
            if game_active != True:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and menu.which_menu == "numb_of_players":
                        menu.menu_cursor.menu_update()
                        numb_of_players = menu.menu_cursor.number_of_players
                    elif event.key == pygame.K_RETURN and menu.which_menu == "cpu_difficulty":
                        menu.cpu_diff_cursor.menu_update()
                        difficulty = menu.cpu_diff_cursor.cpu_difficulty
                    elif event.key == pygame.K_RETURN and (
                            menu.which_menu == "control_mapping" or menu.which_menu == "score_screen"):  # game retry
                        game_restart()
                        first_start = False
                        game_music.play(loops=-1)
                    elif event.key == pygame.K_SPACE and menu.which_menu == "score_screen":  # full game restart
                        game_restart()
                        menu.char_selected_reset()
                        first_start = True
                        game_active = False
                        p2_as_cpu = False
                    if menu.which_menu == "numb_of_players":
                        menu.menu_cursor.pressed = False
                    elif menu.which_menu == "char_select":
                        menu.p1_char_select.pressed = False
                        if numb_of_players > 1:
                            menu.p2_char_select.pressed = False
                    elif menu.which_menu == "cpu_difficulty":
                        menu.cpu_diff_cursor.pressed = False

        if game_active: # the actual game

            if start!= True:
                player_start_movement()

            bg.draw_assets()
            tile_placement()

            player_overlapping()

            for light_column in light_columns:
                light_column.draw_assets()

            game_active = display_time_limit(31, start_ticks)

            if p2_as_cpu:
                move_cpu_opponent("very hard", p1, p2)

            player_collision()

        else: # menu screens
            if first_start:
                if menu.title_music_played != True:
                    game_music.stop()
                    menu.title_music.play(loops=-1)
                    menu.title_music_played = True
                if menu.which_menu == "numb_of_players":
                    menu.display_menu_numb_of_players()
                    menu.menu_cursor.menu_update()
                elif menu.which_menu == "char_select":
                    menu.display_char_select()
                    menu.char_select_rect()
                    menu.p1_char_select.menu_update()
                    if menu.p1_char:
                        if menu.p1_char_select.player_initialized != True:
                            p1 = Player(menu.p1_char_select.character[:3], 1, False)
                            menu.p1_char_select.player_initialized = True
                        if numb_of_players == 1:
                            if menu.p2_char:
                                p2 = Player(menu.p1_char_select.cpu_character[:3], 2, True)
                                p2_as_cpu = True
                                menu.menu_change()
                    if numb_of_players > 1:
                        menu.p2_char_select.menu_update()
                        if menu.p2_char:
                            p2 = Player(menu.p2_char_select.character[:3], 2, False)
                            if numb_of_players == 2 and menu.p1_char and menu.p2_char:
                                menu.menu_change()
                elif menu.which_menu == "cpu_difficulty":
                    menu.display_cpu_difficulty()
                    menu.cpu_diff_cursor.menu_update()
                elif menu.which_menu == "control_mapping":
                    menu.display_control_mapping()

            else:
                if menu.score_music_played != True:
                    game_music.stop()
                    p1.hovercraft_sfx.stop()
                    p2.hovercraft_sfx.stop()
                    menu.score_music.play(loops=-1)
                    menu.score_music_played = True

                p1.calculate_score()
                score_message_surf_p1 = menu.mario64_font.render(f"P1: {str(p1.score)} {'tiles' if p1.score > 1 else 'tile'}", False, (25, 25, 25))
                score_message_rect_p1 = score_message_surf_p1.get_rect(center=(400, 110))
                p2.calculate_score()
                score_message_surf_p2 = menu.mario64_font.render(f"P2: {str(p2.score)} {'tiles' if p2.score > 1 else 'tile'}", False, (25, 25, 25))
                score_message_rect_p2 = score_message_surf_p2.get_rect(center=(400, 194))

                menu.display_score_screen()

                SCREEN.blit(score_message_surf_p1, score_message_rect_p1)
                SCREEN.blit(score_message_surf_p2, score_message_rect_p2)

        pygame.display.set_caption("Light Speed 2D Demake | " + str(round(clock.get_fps())) + " FPS")
        pygame.display.update()
        clock.tick(FPS)