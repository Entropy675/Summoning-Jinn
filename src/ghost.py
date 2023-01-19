import pygame
import random
import math
import basicSprite
import level
import entity
import enemy
import player


class Ghost(enemy.Enemy):

    meleRange = 25;
    currentSprite = 0;
    sprites = []; # basicSprite
    pathPoints = []; # location that it will go
    
    def __init__(self, x, y, pathPoints):
        self.range = 200
        self.pathPoints = pathPoints;
        self.maxPathPoint = len(pathPoints);
        self.speed = 1;
        
        image = pygame.image.load("..\\assets\\GothicCharacters\\GPV\\Ghost-Files\\PNG\\ghost-idle.png")
        
        self.original_image = image
        self.image = image
        self.rect = self.image.get_rect(); # change later to a set shape for hitbox?
        self.isEntityInanimate = False;
        
        self.sprites.append(basicSprite.BasicSprite(image, 0, 0, 7, 0, 0, 16 - self.speed)); # first animation: idle movement
        self.sprites.append(basicSprite.BasicSprite(pygame.image.load("..\\assets\\GothicCharacters\\GPV\\Ghost-Files\\PNG\\ghost-shriek.png"), 0, 0, 4, 1, 0, 16 - self.speed)); # second animation: attack
        self.sprites.append(basicSprite.BasicSprite(pygame.image.load("..\\assets\\GothicCharacters\\GPV\\Ghost-Files\\PNG\\ghost-vanish.png"), 0, 0, 7, 1, 0, 16 - self.speed)); # third animation: vanish (teleport ?) (die ?)
        self.sprites.append(basicSprite.BasicSprite(pygame.image.load("..\\assets\\GothicCharacters\\GPV\\Ghost-Files\\PNG\\ghost-appears.png"), 0, 0, 6, 1, 0, 16 - self.speed)); # third animation: appear (could be used for teleport)
        # basic sprite takes in image, x and y position for the image, image frame width, image frame height, ending offset, image speed
        
        super().__init__() 

    def path(self, plr):

        #checks if player is within range of goblin, if true it sets goblin path towards player
        if(self.sqrDistToPlayer(plr) < self.range*self.range): # range is a variable u declare at the start, represents the pixel range that the player needs to be within for the enemy to start chasing the player
            self.goToX = plr.x
            self.goToY = plr.y
            self.attacking = True;
        else:

                
            if(self.currentPathPoint == self.maxPathPoint):
                self.goToY = 10000;
            else:
                self.goToX = self.pathPoints[self.currentPathPoint][0] + self.boundryX
                self.goToY = self.pathPoints[self.currentPathPoint][1] + self.boundryY
                if(self.pathPoints[self.currentPathPoint][0] + self.boundryX == self.x and self.pathPoints[self.currentPathPoint][1] + self.boundryY == self.y):
                    self.currentPathPoint += 1;
                
            self.attacking = False;

    def attackBehavior(self, plr):
        attackType = random.randint(1, 100) #random number between 1 - 100 determines attack type
        
        if(attackType <= 80):
            currentSprite = 0 #80% chance the goblin will walk
        else:
            currentSprite = 1 # attack sprite
            


    def draw(self, surf):
        doneframe = None; # doneframe returns true when done animation
        
        if(self.facingLeft):
            doneframe = self.sprites[self.currentSprite].draw(surf, self.x + self.sprites[self.currentSprite].x - self.sprites[self.currentSprite].rect.width/2, self.y + self.sprites[self.currentSprite].y - self.sprites[self.currentSprite].rect.height/2, True);
        else:
            doneframe = self.sprites[self.currentSprite].draw(surf, self.x + self.sprites[self.currentSprite].x  - self.sprites[self.currentSprite].rect.width/2, self.y + self.sprites[self.currentSprite].y - self.sprites[self.currentSprite].rect.height/2);
        
        if(doneframe): # if we are on the last frame of the animation
            if(self.currentSprite == 1): # and its the attack sprite
                self.currentSprite = 0;
            self.sprites[self.currentSprite].currentFrameX = 0;
            self.sprites[self.currentSprite].currentFrameY = 0; 
        

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
        #print(str(self.x) + " " + str(self.y) + " goto " + str(self.goToX) + " " + str(self.goToY))
        # indicator for changing value : current problem can be resolved with ranges
        self.path(plr)
        if(self.attacking): 
            self.attackBehavior(plr)