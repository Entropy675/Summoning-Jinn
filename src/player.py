import pygame
import random

# pygame.sprite.Sprite
# https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Sprite
# this class imports from the simple visible game objects base class in pygame
# ask me before messing with this class if you don't remember how pygame works, i'll show you. - SIB

class Player(pygame.sprite.Sprite):
    w = 30
    h = 30
    
    plrUp = False
    plrDown = False
    plrRight = False
    plrLeft =  False

    plrSpeed = 6; # pix
    
    rect = None;
    original_image = None;
    
    # assumes input image is in long strip format
    # may need to be refactored to work with 2d sprites
    imageFramesXMax = 0;
    imageFramesYMax = 0;
    currentFrameX = 0;
    currentFrameY = 0;
    frameWidth = 0;
    frameHeight = 0;
    nthFrame = 0;
    
    def __init__(self, image, x, y, imfmx, imfmy, imgSpeed):
        
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
        
        self.imageFramesYMax = imfmy;
        
        self.frameHeight = self.rect.height/imfmy; # leave as be for now
        self.frameWidth = self.rect.width/imfmx;
        self.currentFrameX = 0;
        self.currentFrameY = 0;
        


    def keyboardCheckDown(self, event):
        # if event.type == pygame.KEYDOWN:
        if event == pygame.K_w:
            self.plrUp = True;
        if event == pygame.K_a:
            self.plrLeft = True;
        if event == pygame.K_s:
            self.plrDown = True;
        if event == pygame.K_d:
            self.plrRight = True;


    def keyboardCheckUp(self, event):
        # if event.type == pygame.KEYUP:
        if event == pygame.K_w:
            self.plrUp = False;
        if event == pygame.K_a:
            self.plrLeft = False;
        if event == pygame.K_s:
            self.plrDown = False;
        if event == pygame.K_d:
            self.plrRight = False;
            
    
    tempDelay = 0; # artificial delay, replace with timer for better functionality and frame independance 
    
    def draw(self, surf):
        #self.clip(self.image, self.frameWidth*self.currentFrameX, self.frameHeight*self.currentFrameY, self.frameWidth, self.frameHeight) 
        surf.blit(self.image, pygame.Rect((self.x - self.w/2, self.y - self.h/2), (self.w, self.h)))
        

    

    def update(self):
        self.image = self.original_image.subsurface(self.rect)
        self.rect = pygame.Rect((self.currentFrameX*self.frameWidth,0),(self.frameWidth, self.frameHeight));
        
        self.tempDelay += 1;
        if(self.tempDelay % self.nthFrame == 0):
            self.tempDelay = 0
            self.currentFrameX += 1;
        
        if(self.currentFrameX == self.imageFramesXMax):
            self.currentFrameX = 0;
        
        if self.plrUp:
            self.y -= self.plrSpeed;
        if self.plrDown:
            self.y += self.plrSpeed;
        if self.plrLeft:
            self.x -= self.plrSpeed;
        if self.plrRight:
            self.x += self.plrSpeed;
        
        print(f'{self.x}, {self.y}, {self.frameWidth}')
        
        # if (self.playerY + self.plrHeight) < pygame.Surface.get_rect(pygame.display.get_surface()).height:
            # self.playerY += self.grav #gravity
        # else:
            # self.playerY = pygame.Surface.get_rect(pygame.display.get_surface()).height - 30
        
