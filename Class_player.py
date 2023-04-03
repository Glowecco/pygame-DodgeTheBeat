import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, stand, jump, run):
        super().__init__()
        
        #variable
        self.playerCostume_Index = 0
        self.playerCostume_Index_2 = 0
        self.animationSpeed = 0.3
        self.animationSpeed_2 = 0.3
        self.flipLeft = False
        self.running = False
        self.gravity = -1
        self.stand = stand
        self.jump = jump
        self.run = run
        self.ALIVE = True

        #setup
        self.startImage = pygame.image.load('playerStand/rabbit -1.png').convert_alpha()
        self.startImage = pygame.transform.scale(self.startImage, (27, 42))
        self.image = self.startImage
        self.rect = self.image.get_rect(midbottom = (400,350))
        #save value
        self.animation()
    def animation(self):
        #stand
        keys = pygame.key.get_pressed()
        if self.rect.bottom == 400 and self.running==False: 
            self.image = self.stand[int(self.playerCostume_Index)]
            self.playerCostume_Index += self.animationSpeed
            if self.playerCostume_Index >= 7.5:
                self.animationSpeed = - 0.3
            elif self.playerCostume_Index < 0.5:
                self.animationSpeed = 0.3
        #jump
        if self.rect.bottom != 400: 
            self.image = self.jump
        #left and right
        elif keys[pygame.K_LEFT]:
            if self.playerCostume_Index_2 >= 9.5:
                self.animationSpeed_2 = -0.5
            elif self.playerCostume_Index_2 < 0.5:
                self.animationSpeed_2 = 0.5
            self.image = self.run[int(self.playerCostume_Index_2)]
            self.playerCostume_Index_2 += self.animationSpeed_2
        elif keys[pygame.K_RIGHT]:
            if self.playerCostume_Index_2 >= 9.5:
                self.animationSpeed_2 = -0.5
            elif self.playerCostume_Index_2 < 0.5:
                self.animationSpeed_2 = 0.5
            self.image = self.run[int(self.playerCostume_Index_2)]
            self.playerCostume_Index_2 += self.animationSpeed_2
        #flip image according to left/right
        self.image = pygame.transform.flip(self.image, self.flipLeft, False)
    def physicsLogic(self):
        if self.rect.bottom == 400:
            self.rect.y += self.gravity
        else:
            self.gravity += 0.4
            self.rect.y += self.gravity

        if 420 > self.rect.bottom >= 400 and 740>self.rect.x>33: 
            self.rect.bottom = 400
    
        if self.rect.bottom >600:
            self.ALIVE = False
    def movements(self):
        keys = pygame.key.get_pressed()
        #jump
        if keys[pygame.K_UP] and 420 > self.rect.bottom >= 400 and 740>self.rect.x>33:
            self.gravity = -9
        #left and right
        if keys[pygame.K_LEFT]:
            self.rect.left -= 4
            self.flipLeft = True
            self.running = True
        elif keys[pygame.K_RIGHT]:
            self.rect.right += 4
            self.flipLeft = False
            self.running = True
        else:
            self.running = False        
    def update(self):
        self.physicsLogic()
        self.movements()
        self.animation()
