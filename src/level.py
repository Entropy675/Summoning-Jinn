# Define screen enums
from enum import Enum
import basicSprite
import pygame
import enemy

class Screen(Enum):
    LOADING = 0
    MAIN = 1
    PAUSE = 2
    DEATH = 3


def loadAssets():
    batchDrawUpdate = [];
    batchDrawUpdate.append(basicSprite.BasicSprite(pygame.image.load("..\\assets\\PixelEffects\\6_flamelash_spritesheet.png"), 60, 60, 7, 7, 3, 1))
    batchDrawUpdate.append(basicSprite.BasicSprite(pygame.image.load("..\\assets\\PixelEffects\\10_weaponhit_spritesheet.png"), 160, 160, 6, 6, 5, 1))
    batchDrawUpdate.append(basicSprite.BasicSprite(pygame.image.load("..\\assets\\PixelEffects\\13_vortex_spritesheet.png"), 230, 230, 8, 8, 3, 5))
    batchDrawUpdate.append(basicSprite.BasicSprite(pygame.image.load("..\\assets\\PixelEffects\\14_phantom_spritesheet.png"), 500, 500, 8, 8, 3, 1))
    batchDrawUpdate.append(basicSprite.BasicSprite(pygame.image.load("..\\assets\\PixelEffects\\18_midnight_spritesheet.png"), 400, 400, 8, 8, 3, 1))
    batchDrawUpdate.append(enemy.Enemy(pygame.image.load("..\\assets\\GothicCharacters\\GPV\\Ghost-Files\\PNG\\ghost-idle.png"), 100, 230, 7, 0, 0, 16))
    batchDrawUpdate.append(enemy.Enemy(pygame.image.load("..\\assets\\GothicCharacters\\GPV\\Ghost-Files\\PNG\\ghost-idle.png"), 100, 230, 7, 0, 0, 16))
    #assets\GothicCharacters\GPV\Ghost-Files\PNG
    return batchDrawUpdate;
