import pygame
import random
import player
import basicSprite
import levelEnum

WIDTH = 360
HEIGHT = 480
FPS = 120 #pref

# Define Colors 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

## initialize pygame and create window
pygame.init()
pygame.mixer.init()  ## For sound
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("SUMMONING JINN")
clock = pygame.time.Clock()     ## For syncing the FPS



plr = player.Player(pygame.image.load("..\\assets\\GothicCharacters\\GPV\\demon-Files\\PNG\\demon-idle.png"), 150, 150, 6, 0, 10) # 6 frames in idle demon

basicSprites = [];
basicSprites.append(basicSprite.BasicSprite(pygame.image.load("..\\assets\\PixelEffects\\6_flamelash_spritesheet.png"), 60, 60, 7, 7, 3, 3));
basicSprites.append(basicSprite.BasicSprite(pygame.image.load("..\\assets\\PixelEffects\\10_weaponhit_spritesheet.png"), 160, 160, 6, 6, 5, 3));
basicSprites.append(basicSprite.BasicSprite(pygame.image.load("..\\assets\\PixelEffects\\13_vortex_spritesheet.png"), 230, 230, 8, 8, 4, 5));

## group all the sprites together for ease of update
# spriteGroup = pygame.sprite.Group(fireSpr) # <-- put normal sprites in there

## Game loop
running = True
while running:
    #1 Process input/events
    clock.tick(FPS)
    ## will make the loop run at the same speed all the time
    
    
    for event in pygame.event.get():        # gets all the events which have occured till now and keeps tab of them.
        ## listening for the the X button at the top
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE: # resizable fix
            screen = pygame.display.set_mode(event.size, pygame.RESIZABLE)
        elif event.type == pygame.KEYDOWN:
            plr.keyboardCheckDown(event.key);
        elif event.type == pygame.KEYUP:
            plr.keyboardCheckUp(event.key);


    
    #2 Update normal sprites
    
    plr.update()
    #spriteGroup.update();

    #3 Draw/render
    
    screen.fill(BLACK)
    #pygame.draw.rect(screen, RED, pygame.Rect(plr.playerX, plr.playerY, 30, 30));
    
    plr.draw(screen)
    
    for i in basicSprites:
        i.update();
        i.draw(screen);
    
    #spriteGroup.draw(screen)
    ########################

    ### Your code comes here

    ########################

    ## Done after drawing everything to the screen
    pygame.display.flip()       

pygame.quit()