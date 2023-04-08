import pygame

class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        #variable
        self.obstacleCostume_Index = 0
        self.animationSpeed = 0.3

        #setup images
        self.image_fireball_1 = pygame.image.load('fires/Fireball_1.png').convert_alpha()
        self.image_fireball_1 = pygame.transform.scale(self.image_fireball_1, (52,32))

        #setup multiple rects(share 'image_fireball_1' image)
        self.rect_fireball_1 = self.image_fireball_1.get_rect(midbottom = (0,400))
        self.rect_fireball_2 = self.image_fireball_1.get_rect(midbottom = (200,400))

        #load animation cuts
        self.fireball = []
        for i in range(1, 9):
            self.filename = 'fires/Fireball_' + str(i) + '.png'
            self.image_fireball_1 = pygame.image.load(self.filename).convert_alpha()
            self.fireball.append(self.image_fireball_1)
    
    def animation(self):
        self.image_fireball_1 = self.fireball[int(self.obstacleCostume_Index)]
        self.obstacleCostume_Index += self.animationSpeed
        if self.obstacleCostume_Index >= 7.6:
            self.animationSpeed = - 0.3
        elif self.obstacleCostume_Index < 4.4:
            self.animationSpeed = 0.1

    def timingObstacles(self, screen, start_time):
        self.start_time = start_time
        self.timer = "%.1f" %((pygame.time.get_ticks()-self.start_time)/1000)
        
        
        
        obstacle_class = Obstacle()
        fireball = obstacle_class.fireball()
        screen.blit(fireball[1], (0,0))

    def movement(self):
        self.rect_fireball_1.x += 4
        self.rect_fireball_2.x += 4


    def drawAll(self, surface):
        surface.blit(self.image_fireball_1, self.rect_fireball_1)
        surface.blit(self.image_fireball_1, self.rect_fireball_2)

    def setRect_fireball(self, num):
        var_name = 'rect_fireball_'+str(num)
        self.rect = getattr(self, var_name)

    def update(self, screen):
        self.animation()
        self.movement()
        self.drawAll(screen)


