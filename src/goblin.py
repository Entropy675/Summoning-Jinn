import pygame
import random
import math
import basicSprite
import level
import entity
import enemy
import player


class Goblin(enemy.Enemy):

    range = 16 #range for when goblin will follow player

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

        #checks if player is within range of goblin, if true it sets goblin path towards player
        if(self.sqrDistToPlayer(self, plr) < range*range): # range is a variable u declare at the start, represents the pixel range that the player needs to be within for the enemy to start chasing the player
            self.gotoX = plr.x
            self.gotoY = plr.y
        else:
            self.gotoX = self.pathToPoints[0].x
            self.gotoY = self.pathToPoints[0].y
            #remove path to points [0] once they have reached it

    def attackBehavior(self):
    
        attackType = random.randint(1, 100) #random number between 1 - 100 determines attack type
        if(self.sqrDistToPlayer(self, plr) < 4*4):
            if(attackType <= 80):
                currentSprite = 0 #80% chance the goblin will walk
            elif(attackType <= 15):
                currentSprite = 1 #15% chance the goblin will try a basic attack(i think biting would be very funny but that can be for later)
            elif(attackType <= 5):
                currentSprite = 2 #5% chance the goblin will dash
        else:
            self.path(self)

    def draw(self, surf):
        super().draw()
        

    def update(self):
        super().update()
        if(self.attacking): 
            self.attackBehavior(self)