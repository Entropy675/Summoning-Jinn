import pygame
import random
import math
import levelEnum

# pygame.sprite.Sprite
# https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Sprite
# this class imports from the simple visible game objects base class in pygame
# ask me before messing with this class if you don't remember how pygame works, i'll show you. - SIB

class BasicSprite(pygame.sprite.Sprite):
    w = 30
    h = 30
    
    original_image = None;
    
    # assumes input image is in long strip format
    # may need to be refactored to work with 2d sprites
    imageFramesXMax = 0;
    imageFramesYMax = 0;
    currentFrameX = 0;
    currentFrameY = 0;
    
    frameWidth = 0;
    frameHeight = 0;
    
    offset = 0;
    nthFrame = 0; # the nth frame in which the current frame for the animation is updated
    
    doneFrame = False;
    
    def __init__(self, image, x, y, imfmx, imfmy, os, imgSpeed):
        
        # see setting up pygame.sprite.Sprite object in documentation
        super().__init__()
        self.original_image = image
        self.image = image
        self.rect = self.image.get_rect();
        
        self.x = x;
        self.y = y;
        
        self.nthFrame = imgSpeed; #imgspeed is the 
        
        if(imfmx == 0):
            imfmx = 1;
            
        self.imageFramesXMax = imfmx;
        
        if(imfmy == 0):
            imfmy = 1;
        
        self.offset = os + 1;
        self.imageFramesYMax = imfmy;
        self.frameHeight = self.rect.height/imfmy; # leave as be for now
        self.frameWidth = self.rect.width/imfmx;
        self.currentFrameX = 0;
        self.currentFrameY = 0;
        
    
    tempDelay = 0; # artificial delay, replace with timer for better functionality and frame independance 
    
    def draw(self, surf):
        #self.clip(self.image, self.frameWidth*self.currentFrameX, self.frameHeight*self.currentFrameY, self.frameWidth, self.frameHeight) 
        surf.blit(self.image, pygame.Rect((self.x, self.y), (self.frameWidth, self.frameHeight)))
        

    

    def update(self):
        doneFrame = False
        self.image = self.original_image.subsurface(self.rect)
        self.rect = pygame.Rect((self.currentFrameX*self.frameWidth,self.currentFrameY*self.frameHeight),(self.frameWidth, self.frameHeight));
        
        self.tempDelay += 1;
        if(self.tempDelay % self.nthFrame == 0):
            self.tempDelay = 0
            self.currentFrameX += 1;
            #print(f"xadd {self.currentFrameX}");
        
        if(self.currentFrameX == self.imageFramesXMax or ((self.currentFrameX == (self.imageFramesXMax - math.floor(self.offset % self.imageFramesXMax))) and (self.currentFrameY == (self.imageFramesYMax - math.floor(self.offset/self.imageFramesYMax) - 1)))):
            self.currentFrameX = 0;
            self.currentFrameY += 1;
            #print(f"yadd {self.currentFrameY}");
            
        
        if(self.currentFrameY == (self.imageFramesYMax - math.floor(self.offset/self.imageFramesYMax))):
            self.currentFrameY = 0;
            
            #print(f"ydone {self.currentFrameY}");
           