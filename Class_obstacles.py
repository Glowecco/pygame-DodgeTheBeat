import pygame

class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        #variable
        self.fireballCostume_Index = 0
        self.animationSpeed_1 = 0.3
        self.firepillarCostume_Index = 0
        self.animationSpeed_2 = 0.25
        self.firegroundCostume_Index = 0
        self.animationSpeed_3 = 0.4
        self.coords_under = (5,400)
        self.coords_top = (800,355)
        self.coords_untouched = (0,0)
        self.activate_1 = False
        self.activate_2 = False
        self.alpha = 400
        self.runthis = False

        #setup images
        self.temporary_fireball = pygame.image.load('fires/fireball/Fireball_1.png').convert_alpha()
        self.temporary_fireball = pygame.transform.scale(self.temporary_fireball, (32, 32))
        self.temporary_firepillar = pygame.image.load('fires/firepillar/pillar_1.png').convert_alpha()
        self.temporary_firepillar = pygame.transform.scale(self.temporary_firepillar, (192, 500))
        self.temporary_fireground = pygame.image.load('fires/flameFloor/fireGround_1.png').convert_alpha()
        self.temporary_fireground = pygame.transform.scale(self.temporary_fireground, (750,60))

        #setup rects
        self.rect_fireball_1 = self.temporary_fireball.get_rect(midbottom = self.coords_under)
        self.rect_fireball_2 = self.temporary_fireball.get_rect(midbottom = self.coords_under)
        self.rect_fireball_3 = self.temporary_fireball.get_rect(midbottom = self.coords_under)
        self.rect_fireball_4 = self.temporary_fireball.get_rect(midbottom = self.coords_top)
        self.rect_fireball_5 = self.temporary_fireball.get_rect(midbottom = self.coords_top)
        self.rect_fireball_6 = self.temporary_fireball.get_rect(midbottom = self.coords_top)
        self.rect_firepillar_1 = self.temporary_firepillar.get_rect(midbottom = self.coords_untouched)
        self.rect_firepillar_2 = self.temporary_firepillar.get_rect(midbottom = self.coords_untouched)
        self.rect_fireground = self.temporary_fireground.get_rect(midbottom = self.coords_untouched)

        #load animation cuts
        self.fireball = []
        for i in range(1, 9):
            self.filename = 'fires/fireball/Fireball_' + str(i) + '.png'
            self.temporary_fireball = pygame.image.load(self.filename).convert_alpha()
            self.temporary_fireball = pygame.transform.scale(self.temporary_fireball, (32, 32))
            self.fireball.append(self.temporary_fireball)

        self.firepillar = []
        for i in range(1, 11):
            self.filename = 'fires/firepillar/pillar_' + str(i) + '.png'
            self.temporary_firepillar = pygame.image.load(self.filename).convert_alpha()
            self.temporary_firepillar = pygame.transform.scale(self.temporary_firepillar, (192, 500))
            self.firepillar.append(self.temporary_firepillar)
        
        self.fireground = []
        for i in range(1, 10):
            self.filename = 'fires/flameFloor/fireGround_' + str(i) + '.png'
            self.temporary_fireground = pygame.image.load(self.filename).convert_alpha()
            self.temporary_fireground = pygame.transform.scale(self.temporary_fireground, (750,60))
            self.fireground.append(self.temporary_fireground)
    def animation(self):
        self.image_fireball = self.fireball[int(self.fireballCostume_Index)]
        self.fireballCostume_Index += self.animationSpeed_1
        if self.fireballCostume_Index >= 7.6:
            self.animationSpeed_1 = - 0.3
        elif self.fireballCostume_Index < 2.4:
            self.animationSpeed_1 = 0.3
        
        if self.activate_1 == True:
            self.image_firepillar = self.firepillar[int(self.firepillarCostume_Index)]
            self.firepillarCostume_Index += self.animationSpeed_2
            if self.firepillarCostume_Index >= 8.6:
                self.animationSpeed_2 = 0
        elif self.activate_1 == False:
            self.image_firepillar = None
        
        if self.activate_2 == True:
            self.image_fireground = self.fireground[int(self.firegroundCostume_Index)]
            self.firegroundCostume_Index += self.animationSpeed_2
            self.image_fireground.set_alpha(self.alpha)
            if self.firegroundCostume_Index >= 7.5:
                self.firegroundCostume_Index = 0

            if self.alpha < 0:
                pass
            else:
                self.alpha -= 20

    def timingObstacles(self, start_time):
        self.start_time = start_time
        self.timer = "%.1f" %((pygame.time.get_ticks()-self.start_time)/1000)
        self.timer = float(self.timer)
        print(self.timer)

    def queue(self, surface):
        self.image_fireball_flipped = pygame.transform.flip(self.image_fireball, True, False)
        #horizontal fire balls
#cycle 1
        if 4 >= self.timer >= 0:
            surface.blit(self.image_fireball, self.rect_fireball_1)
            self.rect_fireball_1.x += 4
            surface.blit(self.image_fireball_flipped, self.rect_fireball_4)
            self.rect_fireball_4.x -= 4
        elif self.timer == 4.1:
            self.rect_fireball_1.midbottom = self.coords_under
            self.rect_fireball_4.midbottom = self.coords_top

        if 5 >= self.timer >= 1:
            surface.blit(self.image_fireball, self.rect_fireball_2)
            self.rect_fireball_2.x += 4
        if 5.3 >= self.timer >= 1.3:
            surface.blit(self.image_fireball_flipped, self.rect_fireball_5)
            self.rect_fireball_5.x -= 4
        elif self.timer == 5.4:
            self.rect_fireball_2.midbottom = self.coords_under
            self.rect_fireball_5.midbottom = self.coords_top

        if 6.3 >= self.timer >= 2.3:
            surface.blit(self.image_fireball_flipped, self.rect_fireball_6)
            self.rect_fireball_6.x -= 4
        if 6.7 >= self.timer >= 2.7:
            surface.blit(self.image_fireball, self.rect_fireball_3)
            self.rect_fireball_3.x += 4
        elif self.timer == 6.8:
            self.rect_fireball_3.midbottom = self.coords_under
            self.rect_fireball_6.midbottom = self.coords_top            
#cycle 2
        if 8.5 >= self.timer >= 4.5:
            surface.blit(self.image_fireball, self.rect_fireball_1)
            self.rect_fireball_1.x += 4
            surface.blit(self.image_fireball_flipped, self.rect_fireball_4)
            self.rect_fireball_4.x -= 4
        elif self.timer == 8.6:
            self.rect_fireball_1.midbottom = self.coords_under
            self.rect_fireball_4.midbottom = self.coords_top

        if 9.5 >= self.timer >= 5.5:
            surface.blit(self.image_fireball_flipped, self.rect_fireball_5)
            self.rect_fireball_5.x -= 4
        if 9.8 >= self.timer >= 5.8:
            surface.blit(self.image_fireball, self.rect_fireball_2)
            self.rect_fireball_2.x += 4
        elif self.timer == 9.9:
            self.rect_fireball_2.midbottom = self.coords_under
            self.rect_fireball_5.midbottom = self.coords_top

        if 10.9 >= self.timer >= 6.9:
            surface.blit(self.image_fireball_flipped, self.rect_fireball_6)
            self.rect_fireball_6.x -= 4
        if 11 >= self.timer >= 7:
            surface.blit(self.image_fireball, self.rect_fireball_3)
            self.rect_fireball_3.x += 4
        elif self.timer == 11.1:
            self.rect_fireball_3.midbottom = self.coords_under
            self.rect_fireball_6.midbottom = self.coords_top

#cycle 3 (last)
        if 12.7 >= self.timer >= 8.7:
            surface.blit(self.image_fireball, self.rect_fireball_1)
            self.rect_fireball_1.x += 4
            surface.blit(self.image_fireball_flipped, self.rect_fireball_4)
            self.rect_fireball_4.x -= 4
        elif self.timer == 12.8:
            self.rect_fireball_1.midbottom = self.coords_untouched
            self.rect_fireball_4.midbottom = self.coords_untouched

        if 14 >= self.timer >= 10:
            surface.blit(self.image_fireball_flipped, self.rect_fireball_5)
            self.rect_fireball_5.x -= 4
        if 14.3 >= self.timer >= 10.3:
            surface.blit(self.image_fireball, self.rect_fireball_2)
            self.rect_fireball_2.x += 4
        elif self.timer == 14.4:
            self.rect_fireball_2.midbottom = self.coords_untouched
            self.rect_fireball_5.midbottom = self.coords_untouched

        if 15.2 >= self.timer >= 11.2:
            surface.blit(self.image_fireball_flipped, self.rect_fireball_6)
            self.rect_fireball_6.x -= 4
        if 15.5 >= self.timer >= 11.5:
            surface.blit(self.image_fireball, self.rect_fireball_3)
            self.rect_fireball_3.x += 4
        elif self.timer == 15.6:
            self.rect_fireball_3.midbottom = self.coords_untouched
            self.rect_fireball_6.midbottom = self.coords_untouched

        #flame pillar and fire-ground
#fireground
        if 16> self.timer >= 15.4:
            if self.activate_2 == False:
                self.activate_2 = True
                self.rect_fireground.midbottom = (380,405)
            else:
                surface.blit(self.image_fireground, self.rect_fireground)
        elif self.timer == 16.1:
            self.activate_2 = False
            self.rect_fireground.midbottom = self.coords_untouched
#pillar      
        if 16> self.timer >= 15.4:
            if self.activate_1 == False:
                self.activate_1 = True
                self.rect_firepillar_1.midbottom = (150,500)
                self.rect_firepillar_2.midbottom = (630,500)
            else:
                surface.blit(self.image_firepillar, self.rect_firepillar_1)
                surface.blit(self.image_firepillar, self.rect_firepillar_2)
        elif self.timer == 16.1:
            self.activate_1 = False
            self.rect_firepillar_1.midbottom = self.coords_untouched
            self.rect_firepillar_2.midbottom = self.coords_untouched
            
    def setRect_fireball(self, num):
        var_name = 'rect_fireball_'+str(num)
        self.rect = getattr(self, var_name)

    def setRect_firepillar(self, num):
        var_name = 'rect_firepillar_'+str(num)
        self.rect = getattr(self, var_name)

    def setRect_fireground(self):
        var_name = 'rect_fireground'
        self.rect = getattr(self, var_name)

    def update(self, screen, start_time):
        self.animation()
        self.timingObstacles(start_time)
        self.queue(screen)


