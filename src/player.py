import pygame
import random
import basicSprite

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

    x = 0;
    y = 0;
    plrSpeed = 6; # pix
    
    rect = None;
    original_image = None;
    
    currentSprite = 0;
    sprites = []; # basicSprite
    
    # assumes input image is in long strip format
    # may need to be refactored to work with 2d sprites
    
    
    def __init__(self, x, y):
        
        # see setting up pygame.sprite.Sprite object in documentation
        
        super().__init__()
        
        image = pygame.image.load("..\\assets\\GothicCharacters\\GPV\\demon-Files\\PNG\\demon-idle.png");
        
        self.original_image = image
        self.image = image
        self.rect = self.image.get_rect(); # change later to a set shape for hitbox?
        
        #plr = player.Player(, 150, 150, 6, 0, 10) # 6 frames in idle demon      
        
        # add all of the player sprites to the sprite list here
        # order added is the # position for currentSprite, starts at 0
        self.sprites.append(basicSprite.BasicSprite(pygame.image.load("..\\assets\\GothicCharacters\\GPV\\demon-Files\\PNG\\demon-idle.png"), x, y, 6, 0, 0, self.plrSpeed));
        
        self.x = x;
        self.y = y;
        

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
            
    
    
    def draw(self, surf):
        self.sprites[self.currentSprite].draw(surf, self.x, self.y);
        #self.clip(self.image, self.frameWidth*self.currentFrameX, self.frameHeight*self.currentFrameY, self.frameWidth, self.frameHeight) 
        #surf.blit(self.image, pygame.Rect((self.x, self.y), (self.w, self.h))) #- self.w/2 - self.h/2
        

    

    def update(self):
        
        self.sprites[self.currentSprite].update();
        
        if self.plrUp:
            self.y -= self.plrSpeed;
        if self.plrDown:
            self.y += self.plrSpeed;
        if self.plrLeft:
            self.x -= self.plrSpeed;
        if self.plrRight:
            self.x += self.plrSpeed;
        
        # if (self.playerY + self.plrHeight) < pygame.Surface.get_rect(pygame.display.get_surface()).height:
            # self.playerY += self.grav #gravity
        # else:
            # self.playerY = pygame.Surface.get_rect(pygame.display.get_surface()).height - 30
        
