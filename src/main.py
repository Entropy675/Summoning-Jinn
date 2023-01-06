import pygame
import random
import player
import basicSprite
import level
import enemy
import constants
import sys

## initialize pygame and create window
pygame.init()
pygame.mixer.init()  ## For sound
screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("SUMMONING JINN")
clock = pygame.time.Clock()     ## For syncing the FPS

plr = player.Player(130, 130);


levelImg = pygame.image.load("..\\assets\\LevelImages\\Map1.png").convert()
#level1Img = pygame.transform.scale(level1Img, (1280, 720))


## Game loop
batchDrawUpdate = level.loadAssets(); # get all assets from loadAssets() func in level file
running = True
while running:
    clock.tick(constants.FPS)
    ## will make the loop run at the same speed all the time
    
    for event in pygame.event.get(): # go through every event in pygame for every frame (whenever event occures, triggeres inside here)
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
        elif event.type == pygame.VIDEORESIZE: # resizable fix
            screen = pygame.display.set_mode(event.size, pygame.RESIZABLE)
            #level1X, level1Y = pygame.display.get_surface().get_size()
            #level1Img = pygame.transform.scale(level1Img, (level1X, level1Y))
        elif event.type == pygame.KEYDOWN:
            plr.keyboardCheckDown(event.key); # for attack when space pressed
            if event.key == pygame.K_ESCAPE:
                level.pause(screen)
        elif event.type == pygame.KEYUP:
            plr.keyboardCheckUp(event.key);
        elif event.type == pygame.MOUSEBUTTONDOWN:
            plr.goToPoint(pygame.mouse.get_pos(),screen);


    
    
    plr.update()
    
    screen.fill(constants.BLACK)
    screen.blit(levelImg,(0,0))
    
    #pygame.draw.rect(screen, RED, pygame.Rect(plr.playerX, plr.playerY, 30, 30));
    
    plr.draw(screen)
    
    for i in batchDrawUpdate: # update & draw everything in the array (all assets loaded)
        i.update();
        i.draw(screen);
        
    # Draw the HUD last so that it goes on top of everything
    plr.drawHUD(screen);

    ## Done after drawing everything to the screen
    pygame.display.flip()       

pygame.quit()