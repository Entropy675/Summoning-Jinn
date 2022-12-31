import pygame
import random
import math
import basicSprite
import level
import entity
import player


class Goblin(enemy.Enemy):

    currentSprite = 0;
    sprites = []; # basicSprite
    pathPoints = []; # location that it will go
    
    def __init__(self, x, y):
        self.range = 20
        super().__init__() # do not create a lone instance of this class

    def sqrDistToPlayer(self, plr): # use this if you can help it because sqrt is a slow operation
        return math.abs(self.x - p.x)*math.abs(self.x - p.x) + math.abs(self.y - p.y)*math.abs(self.y - p.y); 
    
    def distToPlayer(self, plr): # dont use this if you can help it because it is slow
        return math.sqrt(sqrdDistToPlayer(self, plr));

    def path(self):

        if(self.sqrDistanceToPlayer(self, plr) < range*range): # range is a variable u declare at the start, represents the pixel range that the player needs to be within for the enemy to start chasing the player
            self.gotoX = plr.x
            self.gotoY = plr.y
            currentSprite = 1;
        else:
            self.gotoX = self.pathToPoints[0].x
            self.gotoY = self.pathToPoints[0].y
            #remove path to points [0] once they have reached it

    def attackBehavior(self):
        pass;

    def draw(self, surf):
        super().draw()
        

    def update(self):
        super().update()