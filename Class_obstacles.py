import pygame

class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        #variable
        self.fireballCostume_Index = 0
        self.animationSpeed_1 = 0.3
        self.firepillarCostume_Index = 0
        self.animationSpeed_2 = 0.2
        self.firegroundCostume_Index = 0
        self.animationSpeed_3 = 0.75
        self.firedropCostume_Index_Right = 0
        self.animationSpeed_4 = 1
        self.firedropCostume_Index_Left = 0
        self.animationSpeed_5 = 1
        self.coords_under = (5,400)
        self.coords_top = (800,355)
        self.coords_MeteorR = (680, 330)
        self.coords_MeteorL = (100,330)
        self.coords_untouched = (0,0)
        self.activate_1 = False
        self.activate_2 = False
        self.activate_3 = False
        self.activate_4 = False
        self.activate_5 = False
        self.activate_6 = False
        self.alpha = 400
        self.runthis = False
        self.coords_MeteorR_2 = (750, 120)
        self.coords_MeteorL_2 = (0,100)

        #setup images
        self.temporary_fireball = pygame.image.load('fires/fireball/Fireball_1.png').convert_alpha()
        self.temporary_fireball = pygame.transform.scale(self.temporary_fireball, (32, 32))
        self.temporary_firepillar = pygame.image.load('fires/firepillar/pillar_1.png').convert_alpha()
        self.temporary_firepillar = pygame.transform.scale(self.temporary_firepillar, (120, 500))
        self.temporary_fireground = pygame.image.load('fires/flameFloor/fireGround_1.png').convert_alpha()
        self.temporary_fireground = pygame.transform.scale(self.temporary_fireground, (750,60))
        self.temporary_firedrop = pygame.image.load('fires/firedrop/firedrop_1.png').convert_alpha()
        self.temporary_firedrop = pygame.transform.scale(self.temporary_firedrop, (150,528))
        self.temporary_firedrop = pygame.transform.rotate(self.temporary_firedrop, -60)
        self.temporary_firedrop_flipped = pygame.transform.flip(self.temporary_firedrop, True, False)

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
        self.rect_firedrop_right = self.temporary_firedrop.get_rect(midbottom = self.coords_MeteorR)
        self.rect_firedrop_left = self.temporary_firedrop_flipped.get_rect(midbottom = self.coords_MeteorL)

        self.meteor_right = pygame.Rect(0, 0, 70, 70)
        self.meteor_right.midbottom = (self.coords_MeteorR_2)

        self.meteor_left = pygame.Rect(0, 0, 70, 70)
        self.meteor_left.midbottom = (self.coords_MeteorL_2)

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
            self.temporary_firepillar = pygame.transform.scale(self.temporary_firepillar, (120, 500))
            self.firepillar.append(self.temporary_firepillar)
        
        self.fireground = []
        for i in range(1, 10):
            self.filename = 'fires/flameFloor/fireGround_' + str(i) + '.png'
            self.temporary_fireground = pygame.image.load(self.filename).convert_alpha()
            self.temporary_fireground = pygame.transform.scale(self.temporary_fireground, (750,60))
            self.fireground.append(self.temporary_fireground)

        self.firedrop = []
        self.firedrop_flipped = []
        for i in range(1, 31):
            self.filename = 'fires/firedrop/firedrop_' + str(i) + '.png'
            self.temporary_firedrop = pygame.image.load(self.filename).convert_alpha()
            self.temporary_firedrop = pygame.transform.scale(self.temporary_firedrop, (150,528))
            self.temporary_firedrop = pygame.transform.rotate(self.temporary_firedrop, -60)
            self.firedrop.append(self.temporary_firedrop)
            self.temporary_firedrop = pygame.transform.flip(self.temporary_firedrop, True, False)
            self.firedrop_flipped.append(self.temporary_firedrop)
    def animation(self):
        self.image_fireball = self.fireball[int(self.fireballCostume_Index)]
        self.image_fireball_flipped = pygame.transform.flip(self.image_fireball, True, False)

        if self.timer_precise <=16:
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
            self.firegroundCostume_Index += self.animationSpeed_3
            self.image_fireground.set_alpha(self.alpha)
            if self.firegroundCostume_Index >= 7.5:
                self.firegroundCostume_Index = 0

            if self.alpha < 0:
                pass
            else:
                self.alpha -= 40

        if self.activate_3 == True:
            self.image_firedrop = self.firedrop[int(self.firedropCostume_Index_Right)]
            self.firedropCostume_Index_Right += self.animationSpeed_4
            if self.firedropCostume_Index_Right >= 29:
                self.animationSpeed_4 = 0
            elif self.firedropCostume_Index_Right == 0:
                self.animationSpeed_4 = 1

        if self.activate_4 == True:
            self.image_firedrop_flipped = self.firedrop_flipped[int(self.firedropCostume_Index_Left)]
            self.firedropCostume_Index_Left += self.animationSpeed_5
            if self.firedropCostume_Index_Left >= 29:
                self.animationSpeed_5 = 0
            elif self.firedropCostume_Index_Left == 0:
                self.animationSpeed_5 = 1

    def timingObstacles(self, start_time):
        self.start_time = start_time
        self.timer_precise = float("%.4f" %((pygame.time.get_ticks()-self.start_time)/1000))
        self.timer = float("%.1f" %self.timer_precise)
        print(self.timer_precise)

    def queue(self, surface):
#PHASE 1: horizontal fire balls
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

#PHASE 2: flame pillar and fire-ground
        #fireground
        if 15.7> self.timer >= 15.4:
            if self.activate_2 == False:
                self.activate_2 = True
                self.rect_fireground.midbottom = (380,405)
            else:
                surface.blit(self.image_fireground, self.rect_fireground)
        elif self.timer == 15.8:
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
            
#PHASE 3: Meteor with beats
        #Right Meteor
        if 23 > self.timer >= 16.5: 
            if self.activate_3 == False:
                self.activate_3 = True
            else:
                surface.blit(self.image_firedrop, self.rect_firedrop_right)
                # pygame.draw.circle(surface, (255, 0, 0), self.meteor_right.center, 50) # show rectangle(red circle)
                self.rect_firedrop_right.x -= 0.87*25
                self.rect_firedrop_right.y += 0.5*25
                self.meteor_right.x -= 0.87*30
                self.meteor_right.y += 0.5*30
                if self.rect_firedrop_right.y >= 660:
                    self.rect_firedrop_right.midbottom = self.coords_MeteorR
                    self.firedropCostume_Index_Right = 0
                    self.meteor_right.midbottom = self.coords_MeteorR_2
    
        #Left Meteor
        if 23 > self.timer_precise >= 16.85: #16.85
            if self.activate_4 == False:
                self.activate_4 = True
            else:
                surface.blit(self.image_firedrop_flipped, self.rect_firedrop_left)
                # pygame.draw.circle(surface, (255, 0, 0), self.meteor_left.center, 50) # show rectangle(red circle)
                self.rect_firedrop_left.x += 0.87*25
                self.rect_firedrop_left.y += 0.5*25
                self.meteor_left.x += 0.87*30
                self.meteor_left.y += 0.5*30
                if self.rect_firedrop_left.y >= 660:
                    self.rect_firedrop_left.midbottom = self.coords_MeteorL
                    self.firedropCostume_Index_Left = 0
                    self.meteor_left.midbottom = self.coords_MeteorL_2

#PHASE 4: Spreading bullets
        #Right side 1
        if 25 > self.timer >= 23: #23
            if self.activate_5 == False:
                self.activate_5 = True
                self.rect_fireball_4.midbottom = (800, 100)
                self.rect_fireball_5.midbottom = (800, 100)
                self.rect_fireball_6.midbottom = (800, 100)
            surface.blit(self.image_fireball_flipped, self.rect_fireball_4)
            self.rect_fireball_4.x -= 4
            self.rect_fireball_4.y += 8
        if 25.2 > self.timer >= 23.2: 
            surface.blit(self.image_fireball_flipped, self.rect_fireball_5)
            self.rect_fireball_5.x -= 6
            self.rect_fireball_5.y += 8
        if 25.4 > self.timer >= 23.4: 
            surface.blit(self.image_fireball_flipped, self.rect_fireball_6)
            self.rect_fireball_6.x -= 10
            self.rect_fireball_6.y += 8
        if self.timer == 26:
            self.activate_5 = False
        #Left side 1
        if 27 > self.timer >= 25: #23
            if self.activate_6 == False:
                self.activate_6 = True
                self.rect_fireball_1.midbottom = (0, 100)
                self.rect_fireball_2.midbottom = (0, 100)
                self.rect_fireball_3.midbottom = (0, 100)
            surface.blit(self.image_fireball, self.rect_fireball_1)
            self.rect_fireball_1.x += 4
            self.rect_fireball_1.y += 8
        if 27.2 > self.timer >= 25.2: 
            surface.blit(self.image_fireball, self.rect_fireball_2)
            self.rect_fireball_2.x += 6
            self.rect_fireball_2.y += 8
        if 27.4 > self.timer >= 25.4: 
            surface.blit(self.image_fireball, self.rect_fireball_3)
            self.rect_fireball_3.x += 10
            self.rect_fireball_3.y += 8
        if self.timer == 28:
            self.activate_6 = False
        #Right side 2
        if 29 > self.timer >= 27: #23
            if self.activate_5 == False:
                self.activate_5 = True
                self.rect_fireball_4.midbottom = (800, 100)
                self.rect_fireball_5.midbottom = (800, 100)
                self.rect_fireball_6.midbottom = (800, 100)
            surface.blit(self.image_fireball_flipped, self.rect_fireball_4)
            self.rect_fireball_4.x -= 4
            self.rect_fireball_4.y += 8
        if 29.2 > self.timer >= 27.2: 
            surface.blit(self.image_fireball_flipped, self.rect_fireball_5)
            self.rect_fireball_5.x -= 6
            self.rect_fireball_5.y += 8
        if 29.4 > self.timer >= 27.4: 
            surface.blit(self.image_fireball_flipped, self.rect_fireball_6)
            self.rect_fireball_6.x -= 10
            self.rect_fireball_6.y += 8
        #Left side 2
        if 31 > self.timer >= 29: #23
            if self.activate_6 == False:
                self.activate_6 = True
                self.rect_fireball_1.midbottom = (0, 100)
                self.rect_fireball_2.midbottom = (0, 100)
                self.rect_fireball_3.midbottom = (0, 100)
            surface.blit(self.image_fireball, self.rect_fireball_1)
            self.rect_fireball_1.x += 4
            self.rect_fireball_1.y += 8
        if 31.2 > self.timer >= 29.2: 
            surface.blit(self.image_fireball, self.rect_fireball_2)
            self.rect_fireball_2.x += 6
            self.rect_fireball_2.y += 8
        if 31.4 > self.timer >= 29.4: 
            surface.blit(self.image_fireball, self.rect_fireball_3)
            self.rect_fireball_3.x += 10
            self.rect_fireball_3.y += 8

    def setRect_fireball(self, num):
        var_name = 'rect_fireball_'+str(num)
        self.rect = getattr(self, var_name)

    def setRect_firepillar(self, num):
        var_name = 'rect_firepillar_'+str(num)
        self.rect = getattr(self, var_name)

    def setRect_fireground(self):
        var_name = 'rect_fireground'
        self.rect = getattr(self, var_name)

    def setRect_firedrop(self, num):
        if num == 1:
            var_name = 'meteor_right'
            self.rect = getattr(self, var_name)
        elif num == 2:
            var_name = 'meteor_left'
            self.rect = getattr(self, var_name)

    def update(self, screen, start_time):
        self.timingObstacles(start_time)
        self.animation()
        self.queue(screen)


