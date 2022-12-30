import pygame
import random
import math
import basicSprite
import level
import entity
# pygame.sprite.Sprite
# https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Sprite
# this class imports from the simple visible game objects base class in pygame
# ask me before messing with this class if you don't remember how pygame works, i'll show you. - SIB

class Enemy(entity.Entity):

    currentSprite = 0;
    sprites = []; # basicSprite
    pathPoints = []; # location that it will go
    
    def __init__(self, x, y):
        super().__init__() # do not create a lone instance of this class

    def distToPlayer(self):
        pass;
    
    def update(self):
        pass;
    
    def pathToPlayer(self):
        pass;
    
    def pathToGoal(self):
        pass;
    
    def attackBehavior(self):
        pass;

    def draw(self, surf):

        doneframe = None; # doneframe returns true when done animation
        
        self.sprites[self.currentSprite].update();
        
        if(self.facingLeft):
            doneframe = self.sprites[self.currentSprite].draw(surf, self.x + self.sprites[self.currentSprite].x - self.sprites[self.currentSprite].rect.width/2, self.y + self.sprites[self.currentSprite].y - self.sprites[self.currentSprite].rect.height/2, True);
        else:
            doneframe = self.sprites[self.currentSprite].draw(surf, self.x + self.sprites[self.currentSprite].x  - self.sprites[self.currentSprite].rect.width/2, self.y + self.sprites[self.currentSprite].y - self.sprites[self.currentSprite].rect.height/2);
        #self.clip(self.image, self.frameWidth*self.currentFrameX, self.frameHeight*self.currentFrameY, self.frameWidth, self.frameHeight) 
        #surf.blit(self.image, pygame.Rect((self.x, self.y), (self.w, self.h))) #- self.w/2 - self.h/2
        
        if(doneframe):
            self.currentSprite = 0; #default sprite, either plr is running -> done = default sprite (idle), or plr is attacking -> done = default sprite (idle).
            self.sprites[self.currentSprite].currentFrameX = 0;
            self.sprites[self.currentSprite].currentFrameY = 0; # resetting the current frame to the start of the animation loop after switching back to idle
        

    def update(self):
        self.sprites[self.currentSprite].update();
        if self.y > self.goToY:
            self.y -= self.plrSpeed;
        if self.y < self.goToY:
            self.y += self.plrSpeed;
        if self.x > self.goToX:
            self.x -= self.plrSpeed;
        if self.x < self.goToX:
            self.x += self.plrSpeed;
        
           