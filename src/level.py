import basicSprite
import pygame
import enemy
import goblin

def loadAssets():
    batchDrawUpdate = [];
    batchDrawUpdate.append(basicSprite.BasicSprite(pygame.image.load("..\\assets\\sprites\\spinningMana.png"), 60, 60, 8, 8, 4, 1))
    #batchDrawUpdate.append(basicSprite.BasicSprite(pygame.image.load("..\\assets\\PixelEffects\\10_weaponhit_spritesheet.png"), 160, 160, 6, 6, 5, 1)) #USE THIS
    batchDrawUpdate.append(basicSprite.BasicSprite(pygame.image.load("..\\assets\\PixelEffects\\13_vortex_spritesheet.png"), 230, 230, 8, 8, 3, 5))
    batchDrawUpdate.append(basicSprite.BasicSprite(pygame.image.load("..\\assets\\PixelEffects\\14_phantom_spritesheet.png"), 500, 500, 8, 8, 3, 1))
    batchDrawUpdate.append(basicSprite.BasicSprite(pygame.image.load("..\\assets\\PixelEffects\\18_midnight_spritesheet.png"), 400, 400, 8, 8, 3, 1))
    batchDrawUpdate.append(basicSprite.BasicSprite(pygame.image.load("..\\assets\\sprites\\summoningCircle.png"), 800, 500, 15, 15, 25, 1))
    #batchDrawUpdate.append(goblin.Goblin(600, 600));
    #batchDrawUpdate.append(goblin.Goblin(pygame.image.load("..\\assets\\Sprites\\goblin1V2_summoning_jinn.png"), 700)) 

    #assets\GothicCharacters\GPV\Ghost-Files\PNG
    #assets\ has all assets
    return batchDrawUpdate;


def pause(screen):
    pygame.font.init()
    font = pygame.font.SysFont('Comic Sans MS',115)
    textSurface = font.render('PAUSED', True, (204, 0, 0))
    pause = True
    X, Y = pygame.display.get_surface().get_size()
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pause = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause = False
              
        screen.blit(textSurface, (X/2-250,Y/2))
        pygame.display.flip()   