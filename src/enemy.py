import pygame
import random
import math
import basicSprite
import level
import entity
import player

class Enemy(entity.Entity):

    attacking = False;
    range = 0; #range for when goblin will follow player
    currentSprite = 0;
    currentPathPoint = 0;
    maxPathPoint = 0;
    sprites = []; # basicSprite
    pathPoints = []; # location that it will go
    
    def __init__(self):
        super().__init__() # do not create a lone instance of this class

    def sqrDistToPlayer(self, p): # use this if you can help it because sqrt is a slow operation
        return abs(self.x - p.x)*abs(self.x - p.x) + abs(self.y - p.y)*abs(self.y - p.y); 
    
    def distToPlayer(self, plr): # dont use this if you can help it because it is slow
        return math.sqrt(sqrdDistToPlayer(self, plr));

    def path(self, plr):
        pass;
    
    def attackBehavior(self, plr):
        pass;

    def draw(self, surf):

        doneframe = None; # doneframe returns true when done animation
        
        if(self.facingLeft):
            doneframe = self.sprites[self.currentSprite].draw(surf, self.x + self.sprites[self.currentSprite].x - self.sprites[self.currentSprite].rect.width/2, self.y + self.sprites[self.currentSprite].y - self.sprites[self.currentSprite].rect.height/2, True);
        else:
            doneframe = self.sprites[self.currentSprite].draw(surf, self.x + self.sprites[self.currentSprite].x  - self.sprites[self.currentSprite].rect.width/2, self.y + self.sprites[self.currentSprite].y - self.sprites[self.currentSprite].rect.height/2);
        
        if(doneframe): # if we are on the last frame of the animation
            if(self.currentSprite != 0 or self.currentSprite != 1):
                self.currentSprite = 0; # set the current sprite to 0 if we are not on idle or movement sprite, this resets attack animations when done
            self.sprites[self.currentSprite].currentFrameX = 0;
            self.sprites[self.currentSprite].currentFrameY = 0; # resetting the current frame to the start of the animation loop after switching back to idle
        

    def update(self, plr):
        self.sprites[self.currentSprite].update();
        if self.y > self.goToY:
            self.y -= self.speed;
        if self.y < self.goToY:
            self.y += self.speed;
        if self.x > self.goToX:
            self.x -= self.speed;
        if self.x < self.goToX:
            self.x += self.speed;
        