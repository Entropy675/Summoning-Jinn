#file  -- test.py --
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
        
