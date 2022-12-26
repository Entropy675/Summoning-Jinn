import pygame
import random
import time
import basicSprite

# pygame.sprite.Sprite
# https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Sprite
# this class imports from the simple visible game objects base class in pygame

class Player(pygame.sprite.Sprite):
    w = 30
    h = 30
    
    fps = 60; # hardcoded fps bad, link this to the fps in main (defs file?)
    
    plrUp = False
    plrDown = False
    plrRight = False
    plrLeft =  False
    
    facingLeft = False;
    
    x = 0;
    y = 0;
    goToX = 180
    goToY = 240
    plrSpeed = 6; # pix

    
    rect = None;
    original_image = None;
    
    currentSprite = 0;
    sprites = []; # basicSprite

    frameCounter = 0
    
    cursorMark = None    #Sprite Click Object
    # assumes input image is in long strip format
    # may need to be refactored to work with 2d sprites
    
    
    def __init__(self, x, y):
        
        # see setting up pygame.sprite.Sprite object in documentation
        
        super().__init__()
        
        # Summoning-Jinn\assets\GothicCharacters\GPV\Gothic-hero-Files\PNG
        image = pygame.image.load("..\\assets\\GothicCharacters\\GPV\\demon-Files\\PNG\demon-idle.png");
        
        self.original_image = image
        self.image = image
        self.rect = self.image.get_rect(); # change later to a set shape for hitbox?
        self.cursorMark =  basicSprite.BasicSprite(pygame.image.load("..\\assets\\PixelEffects\\10_weaponhit_spritesheet.png"), 0, 0, 6, 6, 5, 1);

        
        #plr = player.Player(, 150, 150, 6, 0, 10) # 6 frames in idle demon      
        
        # add all of the player sprites to the sprite list here
        # order added is the # position for currentSprite, starts at 0
        self.sprites.append(basicSprite.BasicSprite(pygame.image.load("..\\assets\\GothicCharacters\\GPV\\demon-Files\\PNG\\demon-idle.png"), 0, 0, 6, 0, 0, 16 - self.plrSpeed)); # should be fine
        self.sprites.append(basicSprite.BasicSprite(pygame.image.load("..\\assets\\GothicCharacters\\GPV\\demon-Files\\PNG\\demon-attack.png"), -35, -30, 11, 0, 0, 16 - self.plrSpeed)); # should be fine
        
        self.x = x;
        self.y = y;
        
    
    def keyboardCheckDown(self, event): #When key is up
        # if event.type == pygame.KEYDOWN:
        if event == pygame.K_w:
            self.plrUp = True;
        if event == pygame.K_a:
            self.plrLeft = True;
            self.facingLeft = False;
        if event == pygame.K_s:
            self.plrDown = True;
        if event == pygame.K_d:
            self.plrRight = True;
            self.facingLeft = True;
        if event == pygame.K_SPACE:
            self.currentSprite = not self.currentSprite; # really wacky
            self.sprites[self.currentSprite].currentFrameX = 0;
            self.sprites[self.currentSprite].currentFrameY = 0;

            


    def keyboardCheckUp(self, event):   #When key is up
        # if event.type == pygame.KEYUP:
        if event == pygame.K_w:
            self.plrUp = False;
        if event == pygame.K_a:
            self.plrLeft = False;
        if event == pygame.K_s:
            self.plrDown = False;
        if event == pygame.K_d:
            self.plrRight = False;
    

    def goToPoint(self,cord,screen):   #When key is up
        self.cursorMark.x = cord[0]
        self.goToX = cord[0]
        self.cursorMark.y = cord[1]
        self.goToY = cord[1]
        self.frameCounter = 60

        #Adding to the x and y so that it goes to desired point




    def draw(self, surf):

        # self.sprites[self.currentSprite].draw(surf, self.x, self.y);
        if self.frameCounter > 0:
            self.cursorMark.draw(surf,self.cursorMark.x,self.cursorMark.y)
            self.frameCounter =- 1
        doneframe = None;
        
        self.sprites[self.currentSprite].update();
        
        if(self.facingLeft):
            doneframe = self.sprites[self.currentSprite].draw(surf, self.x + self.sprites[self.currentSprite].x, self.y + self.sprites[self.currentSprite].y, True);
        else:
            doneframe = self.sprites[self.currentSprite].draw(surf, self.x + self.sprites[self.currentSprite].x + 30, self.y + self.sprites[self.currentSprite].y);
        #self.clip(self.image, self.frameWidth*self.currentFrameX, self.frameHeight*self.currentFrameY, self.frameWidth, self.frameHeight) 
        #surf.blit(self.image, pygame.Rect((self.x, self.y), (self.w, self.h))) #- self.w/2 - self.h/2
        
        if(doneframe):
            self.currentSprite = 0; #default sprite, either plr is running -> done = default sprite (idle), or plr is attacking -> done = default sprite (idle).
            self.sprites[self.currentSprite].currentFrameX = 0;
            self.sprites[self.currentSprite].currentFrameY = 0;
            # this means that the player pauses for a second after either of these? (that or change this)
        

    def update(self):
        self.sprites[self.currentSprite].update();
        self.cursorMark.update();
        if self.y > self.goToY:
            self.y -= self.plrSpeed;
        if self.y < self.goToY:
            self.y += self.plrSpeed;
        if self.x > self.goToX:
            self.x -= self.plrSpeed;
        if self.x < self.goToX:
            self.x += self.plrSpeed;
        
        
        # if (self.playerY + self.plrHeight) < pygame.Surface.get_rect(pygame.display.get_surface()).height:
            # self.playerY += self.grav #gravity
        # else:
            # self.playerY = pygame.Surface.get_rect(pygame.display.get_surface()).height - 30
        
