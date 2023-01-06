import pygame
import random
import basicSprite
import entity
import constants

class Player(entity.Entity):
    currentSprite = 0;
    sprites = []; # basicSprite
    
    HUDsprites = [];
    
    escapePoints = 15;
    frameCounter = 0
    
    cursorMark = None    #Sprite Click Object
    # assumes input image is in long strip format (use BasicSprite to handle)
    
    def __init__(self, x, y):
        super().__init__()
        
        self.speed = constants.PLR_SPEED;
        self.health = constants.PLR_MAX_HEALTH/2; # /2 for demonstration purposes
        self.maxHealth = constants.PLR_MAX_HEALTH;
        self.mana = constants.PLR_MAX_MANA/2; # /2 for demonstration purposes
        self.maxMana = constants.PLR_MAX_MANA;
        image = pygame.image.load("..\\assets\\GothicCharacters\\GPV\\demon-Files\\PNG\demon-idle.png");
        
        self.image = image
        self.rect = self.image.get_rect(); # change later to a set shape for hitbox?
        self.cursorMark =  basicSprite.BasicSprite(pygame.image.load("..\\assets\\PixelEffects\\10_weaponhit_spritesheet.png"), 0, 0, 6, 6, 5, 1);
        self.isEntityInanimate = False;
        
        # add all of the player sprites to the sprite list here
        # order added is the # position for currentSprite, starts at 0. 0 is assumed to be idle, 1 is assumed to be moving.
        self.sprites.append(basicSprite.BasicSprite(pygame.image.load("..\\assets\\GothicCharacters\\GPV\\demon-Files\\PNG\\demon-idle.png"), 0, 0, 6, 0, 0, constants.PLR_SPEED_BASE_LIMIT - self.speed));
        self.sprites.append(basicSprite.BasicSprite(pygame.image.load("..\\assets\\GothicCharacters\\GPV\\demon-Files\\PNG\\demon-attack.png"), -35, -30, 11, 0, 0, constants.PLR_SPEED_BASE_LIMIT - self.speed));
        
        # lets loed in the players HUD here too
        for i in range(self.escapePoints):
            self.HUDsprites.append(basicSprite.BasicSprite(pygame.image.load("..\\assets\\sprites\\healthAnimation.png"), random.randint(0, 10), random.randint(0, 10), 11, 11, 1, 4));
            self.HUDsprites[i].currentFrameX = random.randint(0, 10)
            self.HUDsprites[i].currentFrameY = random.randint(0, 10)
        
        self.goToX = x;
        self.goToY = y;
        self.x = x;
        self.y = y;
        
    
    def keyboardCheckDown(self, event): #When key is up
        if event == pygame.K_SPACE:
            if(self.currentSprite == 0):
                self.currentSprite = 1;
            self.sprites[self.currentSprite].currentFrameX = 0;
            self.sprites[self.currentSprite].currentFrameY = 0;
            self.removeHUDsprite();


    def keyboardCheckUp(self, event): #When key is up
        pass;
    

    def goToPoint(self,cord,screen):# When key is up
        self.goToX = cord[0] #;
        self.goToY = cord[1] #;
        
        if(cord[0] < self.x):
            self.facingLeft = False;
        else:
            self.facingLeft = True;
        
        self.frameCounter = 60

    def removeHUDsprite(self):
        self.HUDsprites.pop();
        self.escapePoints -= 1;

    def drawHUD(self, surf):
        # Create a surface for the transparent rect
        
        localZero = (0, surf.get_height() - 60); ## position for the top left corner of the HUD shadow box
        
        transparent_rect = pygame.Surface((300, 60))
        transparent_rect.fill(constants.BLACK)  # blk color
        transparent_rect.set_alpha(192)  # 75% alpha

        # Draw the transparent rect on the surface
        surf.blit(transparent_rect, (localZero[0], localZero[1]))

        font = pygame.font.Font(None, 36)  # use default font, size 36
        textsurf = font.render("x" + str(self.escapePoints), True, constants.WHITE)
        
        surf.blit(textsurf, (localZero[0] + 40, localZero[1] + 30));
        
        pygame.draw.rect(surf, constants.BLUE, pygame.Rect(85, localZero[1] + 20, 200*(self.mana/self.maxMana), 12))
        pygame.draw.rect(surf, constants.BLACK, pygame.Rect(85, localZero[1] + 20, 200, 12), 1)
        
        pygame.draw.rect(surf, constants.RED, pygame.Rect(85, localZero[1] + 40, 200*(self.health/self.maxHealth), 12))
        pygame.draw.rect(surf, constants.BLACK, pygame.Rect(85, localZero[1] + 40, 200, 12), 1)
        
        for i in self.HUDsprites:
            i.draw(surf,localZero[0] - 20 + i.x, localZero[1] -27 + i.y);

    def draw(self, surf):
    
        
        if self.frameCounter > 0:
            self.cursorMark.draw(surf, self.goToX - self.cursorMark.rect.width/2, self.goToY - self.cursorMark.rect.height/2)
            self.frameCounter -= 1;
        
        doneframe = None;
        
        if(self.facingLeft):
            doneframe = self.sprites[self.currentSprite].draw(surf, self.x + self.sprites[self.currentSprite].x - self.sprites[self.currentSprite].rect.width/2, self.y + self.sprites[self.currentSprite].y - self.sprites[self.currentSprite].rect.height/2, True);
        else:
            doneframe = self.sprites[self.currentSprite].draw(surf, self.x + self.sprites[self.currentSprite].x  - self.sprites[self.currentSprite].rect.width/2, self.y + self.sprites[self.currentSprite].y - self.sprites[self.currentSprite].rect.height/2);
        
        if(doneframe):
            if(self.currentSprite != 0 or self.currentSprite != 1):
                self.currentSprite = 0; #plr is attacking -> done = default sprite (idle). Avoids changing when already idle or running.
            self.sprites[self.currentSprite].currentFrameX = 0;
            self.sprites[self.currentSprite].currentFrameY = 0;
        

    def update(self):
        for i in self.HUDsprites:
            i.update();
        self.sprites[self.currentSprite].update();
        self.cursorMark.update();
        if self.y > self.goToY:
            self.y -= self.speed;
        if self.y < self.goToY:
            self.y += self.speed;
        if self.x > self.goToX:
            self.x -= self.speed;
        if self.x < self.goToX:
            self.x += self.speed;
        
