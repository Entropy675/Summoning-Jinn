#!/usr/bin/env python2

import pygame
import random


WIDTH = 360
HEIGHT = 480
FPS = 30

# Define Colors 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class ChessPiece(pygame.sprite.Sprite):
    grav = 2
    playerX = 0
    playerY = 0
    plrWidth = 30
    plrHeight = 30
    plrUp = False
    plrDown = False
    plrRight = False
    plrLeft =  False
    plrSpeed = 6; # pix
    
    def __init__(self, image, x, y):
        super().__init__()
        self.original_image = image
        self.x = x;
        self.y = y;
        self.image = image
        self.rect = self.image.get_rect();

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
        surf.blit(self.image, pygame.Rect((self.playerX, self.playerY), (self.plrWidth, self.plrHeight)))
        
    def update(self):

        if self.plrUp:
            self.playerY -= self.plrSpeed;
        if self.plrDown:
            self.playerY += self.plrSpeed;
        if self.plrLeft:
            self.playerX -= self.plrSpeed;
        if self.plrRight:
            self.playerX += self.plrSpeed;
        
        print(f'{self.playerX}, {self.playerY}, {pygame.Surface.get_rect(pygame.display.get_surface()).height}')
        
        if (self.playerY + self.plrHeight) < pygame.Surface.get_rect(pygame.display.get_surface()).height:
            self.playerY += self.grav #gravity
        else:
            self.playerY = pygame.Surface.get_rect(pygame.display.get_surface()).height - 30
        


## initialize pygame and create window
pygame.init()
pygame.mixer.init()  ## For sound
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("SUMMONING JINN")
clock = pygame.time.Clock()     ## For syncing the FPS


sprite = ChessPiece(pygame.image.load("brownknight.png"), 30, 30)


## group all the sprites together for ease of update
spriteGroup = pygame.sprite.Group(sprite) # <-- put sprite in there

## Game loop
running = True
while running:

    #1 Process input/events
    clock.tick(FPS)     ## will make the loop run at the same speed all the time
    for event in pygame.event.get():        # gets all the events which have occured till now and keeps tab of them.
        ## listening for the the X button at the top
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE: # resizable fix
            screen = pygame.display.set_mode(event.size, pygame.RESIZABLE)
        elif event.type == pygame.KEYDOWN:
            sprite.keyboardCheckDown(event.key);
        elif event.type == pygame.KEYUP:
            sprite.keyboardCheckUp(event.key);
        


    
    #2 Update
    spriteGroup.update()


    #3 Draw/render
    screen.fill(BLACK)
    pygame.draw.rect(screen, RED, pygame.Rect(sprite.playerX, sprite.playerY, 30, 30));
    

    spriteGroup.draw(screen)
    ########################

    ### Your code comes here

    ########################

    ## Done after drawing everything to the screen
    pygame.display.flip()       

pygame.quit()