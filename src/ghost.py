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
        self.range = 20
        self.pathPoints = pathPoints;
        self.maxPathPoint = len(pathPoints);
        
        image = pygame.image.load("..assets\\GothicCharacters\\GPV\\Ghost-Files\\PNG\\ghost-idle.png")
        
        self.original_image = image
        self.image = image
        self.rect = self.image.get_rect(); # change later to a set shape for hitbox?
        self.isEntityInanimate = False;
        
        self.sprites.append(basicSprite.BasicSprite(image, 0, 0, 7, 0, 0, 16 - self.speed)); # first animation: idle movement
        self.sprites.append(basicSprite.BasicSprite(pygame.image.load("..assets\\GothicCharacters\\GPV\\Ghost-Files\\PNG\\ghost-shriek.png"), 0, 0, 4, 1, 0, 16 - self.speed)); # second animation: attack
        self.sprites.append(basicSprite.BasicSprite(pygame.image.load("..assets\\GothicCharacters\\GPV\\Ghost-Files\\PNG\\ghost-vanish.png"), 0, 0, 7, 1, 0, 16 - self.speed)); # third animation: vanish (teleport ?) (die ?)
        self.sprites.append(basicSprite.BasicSprite(pygame.image.load("..assets\\GothicCharacters\\GPV\\Ghost-Files\\PNG\\ghost-appears.png"), 0, 0, 6, 1, 0, 16 - self.speed)); # third animation: appear (could be used for teleport)
        # basic sprite takes in image, x and y position for the image, image frame width, image frame height, ending offset, image speed
        
        super().__init__(x, y) 

    def path(self):

        #checks if player is within range of goblin, if true it sets goblin path towards player
        if(self.sqrDistToPlayer(self, plr) < range*range): # range is a variable u declare at the start, represents the pixel range that the player needs to be within for the enemy to start chasing the player
            self.goToX = plr.x
            self.goToY = plr.y
            self.attacking = True;
        else:
            if(self.pathToPoints[self.currentPathPoint].x == self.x &&  self.pathToPoints[self.currentPathPoint].y == self.y):
                self.currentPathPoint += 1;
            if(self.currentPathPoint == self.maxPathPoint):
                self.goToY = -10000;
            else:
                self.goToX = self.pathToPoints[self.currentPathPoint].x
                self.goToY = self.pathToPoints[self.currentPathPoint].y
            self.attacking = False;
            # remove path to points [0] once they have reached it

    def attackBehavior(self):
        attackType = random.randint(1, 100) #random number between 1 - 100 determines attack type
        
        if(attackType <= 80):
            currentSprite = 0 #80% chance the goblin will walk
        elif(attackType <= 95):
            currentSprite = 1 #15% chance the goblin will try a basic attack(i think biting would be very funny but that can be for later)
        elif(attackType <= 100):
            currentSprite = 2 #5% chance the goblin will dash


    def draw(self, surf):
        super().draw(surf)
        

    def update(self):
        super().update()
        self.path(self)
        if(self.attacking): 
            self.attackBehavior(self)