import pygame
import random
import math
import level

# pygame.sprite.Sprite
# https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Sprite
# this class imports from the simple visible game objects base class in pygame
# all entities should extend this class

class Entity(pygame.sprite.Sprite):
    health = 0;
    maxHealth = 0;
    mana = 0;
    healthbarpos = pygame.math.Vector2(0, 0) # use vectors to represent points
    isEntityInanimate = True;
    facingLeft = False;
    x = 0;
    y = 0;    
    goToX = 0;
    goToY = 0;
    speed = 0; # pix
    rect = None;
    original_image = None;