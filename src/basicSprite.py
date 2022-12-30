import pygame
import random
import math
import level


# Defines the class BasicSprite which is used to create visible game effects in pygame
# not necessarily an entity
class BasicSprite(pygame.sprite.Sprite):
    # Stores the original image 
    original_image = None;
    
    # Stores the maximum number of image frames along x and y axes
    imageFramesXMax = 0;
    imageFramesYMax = 0;
    
    # Stores the current frame of the sprite
    currentFrameX = 0;
    currentFrameY = 0;
    
    # Stores the number of hit points
    hp = 0;
    
    # Stores the width and height of each frame
    frameWidth = 0;
    frameHeight = 0;
    
    # Stores the offset
    offset = 0;
    nthFrame = 0; # the nth frame in which the current frame for the animation is updated
    
    # Boolean indicating if the animation has finished
    doneFrame = False;
    
    # Stores the timer
    timer = 0;
    
    # Initializes the sprite
    def __init__(self, image, x, y, imfmx, imfmy, os, imgSpeed):
        # Sets up the pygame.sprite.Sprite object
        super().__init__()
        self.original_image = image
        self.image = image
        self.rect = self.image.get_rect();
        
        # Sets x and y coordinates
        self.x = x;
        self.y = y;
        
        
        # Sets the rate at which the frame is updated
        self.nthFrame = imgSpeed;
        
        # Sets the maximum number of frames along the x axis
        # If it is 0, it sets it to 1
        if(imfmx == 0):
            imfmx = 1;
        self.imageFramesXMax = imfmx;
        
        # Sets the maximum number of frames along the y axis
        # If it is 0, it sets it to 1
        if(imfmy == 0):
            imfmy = 1;
        self.offset = os;
        self.imageFramesYMax = imfmy;
        
        # Sets the width and height of each frame
        self.frameHeight = self.rect.height/imfmy;
        self.frameWidth = self.rect.width/imfmx;
        
        # Resets the current frame
        self.currentFrameX = 0;
        self.currentFrameY = 0;
    
    # Stores the timer
    timer = 0;
    
    # Draws the sprite on the specified surface
    def draw(self, surf , x = None, y = None, flip = None):
        
        doneFrame = False;
        
        # Increments the timer and updates the frame accordingly
        self.timer += 1;
        if(self.timer % self.nthFrame == 0):
            self.timer = 0
            self.currentFrameX += 1;
        
        # If the frame x index is the maximum frame x index or the offset frame x index and the frame y index is the offset frame y index, reset the frame x index
        if(self.currentFrameX == self.imageFramesXMax or ((self.currentFrameX == (self.imageFramesXMax - math.floor(self.offset % self.imageFramesXMax))) and (self.currentFrameY == (self.imageFramesYMax - math.floor(self.offset/self.imageFramesYMax) - 1)))):
            self.currentFrameX = 0;
            self.currentFrameY += 1;
            
        # If the frame y index is the offset frame y index, reset the frame y index
        if(self.currentFrameY == (self.imageFramesYMax - math.floor(self.offset/self.imageFramesYMax))):
            self.currentFrameY = 0;
            doneFrame = True
        # Returns a boolean indicating if the animation has finished
        # return doneFrame
        
        if flip != None:
            surf.blit(pygame.transform.flip(self.image.copy(), True, False), pygame.Rect((x, y), (self.frameWidth, self.frameHeight)))
        elif x != None:
            surf.blit(self.image, pygame.Rect((x, y), (self.frameWidth, self.frameHeight)))
        else:
            surf.blit(self.image, pygame.Rect((self.x, self.y), (self.frameWidth, self.frameHeight)))
            
        return doneFrame;
  
    

    # Updates the current frame
    def update(self):
        self.image = self.original_image.subsurface(self.rect)
        self.rect = pygame.Rect((self.currentFrameX*self.frameWidth,self.currentFrameY*self.frameHeight),(self.frameWidth, self.frameHeight));
        
