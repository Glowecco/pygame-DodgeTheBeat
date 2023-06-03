import pygame
import random

class Obstacle(pygame.sprite.Sprite):
    timer = 0
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
        self.firepopCostume_Index = 0
        self.animationSpeed_6 = 0.25
        self.flamethrowCostume_Index = 0
        self.animationSpeed_7 = 0.4
        self.meteorCostume_Index = 0
        self.animationSpeed_8 = 0.4
        self.flamefallCostume_Index1 = 0
        self.animationSpeed_9 = 0.7
        self.flamefallCostume_Index2 = 0
        self.animationSpeed_10 = 0.7
        self.flamefallCostume_Index3 = 0
        self.animationSpeed_11 = 0.7
        self.flamefallCostume_Index4 = 0
        self.animationSpeed_12 = 0.7
        self.coords_under = (5,400)
        self.coords_top = (800,355)
        self.coords_DropR = (680, 330)
        self.coords_DropL = (100,330)
        self.coords_DropR_2 = (750, 120)
        self.coords_DropL_2 = (0,100)
        self.y_coords_firepop = 354
        self.coords_untouched = (0,0)
        self.coords_flamethrow = (360,360)
        self.activate_pillar = False
        self.activate_fireground = False
        self.activate_firedrop = False
        self.activate_firedropFlipped = False
        self.activate_fireballA = False
        self.activate_fireballB = False
        self.activate_firepop = False
        self.activate_flamethrow = False
        self.activate_meteor = False
        self.activate_meteorhit = False
        self.activate_firepop2 = False
        self.activate_flamefall1 = False
        self.activate_flamefall2 = False
        self.activate_flamefall3 = False
        self.activate_flamefall4 = False
        self.alpha = 400
        self.firepop_relocate = True

        #setup images
        self.temporary_fireball = pygame.image.load('images_obstacles/fireball/Fireball_1.png').convert_alpha()
        self.temporary_fireball = pygame.transform.scale(self.temporary_fireball, (32, 32))
        self.temporary_firepillar = pygame.image.load('images_obstacles/firepillar/pillar_1.png').convert_alpha()
        self.temporary_firepillar = pygame.transform.scale(self.temporary_firepillar, (120, 500))
        self.temporary_fireground = pygame.image.load('images_obstacles/flameFloor/fireGround_1.png').convert_alpha()
        self.temporary_fireground = pygame.transform.scale(self.temporary_fireground, (750,60))
        self.temporary_firedrop = pygame.image.load('images_obstacles/firedrop/firedrop_1.png').convert_alpha()
        self.temporary_firedrop = pygame.transform.scale(self.temporary_firedrop, (150,528))
        self.temporary_firedrop = pygame.transform.rotate(self.temporary_firedrop, -60)
        self.temporary_firedrop_flipped = pygame.transform.flip(self.temporary_firedrop, True, False)
        self.temporary_firepop = pygame.image.load('images_obstacles/firepop/firepop_2.png').convert_alpha()
        self.temporary_firepop = pygame.transform.scale(self.temporary_firepop, (64, 48))
        self.temporary_flamethrow = pygame.image.load('images_obstacles/incendiary/flameThrow_6.png').convert_alpha()
        self.temporary_flamethrow = pygame.transform.scale(self.temporary_flamethrow, (780, 120))
        self.temporary_meteor = pygame.image.load('images_obstacles/meteor/meteor_3.png').convert_alpha()
        self.temporary_meteor = pygame.transform.scale(self.temporary_flamethrow, (32, 32))
        self.temporary_flamefall = pygame.image.load('images_obstacles/firedrop/firedrop_1.png').convert_alpha()
        self.temporary_flamefall = pygame.transform.scale(self.temporary_flamefall, (150,528))
        self.hint = pygame.image.load('images_obstacles/hint.png').convert_alpha()
        self.hint = pygame.transform.scale(self.hint, (500,400))

        #setup rects
        self.rect_dummy = self.temporary_fireball.get_rect(midbottom = self.coords_untouched)
        self.rect_fireball_1 = self.temporary_fireball.get_rect(midbottom = self.coords_under)
        self.rect_fireball_2 = self.temporary_fireball.get_rect(midbottom = self.coords_under)
        self.rect_fireball_3 = self.temporary_fireball.get_rect(midbottom = self.coords_under)
        self.rect_fireball_4 = self.temporary_fireball.get_rect(midbottom = self.coords_top)
        self.rect_fireball_5 = self.temporary_fireball.get_rect(midbottom = self.coords_top)
        self.rect_fireball_6 = self.temporary_fireball.get_rect(midbottom = self.coords_top)
        self.rect_firepillar_1 = self.temporary_firepillar.get_rect(midbottom = self.coords_untouched)
        self.rect_firepillar_2 = self.temporary_firepillar.get_rect(midbottom = self.coords_untouched)
        self.rect_fireground = self.temporary_fireground.get_rect(midbottom = self.coords_untouched)
        self.rect_firedrop_right = self.temporary_firedrop.get_rect(midbottom = self.coords_DropR)
        self.rect_firedrop_left = self.temporary_firedrop_flipped.get_rect(midbottom = self.coords_DropL)
        self.bigdrop_r = pygame.Rect(0, 0, 70, 70)
        self.bigdrop_r.midbottom = (self.coords_DropR_2)
        self.bigdrop_l = pygame.Rect(0, 0, 70, 70)
        self.bigdrop_l.midbottom = (self.coords_DropL_2)
        self.rect_firepop = self.temporary_firepop.get_rect(midbottom = self.coords_untouched)
        self.rect_flamethrow = self.temporary_flamethrow.get_rect(midbottom = self.coords_untouched)
        self.rect_flamethrow_hitbox = pygame.Rect(0, 0, 570, 40)
        self.rect_flamethrow_hitbox.midbottom = self.coords_untouched
        self.rect_meteor1 = self.temporary_meteor.get_rect(midbottom = self.coords_untouched)
        self.rect_meteor2 = self.temporary_meteor.get_rect(midbottom = self.coords_untouched)
        self.rect_meteor3 = self.temporary_meteor.get_rect(midbottom = self.coords_untouched)
        self.rect_meteor4 = self.temporary_meteor.get_rect(midbottom = self.coords_untouched)
        self.rect_meteor5 = self.temporary_meteor.get_rect(midbottom = self.coords_untouched)
        self.rect_meteor6 = self.temporary_meteor.get_rect(midbottom = self.coords_untouched)
        self.rect_meteor7 = self.temporary_meteor.get_rect(midbottom = self.coords_untouched)
        self.rect_meteor8 = self.temporary_meteor.get_rect(midbottom = self.coords_untouched)
        self.rect_meteor9 = self.temporary_meteor.get_rect(midbottom = self.coords_untouched)
        self.rect_meteor10 = self.temporary_meteor.get_rect(midbottom = self.coords_untouched)
        self.rect_meteor11 = self.temporary_meteor.get_rect(midbottom = self.coords_untouched)
        self.rect_meteor12 = self.temporary_meteor.get_rect(midbottom = self.coords_untouched)
        self.rect_flamefall1 = self.temporary_firedrop.get_rect(midbottom = (900,-270))
        self.rect_flamefall2 = self.temporary_firedrop.get_rect(midbottom = (780,-270))
        self.rect_flamefall3 = self.temporary_firedrop.get_rect(midbottom = (660,-270))
        self.rect_flamefall4 = self.temporary_firedrop.get_rect(midbottom = (540,-270))
        self.rect_flamefall_hitbox1 = pygame.Rect(0, 0, 70, 200)
        self.rect_flamefall_hitbox2 = pygame.Rect(0, 0, 70, 200)
        self.rect_flamefall_hitbox3 = pygame.Rect(0, 0, 70, 200)
        self.rect_flamefall_hitbox4 = pygame.Rect(0, 0, 70, 200)

        #load animation cuts
        self.fireball = []
        for i in range(1, 9):
            self.filename = 'images_obstacles/fireball/Fireball_' + str(i) + '.png'
            self.temporary_fireball = pygame.image.load(self.filename).convert_alpha()
            self.temporary_fireball = pygame.transform.scale(self.temporary_fireball, (32, 32))
            self.fireball.append(self.temporary_fireball)

        self.firepillar = []
        for i in range(1, 11):
            self.filename = 'images_obstacles/firepillar/pillar_' + str(i) + '.png'
            self.temporary_firepillar = pygame.image.load(self.filename).convert_alpha()
            self.temporary_firepillar = pygame.transform.scale(self.temporary_firepillar, (120, 500))
            self.firepillar.append(self.temporary_firepillar)
        
        self.fireground = []
        for i in range(1, 10):
            self.filename = 'images_obstacles/flameFloor/fireGround_' + str(i) + '.png'
            self.temporary_fireground = pygame.image.load(self.filename).convert_alpha()
            self.temporary_fireground = pygame.transform.scale(self.temporary_fireground, (750,60))
            self.fireground.append(self.temporary_fireground)

        self.firedrop = []
        self.firedrop_flipped = []
        for i in range(1, 31):
            self.filename = 'images_obstacles/firedrop/firedrop_' + str(i) + '.png'
            self.temporary_firedrop = pygame.image.load(self.filename).convert_alpha()
            self.temporary_firedrop = pygame.transform.scale(self.temporary_firedrop, (150,528))
            self.temporary_firedrop = pygame.transform.rotate(self.temporary_firedrop, -60)
            self.firedrop.append(self.temporary_firedrop)
            self.temporary_firedrop = pygame.transform.flip(self.temporary_firedrop, True, False)
            self.firedrop_flipped.append(self.temporary_firedrop)

        self.firepop = []
        for i in range(1, 8):
            self.filename = 'images_obstacles/firepop/firepop_' + str(i) + '.png'
            self.temporary_firepop = pygame.image.load(self.filename).convert_alpha()
            self.temporary_firepop = pygame.transform.scale(self.temporary_firepop, (64, 48))
            self.firepop.append(self.temporary_firepop)

        self.flamethrow = []
        for i in range(1, 17):
            self.filename = 'images_obstacles/incendiary/flameThrow_' + str(i) + '.png'
            self.temporary_flamethrow = pygame.image.load(self.filename).convert_alpha()
            self.temporary_flamethrow = pygame.transform.scale(self.temporary_flamethrow, (780, 120))
            self.flamethrow.append(self.temporary_flamethrow)

        self.meteor = []
        for i in range(1, 12):
            self.filename = 'images_obstacles/meteor/meteor_' + str(i) + '.png'
            self.temporary_meteor = pygame.image.load(self.filename).convert_alpha()
            self.temporary_meteor = pygame.transform.scale(self.temporary_meteor, (32, 32))
            self.meteor.append(self.temporary_meteor)

        self.flamefall = []
        for i in range(1, 32):
            self.filename = 'images_obstacles/firedrop/firedrop_' + str(i) + '.png'
            self.temporary_flamefall = pygame.image.load(self.filename).convert_alpha()
            self.temporary_flamefall = pygame.transform.scale(self.temporary_flamefall, (150,2200))
            self.flamefall.append(self.temporary_flamefall)

    def animation(self):
        self.image_fireball = self.fireball[int(self.fireballCostume_Index)]
        self.image_fireball_flipped = pygame.transform.flip(self.image_fireball, True, False)

        if self.timer_precise <=16:
            self.fireballCostume_Index += self.animationSpeed_1
            if self.fireballCostume_Index >= 7.6:
                self.animationSpeed_1 = - 0.3
            elif self.fireballCostume_Index < 2.4:
                self.animationSpeed_1 = 0.3
        
        if self.activate_pillar == True:
            self.image_firepillar = self.firepillar[int(self.firepillarCostume_Index)]
            self.firepillarCostume_Index += self.animationSpeed_2
            self.animationSpeed_2 = 0.2
            if self.firepillarCostume_Index >= 9.6:
                self.animationSpeed_2 = 0
        
        if self.activate_fireground == True:
            self.image_fireground = self.fireground[int(self.firegroundCostume_Index)]
            self.firegroundCostume_Index += self.animationSpeed_3
            self.image_fireground.set_alpha(self.alpha)
            if self.firegroundCostume_Index >= 7.5:
                self.firegroundCostume_Index = 0
            if self.alpha < 0:
                pass
            else:
                self.alpha -= 40

        if self.activate_firedrop == True:
            self.image_firedrop = self.firedrop[int(self.firedropCostume_Index_Right)]
            self.firedropCostume_Index_Right += self.animationSpeed_4
            if self.firedropCostume_Index_Right >= 29:
                self.animationSpeed_4 = 0
            elif self.firedropCostume_Index_Right == 0:
                self.animationSpeed_4 = 1

        if self.activate_firedropFlipped == True:
            self.image_firedrop_flipped = self.firedrop_flipped[int(self.firedropCostume_Index_Left)]
            self.firedropCostume_Index_Left += self.animationSpeed_5
            if self.firedropCostume_Index_Left >= 29:
                self.animationSpeed_5 = 0
            elif self.firedropCostume_Index_Left == 0:
                self.animationSpeed_5 = 1

        if self.activate_firepop == True:
            self.image_firepop = self.firepop[int(self.firepopCostume_Index)]
            self.firepopCostume_Index += self.animationSpeed_6
            if self.firepopCostume_Index >= 6:
                self.animationSpeed_6 = 0.024
                if self.firepop_relocate ==True:
                    self.rect_firepop.x = random.randint(40, 700)
                    self.firepop_relocate = False
                else:
                    if self.firepopCostume_Index >= 6.95:
                        self.activate_firepop = False
                        self.firepopCostume_Index = 0
                        self.animationSpeed_6 = 0.29 

        if self.activate_flamethrow == True:
            if self.timer <= 33:
                self.image_flamethrow = self.flamethrow[int(self.flamethrowCostume_Index)]
                self.flamethrowCostume_Index += self.animationSpeed_7
                if self.flamethrowCostume_Index >= 10:
                    self.flamethrowCostume_Index = 4
            else:
                self.image_flamethrow = self.flamethrow[int(self.flamethrowCostume_Index)]
                self.flamethrowCostume_Index -= self.animationSpeed_7
                if self.flamethrowCostume_Index <= 0.3:
                    self.animationSpeed_7 = 0
                    
        if self.activate_meteor == True:
            self.animationSpeed_8 = 0.4
            self.image_meteor = self.meteor[int(self.meteorCostume_Index)]
            self.meteorCostume_Index += self.animationSpeed_8
            if self.rect_meteor1.y >= 370:
                if self.meteorCostume_Index >= 10.6:
                    self.animationSpeed_8 = 0
                    self.activate_meteor = False
            else:
                if self.meteorCostume_Index >= 5.6:
                    self.meteorCostume_Index = 0 

        if self.activate_flamefall1 == True:
            self.image_flamefall1 = self.flamefall[int(self.flamefallCostume_Index1)]
            self.flamefallCostume_Index1 += self.animationSpeed_9
            if self.flamefallCostume_Index1 >= 30:
                self.animationSpeed_9 = 0
        if self.activate_flamefall2 == True:
            self.image_flamefall2 = self.flamefall[int(self.flamefallCostume_Index2)]
            self.flamefallCostume_Index2 += self.animationSpeed_10
            if self.flamefallCostume_Index2 >= 30:
                self.animationSpeed_10 = 0
        if self.activate_flamefall3 == True:
            self.image_flamefall3 = self.flamefall[int(self.flamefallCostume_Index3)]
            self.flamefallCostume_Index3 += self.animationSpeed_11
            if self.flamefallCostume_Index3 >= 30:
                self.animationSpeed_11 = 0
        if self.activate_flamefall4 == True:
            self.image_flamefall4 = self.flamefall[int(self.flamefallCostume_Index4)]
            self.flamefallCostume_Index4 += self.animationSpeed_12
            if self.flamefallCostume_Index4 >= 30:
                self.animationSpeed_12 = 0

    def timingObstacles(self, start_time):
        self.start_time = start_time
        self.timer_precise = float("%.4f" %((pygame.time.get_ticks()-self.start_time)/1000))
        self.timer = float("%.1f" %self.timer_precise)
        Obstacle.timer = self.timer
        if self.DEBUGGING_MODE == 1 or self.DEBUGGING_MODE == 3:
            pass
        else:
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
        if 15.55> self.timer_precise >= 15.4:
            if self.activate_fireground == False:
                self.activate_fireground = True
                self.rect_fireground.midbottom = (380,405)
            else:
                surface.blit(self.image_fireground, self.rect_fireground)
        elif self.timer_precise >= 15.56:
            self.activate_fireground = False
            self.rect_fireground.midbottom = self.coords_untouched
        #pillar      
        if 16> self.timer >= 15.4:
            if self.activate_pillar == False:
                self.activate_pillar = True
                self.firepillarCostume_Index = 0
                self.rect_firepillar_1.midbottom = (150,500)
                self.rect_firepillar_2.midbottom = (630,500)
            else:
                surface.blit(self.image_firepillar, self.rect_firepillar_1)
                surface.blit(self.image_firepillar, self.rect_firepillar_2)
        elif self.timer == 16.1:
            self.activate_pillar = False
            self.rect_firepillar_1.midbottom = self.coords_untouched
            self.rect_firepillar_2.midbottom = self.coords_untouched
            
#PHASE 3: Big drops with beats
        #Right drop
        if 23 > self.timer >= 16.5: 
            if self.activate_firedrop == False:
                self.activate_firedrop = True
            else:
                surface.blit(self.image_firedrop, self.rect_firedrop_right)
                if self.DEBUGGING_MODE == 3 or self.DEBUGGING_MODE == 4:
                    pygame.draw.circle(surface, (255, 0, 0), self.bigdrop_r.center, 50)
                self.rect_firedrop_right.x -= 0.87*25
                self.rect_firedrop_right.y += 0.5*25
                self.bigdrop_r.x -= 0.87*30
                self.bigdrop_r.y += 0.5*30
                if self.rect_firedrop_right.y >= 660:
                    self.rect_firedrop_right.midbottom = self.coords_DropR
                    self.firedropCostume_Index_Right = 0
                    self.bigdrop_r.midbottom = self.coords_DropR_2
    
        #Left drop
        if 23 > self.timer_precise >= 16.85: #16.85
            if self.activate_firedropFlipped == False:
                self.activate_firedropFlipped = True
            else:
                surface.blit(self.image_firedrop_flipped, self.rect_firedrop_left)
                if self.DEBUGGING_MODE == 3 or self.DEBUGGING_MODE == 4:
                    pygame.draw.circle(surface, (255, 0, 0), self.bigdrop_l.center, 50)
                self.rect_firedrop_left.x += 0.87*25
                self.rect_firedrop_left.y += 0.5*25
                self.bigdrop_l.x += 0.87*30
                self.bigdrop_l.y += 0.5*30
                if self.rect_firedrop_left.y >= 660:
                    self.rect_firedrop_left.midbottom = self.coords_DropL
                    self.firedropCostume_Index_Left = 0
                    self.bigdrop_l.midbottom = self.coords_DropL_2

#PHASE 4: Spreading bullets and Fire pops
        #activate fire pops
        if 44 > self.timer >= 22.7:
            if self.activate_firepop == False:
                self.rect_firepop.y = self.y_coords_firepop
                self.activate_firepop = True
                self.firepop_relocate = True
            else:
                surface.blit(self.image_firepop, self.rect_firepop)
        elif self.timer == 44.1:
            self.activate_firepop = False
            self.rect_firepop.midbottom = self.coords_untouched

        #Right side 1
        if 25 > self.timer >= 23: #23
            if self.activate_fireballA == False:
                self.activate_fireballA = True
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
            self.activate_fireballA = False
        #Left side 1
        if 27 > self.timer >= 25: #23
            if self.activate_fireballB == False:
                self.activate_fireballB = True
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
            self.activate_fireballB = False
        #Right side 2
        if 29 > self.timer >= 27: #23
            if self.activate_fireballA == False:
                self.activate_fireballA = True
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
        if self.timer == 30:
            self.activate_fireballA = False
        #Left side 2
        if 31 > self.timer >= 29: #23
            if self.activate_fireballB == False:
                self.activate_fireballB = True
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
        if self.timer == 32:
            self.activate_fireballB = False

#PHASE 5: flame pillar and incendiary
        #pillar
        if 31.4> self.timer >= 30.7:
            if self.activate_pillar == False:
                self.activate_pillar = True
                self.firepillarCostume_Index = 0
                self.rect_firepillar_1.midbottom = (150,500)
                self.rect_firepillar_2.midbottom = (630,500)
            else:
                surface.blit(self.image_firepillar, self.rect_firepillar_1)
                surface.blit(self.image_firepillar, self.rect_firepillar_2)
        elif self.timer == 32.5:
            self.activate_pillar = False
            self.rect_firepillar_1.midbottom = self.coords_untouched
            self.rect_firepillar_2.midbottom = self.coords_untouched
        #incendiary
        if 34> self.timer >= 30.7:
            if self.activate_flamethrow == False:
                self.activate_flamethrow = True
                self.rect_flamethrow.midbottom = self.coords_flamethrow
                self.rect_flamethrow_hitbox.midbottom = (270,320)
            else:
                surface.blit(self.image_flamethrow, self.rect_flamethrow)
                if self.DEBUGGING_MODE == 3 or self.DEBUGGING_MODE == 4:
                    pygame.draw.rect(surface, (0, 0, 255), self.rect_flamethrow_hitbox)
        elif self.timer == 34.1:
            self.rect_flamethrow.midbottom = self.coords_untouched
        
        if self.timer == 33.2:
            self.rect_flamethrow_hitbox.midbottom = self.coords_untouched

#PHASE 6: horizontal fire balls
        benchmark_phase6=28
        #cycle 1
        if 4+benchmark_phase6 >= self.timer >= benchmark_phase6:
            surface.blit(self.image_fireball, self.rect_fireball_1)
            self.rect_fireball_1.x += 4
            surface.blit(self.image_fireball_flipped, self.rect_fireball_4)
            self.rect_fireball_4.x -= 4
        elif self.timer == 4.1+benchmark_phase6:
            self.rect_fireball_1.midbottom = self.coords_under
            self.rect_fireball_4.midbottom = self.coords_top

        if 5+benchmark_phase6 >= self.timer >= 1+benchmark_phase6:
            surface.blit(self.image_fireball, self.rect_fireball_2)
            self.rect_fireball_2.x += 4
        if 5.3+benchmark_phase6 >= self.timer >= 1.3+benchmark_phase6:
            surface.blit(self.image_fireball_flipped, self.rect_fireball_5)
            self.rect_fireball_5.x -= 4
        elif self.timer == 5.4+benchmark_phase6:
            self.rect_fireball_2.midbottom = self.coords_under
            self.rect_fireball_5.midbottom = self.coords_top

        if 6.3+benchmark_phase6 >= self.timer >= 2.3+benchmark_phase6:
            surface.blit(self.image_fireball_flipped, self.rect_fireball_6)
            self.rect_fireball_6.x -= 4
        if 6.7+benchmark_phase6 >= self.timer >= 2.7+benchmark_phase6:
            surface.blit(self.image_fireball, self.rect_fireball_3)
            self.rect_fireball_3.x += 4
        elif self.timer == 6.8+benchmark_phase6:
            self.rect_fireball_3.midbottom = self.coords_under
            self.rect_fireball_6.midbottom = self.coords_top            
        #cycle 2
        if 8.5+benchmark_phase6 >= self.timer >= 4.5+benchmark_phase6:
            surface.blit(self.image_fireball, self.rect_fireball_1)
            self.rect_fireball_1.x += 4
            surface.blit(self.image_fireball_flipped, self.rect_fireball_4)
            self.rect_fireball_4.x -= 4
        elif self.timer == 8.6+benchmark_phase6:
            self.rect_fireball_1.midbottom = self.coords_under
            self.rect_fireball_4.midbottom = self.coords_top

        if 9.5+benchmark_phase6 >= self.timer >= 5.5+benchmark_phase6:
            surface.blit(self.image_fireball_flipped, self.rect_fireball_5)
            self.rect_fireball_5.x -= 4
        if 9.8+benchmark_phase6 >= self.timer >= 5.8+benchmark_phase6:
            surface.blit(self.image_fireball, self.rect_fireball_2)
            self.rect_fireball_2.x += 4
        elif self.timer == 9.9+benchmark_phase6:
            self.rect_fireball_2.midbottom = self.coords_under
            self.rect_fireball_5.midbottom = self.coords_top

        if 10.9+benchmark_phase6 >= self.timer >= 6.9+benchmark_phase6:
            surface.blit(self.image_fireball_flipped, self.rect_fireball_6)
            self.rect_fireball_6.x -= 4
        if 11+benchmark_phase6 >= self.timer >= 7+benchmark_phase6:
            surface.blit(self.image_fireball, self.rect_fireball_3)
            self.rect_fireball_3.x += 4
        elif self.timer == 11.1+benchmark_phase6:
            self.rect_fireball_3.midbottom = self.coords_under
            self.rect_fireball_6.midbottom = self.coords_top
        #cycle 3 (last)
        if 12.7+benchmark_phase6 >= self.timer >= 8.7+benchmark_phase6:
            surface.blit(self.image_fireball, self.rect_fireball_1)
            self.rect_fireball_1.x += 4
            surface.blit(self.image_fireball_flipped, self.rect_fireball_4)
            self.rect_fireball_4.x -= 4
        elif self.timer == 12.8+benchmark_phase6:
            self.rect_fireball_1.midbottom = self.coords_untouched
            self.rect_fireball_4.midbottom = self.coords_untouched

        if 14+benchmark_phase6 >= self.timer >= 10+benchmark_phase6:
            surface.blit(self.image_fireball_flipped, self.rect_fireball_5)
            self.rect_fireball_5.x -= 4
        if 14.3+benchmark_phase6 >= self.timer >= 10.3+benchmark_phase6:
            surface.blit(self.image_fireball, self.rect_fireball_2)
            self.rect_fireball_2.x += 4
        elif self.timer == 14.4+benchmark_phase6:
            self.rect_fireball_2.midbottom = self.coords_untouched
            self.rect_fireball_5.midbottom = self.coords_untouched

        if 15.2+benchmark_phase6 >= self.timer >= 11.2+benchmark_phase6:
            surface.blit(self.image_fireball_flipped, self.rect_fireball_6)
            self.rect_fireball_6.x -= 4
        if 15.5+benchmark_phase6 >= self.timer >= 11.5+benchmark_phase6:
            surface.blit(self.image_fireball, self.rect_fireball_3)
            self.rect_fireball_3.x += 4
        elif self.timer == 15.6+benchmark_phase6:
            self.rect_fireball_3.midbottom = self.coords_untouched
            self.rect_fireball_6.midbottom = self.coords_untouched

#PHASE 7: meteor rain, spreading bullets, and fire pops
        #meteor
        meteor_speed = 4
        if 54.5 > self.timer >= 45:#
            if self.activate_meteor == False:
                rand_coords = set()
                self.exclude = random.randint(-300, 270)
                while len(rand_coords) < 12:
                    random_number = random.randrange(-310, 331, 10)
                    if self.exclude <= random_number <= self.exclude + 150:
                        continue
                    rand_coords.add(random_number)
                rand_coords = list(rand_coords)
                self.rect_meteor1.midbottom = (rand_coords[0],0)
                self.rect_meteor2.midbottom = (rand_coords[1],0)
                self.rect_meteor3.midbottom = (rand_coords[2],0)
                self.rect_meteor4.midbottom = (rand_coords[3],0)
                self.rect_meteor5.midbottom = (rand_coords[4],0)
                self.rect_meteor6.midbottom = (rand_coords[5],0)
                self.rect_meteor7.midbottom = (rand_coords[6],0)
                self.rect_meteor8.midbottom = (rand_coords[7],0)
                self.rect_meteor9.midbottom = (rand_coords[8],0)
                self.rect_meteor10.midbottom = (rand_coords[9],0)
                self.rect_meteor11.midbottom = (rand_coords[10],0)
                self.rect_meteor12.midbottom = (rand_coords[11],0)
                self.meteorCostume_Index = 4
                self.activate_meteor = True
            else:
                surface.blit(self.image_meteor, self.rect_meteor1)
                surface.blit(self.image_meteor, self.rect_meteor2)
                surface.blit(self.image_meteor, self.rect_meteor3)
                surface.blit(self.image_meteor, self.rect_meteor4)
                surface.blit(self.image_meteor, self.rect_meteor5)
                surface.blit(self.image_meteor, self.rect_meteor6)
                surface.blit(self.image_meteor, self.rect_meteor7)
                surface.blit(self.image_meteor, self.rect_meteor8)
                surface.blit(self.image_meteor, self.rect_meteor9)
                surface.blit(self.image_meteor, self.rect_meteor10)
                surface.blit(self.image_meteor, self.rect_meteor11)
                surface.blit(self.image_meteor, self.rect_meteor12)
                if self.rect_meteor1.y >= 370:
                    pass
                else:
                    self.rect_meteor1.x += meteor_speed
                    self.rect_meteor1.y += meteor_speed
                    self.rect_meteor2.x += meteor_speed
                    self.rect_meteor2.y += meteor_speed 
                    self.rect_meteor3.x += meteor_speed
                    self.rect_meteor3.y += meteor_speed   
                    self.rect_meteor4.x += meteor_speed
                    self.rect_meteor4.y += meteor_speed 
                    self.rect_meteor5.x += meteor_speed
                    self.rect_meteor5.y += meteor_speed 
                    self.rect_meteor6.x += meteor_speed
                    self.rect_meteor6.y += meteor_speed 
                    self.rect_meteor7.x += meteor_speed
                    self.rect_meteor7.y += meteor_speed 
                    self.rect_meteor8.x += meteor_speed
                    self.rect_meteor8.y += meteor_speed 
                    self.rect_meteor9.x += meteor_speed
                    self.rect_meteor9.y += meteor_speed 
                    self.rect_meteor10.x += meteor_speed
                    self.rect_meteor10.y += meteor_speed
                    self.rect_meteor11.x += meteor_speed
                    self.rect_meteor11.y += meteor_speed
                    self.rect_meteor12.x += meteor_speed
                    self.rect_meteor12.y += meteor_speed 
        elif self.timer >= 54.5:
            self.rect_meteor1.midbottom = (self.coords_untouched)
            self.rect_meteor2.midbottom = (self.coords_untouched)
            self.rect_meteor3.midbottom = (self.coords_untouched)
            self.rect_meteor4.midbottom = (self.coords_untouched)
            self.rect_meteor5.midbottom = (self.coords_untouched)
            self.rect_meteor6.midbottom = (self.coords_untouched)
            self.rect_meteor7.midbottom = (self.coords_untouched)
            self.rect_meteor8.midbottom = (self.coords_untouched)
            self.rect_meteor9.midbottom = (self.coords_untouched)
            self.rect_meteor10.midbottom = (self.coords_untouched)
            self.rect_meteor11.midbottom = (self.coords_untouched)
            self.rect_meteor12.midbottom = (self.coords_untouched)
        #Spreading bullets
        # #Right side 1
        if 46 > self.timer >= 44: #23
            if self.activate_fireballA == False:
                self.activate_fireballA = True
                self.rect_fireball_4.midbottom = (800, 100)
                self.rect_fireball_5.midbottom = (800, 100)
                self.rect_fireball_6.midbottom = (800, 100)
            surface.blit(self.image_fireball_flipped, self.rect_fireball_4)
            self.rect_fireball_4.x -= 4
            self.rect_fireball_4.y += 8
        if 46.2 > self.timer >= 44.2: 
            surface.blit(self.image_fireball_flipped, self.rect_fireball_5)
            self.rect_fireball_5.x -= 6
            self.rect_fireball_5.y += 8
        if 46.4 > self.timer >= 44.4: 
            surface.blit(self.image_fireball_flipped, self.rect_fireball_6)
            self.rect_fireball_6.x -= 10
            self.rect_fireball_6.y += 8
        if self.timer == 47:
            self.activate_fireballA = False
        # #Left side 1
        if 46 > self.timer >= 44: #23
            if self.activate_fireballB == False:
                self.activate_fireballB = True
                self.rect_fireball_1.midbottom = (0, 100)
                self.rect_fireball_2.midbottom = (0, 100)
                self.rect_fireball_3.midbottom = (0, 100)
            surface.blit(self.image_fireball, self.rect_fireball_1)
            self.rect_fireball_1.x += 4
            self.rect_fireball_1.y += 8
        if 46.2 > self.timer >= 44.2: 
            surface.blit(self.image_fireball, self.rect_fireball_2)
            self.rect_fireball_2.x += 6
            self.rect_fireball_2.y += 8
        if 46.4 > self.timer >= 44.4: 
            surface.blit(self.image_fireball, self.rect_fireball_3)
            self.rect_fireball_3.x += 10
            self.rect_fireball_3.y += 8
        if self.timer == 47:
            self.activate_fireballB = False
        #activate fire pops
        if 55 > self.timer >= 46:
            if self.activate_firepop == False:
                self.rect_firepop.y = self.y_coords_firepop
                self.activate_firepop = True
                self.firepop_relocate = True
            else:
                surface.blit(self.image_firepop, self.rect_firepop)
        elif self.timer == 55.1:
            self.rect_firepop.midbottom = self.coords_untouched

        if 56.9 > self.timer >= 56.3:
            surface.blit(self.hint, (280,2))

#PHASE 8: Flame fall (end)
        benchmark_phase8 = 56.5 
        #cycle 1 (right to left)
        if 1.9+benchmark_phase8 > self.timer >= 1+benchmark_phase8:
            if self.activate_flamefall1 == False:
                self.rect_flamefall_hitbox1.midbottom = (710,100)
                self.animationSpeed_9 = 0.7
                self.flamefallCostume_Index1 = 0
                self.activate_flamefall1 = True
            else:
                if self.flamefallCostume_Index1 < 30:
                    surface.blit(self.image_flamefall1, self.rect_flamefall1)
                    if self.DEBUGGING_MODE == 3 or self.DEBUGGING_MODE == 4:
                        pygame.draw.rect(surface, (255,0,0), self.rect_flamefall_hitbox1)
                    self.rect_flamefall_hitbox1.y += 15
        elif self.timer == 2+benchmark_phase8:
            self.activate_flamefall1 = False
            self.rect_flamefall1.midbottom = (300,-270)

        if 2.1+benchmark_phase8 > self.timer >= 1.2+benchmark_phase8:
            if self.activate_flamefall2 == False:
                self.rect_flamefall_hitbox2.midbottom = (590,100)
                self.animationSpeed_10 = 0.7
                self.flamefallCostume_Index2 = 0
                self.activate_flamefall2 = True
            else:
                if self.flamefallCostume_Index2 < 30:
                    surface.blit(self.image_flamefall2, self.rect_flamefall2)
                    if self.DEBUGGING_MODE == 3 or self.DEBUGGING_MODE == 4:
                        pygame.draw.rect(surface, (255,0,0), self.rect_flamefall_hitbox2)
                    self.rect_flamefall_hitbox2.y += 15     
        elif self.timer == 2.2+benchmark_phase8:
            self.activate_flamefall2 = False
            self.rect_flamefall2.midbottom = (420,-270)

        if 2.3+benchmark_phase8 > self.timer >= 1.4+benchmark_phase8:
            if self.activate_flamefall3 == False:
                self.rect_flamefall_hitbox3.midbottom = (470,100)
                self.animationSpeed_11 = 0.7
                self.flamefallCostume_Index3 = 0
                self.activate_flamefall3 = True
            else:
                if self.flamefallCostume_Index3 < 30:
                    surface.blit(self.image_flamefall3, self.rect_flamefall3)  
                    if self.DEBUGGING_MODE == 3 or self.DEBUGGING_MODE == 4:
                        pygame.draw.rect(surface, (255,0,0), self.rect_flamefall_hitbox3)
                    self.rect_flamefall_hitbox3.y += 15 
        elif self.timer == 2.4+benchmark_phase8:
            self.activate_flamefall3 = False
            self.rect_flamefall3.midbottom = (540,-270)

        if 2.5+benchmark_phase8 > self.timer >= 1.6+benchmark_phase8:
            if self.activate_flamefall4 == False:
                self.rect_flamefall_hitbox4.midbottom = (350,100)
                self.animationSpeed_12 = 0.7
                self.flamefallCostume_Index4 = 0
                self.activate_flamefall4 = True
            else:
                if self.flamefallCostume_Index4 < 30:
                    surface.blit(self.image_flamefall4, self.rect_flamefall4)
                    if self.DEBUGGING_MODE == 3 or self.DEBUGGING_MODE == 4:
                        pygame.draw.rect(surface, (255,0,0), self.rect_flamefall_hitbox4)
                    self.rect_flamefall_hitbox4.y += 20
        elif self.timer == 2.6+benchmark_phase8:
            self.activate_flamefall4 = False
            self.rect_flamefall4.midbottom = (660,-270)

        #cycle 2 (left to right)
        if 2.8+benchmark_phase8 > self.timer >= 2+benchmark_phase8:
            if self.activate_flamefall1 == False:
                self.rect_flamefall_hitbox1.midbottom = (110,100)
                self.animationSpeed_9 = 0.7
                self.flamefallCostume_Index1 = 0
                self.activate_flamefall1 = True
            else:
                if self.flamefallCostume_Index1 < 30:
                    surface.blit(self.image_flamefall1, self.rect_flamefall1)
                    if self.DEBUGGING_MODE == 3 or self.DEBUGGING_MODE == 4:
                        pygame.draw.rect(surface, (255,0,0), self.rect_flamefall_hitbox1)
                    self.rect_flamefall_hitbox1.y += 15

        if 3.1+benchmark_phase8 > self.timer >= 2.2+benchmark_phase8:
            if self.activate_flamefall2 == False:
                self.rect_flamefall_hitbox2.midbottom = (230,100)
                self.animationSpeed_10 = 0.7
                self.flamefallCostume_Index2 = 0
                self.activate_flamefall2 = True
            else:
                if self.flamefallCostume_Index2 < 30:
                    surface.blit(self.image_flamefall2, self.rect_flamefall2)
                    if self.DEBUGGING_MODE == 3 or self.DEBUGGING_MODE == 4:   
                        pygame.draw.rect(surface, (255,0,0), self.rect_flamefall_hitbox2)
                    self.rect_flamefall_hitbox2.y += 15  

        if 3.3+benchmark_phase8 > self.timer >= 2.4+benchmark_phase8:
            if self.activate_flamefall3 == False:
                self.rect_flamefall_hitbox3.midbottom = (350,100)
                self.animationSpeed_11 = 0.7
                self.flamefallCostume_Index3 = 0
                self.activate_flamefall3 = True
            else:
                if self.flamefallCostume_Index3 < 30:
                    surface.blit(self.image_flamefall3, self.rect_flamefall3) 
                    if self.DEBUGGING_MODE == 3 or self.DEBUGGING_MODE == 4: 
                        pygame.draw.rect(surface, (255,0,0), self.rect_flamefall_hitbox3)
                    self.rect_flamefall_hitbox3.y += 15

        if 3.5+benchmark_phase8 > self.timer >= 2.6+benchmark_phase8:
            if self.activate_flamefall4 == False:
                self.rect_flamefall_hitbox4.midbottom = (470,100)
                self.animationSpeed_12 = 0.7
                self.flamefallCostume_Index4 = 0
                self.activate_flamefall4 = True
            else:
                if self.flamefallCostume_Index4 < 30:
                    surface.blit(self.image_flamefall4, self.rect_flamefall4)
                    if self.DEBUGGING_MODE == 3 or self.DEBUGGING_MODE == 4:
                        pygame.draw.rect(surface, (255,0,0), self.rect_flamefall_hitbox4)
                    self.rect_flamefall_hitbox4.y += 20
        
        if self.timer == 3.6+benchmark_phase8:
            self.rect_flamefall_hitbox1.midbottom = self.coords_untouched
            self.rect_flamefall_hitbox2.midbottom = self.coords_untouched
            self.rect_flamefall_hitbox3.midbottom = self.coords_untouched
            self.rect_flamefall_hitbox4.midbottom = self.coords_untouched

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
            var_name = 'bigdrop_r'
            self.rect = getattr(self, var_name)
        elif num == 2:
            var_name = 'bigdrop_l'
            self.rect = getattr(self, var_name)

    def setRect_firepop(self):
        var_name = 'rect_firepop'
        if self.firepopCostume_Index >= 3:
            self.rect = self.rect_dummy
        else:
            self.rect = getattr(self, var_name)
    
    def setRect_flamethrow(self):
        var_name = 'rect_flamethrow_hitbox'
        self.rect = getattr(self, var_name)

    def setRect_meteor(self, num):
        var_name = 'rect_meteor'+str(num)
        if self.meteorCostume_Index >= 6:
            self.rect = self.rect_dummy
        else:
            self.rect = getattr(self, var_name)

    def setRect_flamefall(self, num):
        var_name = 'rect_flamefall_hitbox'+str(num)
        self.rect = getattr(self, var_name)

    def update(self, screen, start_time, debug):
        self.DEBUGGING_MODE = debug
        self.timingObstacles(start_time)
        self.animation()
        self.queue(screen)


