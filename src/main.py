#file -- use_player.py --
import pygame
import random
import player

WIDTH = 360
HEIGHT = 480
FPS = 30

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


plr = player.Player(pygame.image.load("..\\assets\\GothicCharacters\\GPV\\demon-Files\\PNG\\demon-idle.png"), 30, 30, 6) # 6 frames in idle demon


## group all the sprites together for ease of update
# spriteGroup = pygame.sprite.Group() # <-- put normal sprites in there

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
            plr.keyboardCheckDown(event.key);
        elif event.type == pygame.KEYUP:
            plr.keyboardCheckUp(event.key);
        


    
    #2 Update normal sprites
    
    plr.update()
    # spriteGroup.update()


    #3 Draw/render
    
    screen.fill(BLACK)
    #pygame.draw.rect(screen, RED, pygame.Rect(plr.playerX, plr.playerY, 30, 30));
    
    plr.draw(screen)
    # spriteGroup.draw(screen)

    ########################

    ### Your code comes here

    ########################

    ## Done after drawing everything to the screen
    pygame.display.flip()       

pygame.quit()