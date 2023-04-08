import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        #variable
        self.playerCostume_Index = 0
        self.playerCostume_Index_2 = 0
        self.animationSpeed = 0.3
        self.animationSpeed_2 = 0.3
        self.flipLeft = False
        self.running = False
        self.gravity = -1
        self.ALIVE = True

        #setup image and rect
        self.image = pygame.image.load('playerStand/rabbit -1.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (27, 42))
        self.rect = self.image.get_rect(midbottom = (400,350))

        #load animation cuts
        self.stand = []
        self.run = []
        for i in range(1, 9):
            filename = f"{'playerStand/rabbit -'}{i}{'.png'}"
            temp_image = pygame.image.load(filename).convert_alpha()
            temp_image = pygame.transform.scale(temp_image, (27, 42))
            self.stand.append(temp_image)
        self.jump = pygame.image.load('playerJump/rabbit jump -2.png').convert_alpha()
        self.jump = pygame.transform.scale(self.jump, (28, 45))
        for i in range(1, 11):
            filename = f"{'playerRun/rabbit run -'}{i}{'.png'}"
            temp_image = pygame.image.load(filename).convert_alpha()
            temp_image = pygame.transform.scale(temp_image, (30, 43.5))
            self.run.append(temp_image)

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

        if 420 > self.rect.bottom >= 400 and 740>self.rect.x>33: 
            self.rect.bottom = 400
            self.gravity = 0
        else:
            self.gravity += 0.4
            self.rect.y += self.gravity

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
        self.movements()
        self.physicsLogic()
        self.animation()
