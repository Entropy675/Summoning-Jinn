import pygame
import random
import player
import basicSprite
import level
import enemy
import constants
import sys
import entity

## initialize pygame and create window
pygame.init()
pygame.mixer.init()  ## For sound
screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("SUMMONING JINN")
clock = pygame.time.Clock()     ## For syncing the FPS

plr = player.Player(130, 130);


levelImg = pygame.image.load("..\\assets\\LevelImages\\Map1.png").convert()
level1X, level1Y = (0,0);
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
            level1Xt, level1Yt = pygame.display.get_surface().get_size()
            
            # idk how tf i fixed this, but with this math the player stays in the same position even when the screen is resized -sib
            plr.x += (level1Xt / 2) - (levelImg.get_width() / 2) - level1X; # keep in mind the negative values matter for when going from bigger screen to smaller
            plr.goToX += (level1Xt / 2) - (levelImg.get_width() / 2) - level1X;
            plr.y += (level1Yt / 2) - (levelImg.get_height() / 2) - level1Y;
            plr.goToY += (level1Yt / 2) - (levelImg.get_height() / 2) - level1Y;
            
            for i in batchDrawUpdate:
                if(issubclass(type(i), entity.Entity)): # theoretically this should fix each entity (monster or enemy or anything) inside of the batchDrawUpdate array following above logic
                    i.x += (level1Xt / 2) - (levelImg.get_width() / 2) - level1X; # player is not inside of this array so we do it seperately above
                    i.goToX += (level1Xt / 2) - (levelImg.get_width() / 2) - level1X;
                    i.y += (level1Yt / 2) - (levelImg.get_height() / 2) - level1Y;
                    i.goToY += (level1Yt / 2) - (levelImg.get_height() / 2) - level1Y;
                if(issubclass(type(i), basicSprite.BasicSprite)): # this should fix the sprite effects to be in the right locations on resize
                    i.x += (level1Xt / 2) - (levelImg.get_width() / 2) - level1X; 
                    i.y += (level1Yt / 2) - (levelImg.get_height() / 2) - level1Y;
            
            level1X = (level1Xt / 2) - (levelImg.get_width() / 2)
            level1Y = (level1Yt / 2) - (levelImg.get_height() / 2)
            
            plr.boundryX = level1X;
            plr.boundryY = level1Y;
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
    screen.blit(levelImg, (level1X, level1Y))
    
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