import pygame

class Player(pygame.sprite.Sprite):
    dash_on = True
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
        self.higher = False
        self.doublejump_available = False
        self.x_vel = 4
        self.on_cooldown = False
        self.pressed_time = 0

        #setup image and rect
        self.image = pygame.image.load('images_player/playerStand/rabbit -1.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (27, 42))
        self.rect = self.image.get_rect(midbottom = (400,350))

        #load animation cuts
        self.stand = []
        self.run = []
        for i in range(1, 9):
            filename = f"{'images_player/playerStand/rabbit -'}{i}{'.png'}"
            temporary_image = pygame.image.load(filename).convert_alpha()
            temporary_image = pygame.transform.scale(temporary_image, (27, 42))
            self.stand.append(temporary_image)
        self.jump = pygame.image.load('images_player/playerJump/rabbit jump -2.png').convert_alpha()
        self.jump = pygame.transform.scale(self.jump, (28, 45))
        for i in range(1, 11):
            filename = f"{'images_player/playerRun/rabbit run -'}{i}{'.png'}"
            temporary_image = pygame.image.load(filename).convert_alpha()
            temporary_image = pygame.transform.scale(temporary_image, (30, 43.5))
            self.run.append(temporary_image)

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
            self.doublejump_available = True

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
            self.gravity = -8.5 
        #left and right
        if keys[pygame.K_LEFT]:
            self.rect.left -= self.x_vel
            self.flipLeft = True
            self.running = True
        elif keys[pygame.K_RIGHT]:
            self.rect.right += self.x_vel
            self.flipLeft = False
            self.running = True
        else:
            self.running = False  
        #skill
        if keys[pygame.K_x] and self.on_cooldown == False:
            self.pressed_time = int(pygame.time.get_ticks()/100)
            self.on_cooldown = True
            self.x_vel = 10
            self.gravity -= 3
            Player.dash_on = False
        if self.x_vel > 4:
            self.x_vel -= 0.15
        elif self.x_vel <4:
            self.x_vel = 4
        #skill cooldown (5 seconds)
        if (self.pressed_time+50) == (int(pygame.time.get_ticks()/100)):
            self.on_cooldown = False
            Player.dash_on = True

    def update(self):
        self.movements()
        self.physicsLogic()
        self.animation()
