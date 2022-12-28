import pygame
import random
import player
import basicSprite
import level
import enemy

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

plr = player.Player(30, 30);
## group all the sprites together for ease of update
# spriteGroup = pygame.sprite.Group(fireSpr) # <-- put normal sprites in there

level1Img = pygame.image.load("..\\assets\\LevelImages\\Map1.png").convert()
level1Img = pygame.transform.scale(level1Img, (1280, 720))


## Game loop
batchDrawUpdate = level.loadAssets();
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
            level1X, level1Y = pygame.display.get_surface().get_size()
            level1Img = pygame.transform.scale(level1Img, (level1X, level1Y))
        elif event.type == pygame.KEYDOWN:
            plr.keyboardCheckDown(event.key);
        elif event.type == pygame.KEYUP:
            plr.keyboardCheckUp(event.key);
        elif event.type == pygame.MOUSEBUTTONDOWN:
            plr.goToPoint(pygame.mouse.get_pos(),screen);


    
    #2 Update normal sprites
    
    plr.update()
    #spriteGroup.update();

    #3 Draw/render
    
    screen.fill(BLACK)
    screen.blit(level1Img,(0,0))
    #pygame.draw.rect(screen, RED, pygame.Rect(plr.playerX, plr.playerY, 30, 30));
    
    plr.draw(screen)
    
    for i in batchDrawUpdate:
        i.update();
        i.draw(screen);
    
    #spriteGroup.draw(screen)
    ########################

    ### Your code comes here

    ########################

    ## Done after drawing everything to the screen
    pygame.display.flip()       

pygame.quit()