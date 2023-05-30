import pygame
import random
from time import sleep
from Class_player import Player
from Class_obstacles import Obstacle

from sys import exit

def level1(screen, clock, font, textfont):
    # setup
    pygame.init()
    ingame_timer =0 
    blackscreen = pygame.Surface((800,500))
    blackscreen.fill((0, 0, 0))
    whitescreen = pygame.Surface((800,500))
    whitescreen.fill((255, 255, 255))
    background_xval3 = 0
    background_xval2 = 0
    background_xval1 = 0
    fast_bg = False
    flash = 255
    fade = 0
    death = False
    countdown = 0
    Alive = True
    shake_offset = (0, 0)
    screenshake = False
    screenshake_duration = 0
    fadeout = False
    dashicon_fade = 0
    death_cause = 8
    DEBUGGING_MODE = 1
    '''
    __DEBUGGING_MODE manual__ (input 1~4)
    ____________________________ ______________________________ _______________________ _______________                         
    1:|   dies on collision     |               x              |           x           |      x       |
    2:|   dies on collision     |       print collision        |     print time        |      x       |
    3:|        immortal         |       print collisions       |           x           | shows hitbox |
    4:|        immortal         |       print collisions       |     print time        | shows hitbox |

    set the mode to 1 for intended gameplay
    '''
    #constants
    bgm1 = pygame.mixer.Sound('mp3/bgm.mp3')
    bgm1.set_volume(0.4)
    start_time = pygame.time.get_ticks()
    shake_intensity = 15    

    #background surfaces
    background1 = pygame.image.load('images_background/sky1.png').convert_alpha()
    background1 = pygame.transform.scale(background1, (810, 510))
    background1_2 = pygame.image.load('images_background/sky1.png').convert_alpha()
    background1_2 = pygame.transform.scale(background1_2, (810, 510))
    background2 = pygame.image.load('images_background/sky2.png').convert_alpha()
    background2 = pygame.transform.scale(background2, (810, 510))
    background2_2 = pygame.image.load('images_background/sky2.png').convert_alpha()
    background2_2 = pygame.transform.scale(background2_2, (810, 510))
    background3 = pygame.image.load('images_background/sky3.png').convert_alpha()
    background3 = pygame.transform.scale(background3, (810, 510))
    background3_2 = pygame.image.load('images_background/sky3.png').convert_alpha()
    background3_2 = pygame.transform.scale(background3_2, (810, 510))
    platform = pygame.image.load('images_background/ground.png').convert_alpha()
    platform = pygame.transform.scale(platform, (700, 100))
    dashicon = pygame.image.load('images_icons/dash.png').convert_alpha()
    dashicon = pygame.transform.scale(dashicon, (20, 20))
    staricon = pygame.image.load('images_icons/star.png').convert_alpha()
    staricon = pygame.transform.scale(staricon, (75, 51))
    cornerbox = pygame.image.load('images_icons/corner.png').convert_alpha()
    cornerbox = pygame.transform.scale(cornerbox, (100, 40))

    #setup Player class
    player = pygame.sprite.GroupSingle()
    player.add(Player())
    player_sprite = player.sprite

    #setup Obstacle class
    obstacles = pygame.sprite.Group()
    obstacles.add(Obstacle())
    obstacles_sprite = obstacles.sprites()[0]

    #main loop
    bgm1.play()
    while True:
        time = int(pygame.time.get_ticks()/100)
        #check for quit 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                bgm1.stop()
                pygame.quit()
                exit()
        #Death sequence
            #on collision
        if Alive == False and death == False:
            countdown = time+1
            death = True
            screenshake = True
            #screenshake
        if screenshake == True:
            shake_offset = (random.randint(-shake_intensity, shake_intensity),random.randint(-shake_intensity, shake_intensity))
            screenshake_duration += 1
        else:
            shake_offset = (0, 0)
            #fadeout
        if countdown == time:        
            bgm1.stop()
            screenshake = False
            fadeout =True
        if fadeout == True:
            fade += 3
            if fade > 300:
                break

        #draw background(parallex background)
        if fast_bg == True:
            background_xval3 += 3
            background_xval2 += 5
            background_xval1 += 8
        screen.blit(background3, (shake_offset[0]-background_xval3, shake_offset[1]))
        screen.blit(background3_2, (shake_offset[0]-background_xval3+800, shake_offset[1]))
        screen.blit(background2, (shake_offset[0]-background_xval2, shake_offset[1]))
        screen.blit(background2_2, (shake_offset[0]-background_xval2+800, shake_offset[1]))
        screen.blit(background1, (shake_offset[0]-background_xval1, shake_offset[1]))
        screen.blit(background1_2, (shake_offset[0]-background_xval1+800, shake_offset[1]))
        screen.blit(platform, (50 + shake_offset[0], 400 + shake_offset[1]))
        if background_xval3 > 800:
            background_xval3 =0
        if background_xval2 > 800:
            background_xval2 =0
        if background_xval1 > 800:
            background_xval1 =0

        #update and draw obstacles
        obstacles.update(screen, start_time, DEBUGGING_MODE)
        if death == False:
            ingame_timer = Obstacle.timer

        #draw blackscreen
        blackscreen.set_alpha(fade)
        screen.blit(blackscreen, (0,0))
        
        #update and draw player
        if death == False:
            player.update()
        player.draw(screen)
        
        if ingame_timer >= 15.5 and flash > 0:
            fast_bg = True
            flash -= 10
            whitescreen.set_alpha(flash)
            screen.blit(whitescreen, (0,0))
        
        #draw icon and timer
        screen.blit(cornerbox, (710,0)) 
        screen.blit(staricon, (-20,-5))
        if Player.dash_on == True:
            dashicon.set_alpha(dashicon_fade)
            if dashicon_fade < 255:
                dashicon_fade += 20
            screen.blit(dashicon, (695,11))
        else:
            if dashicon_fade > 0:
                dashicon_fade -= 30
        text = font.render(str(ingame_timer), True, (0, 0, 0))
        screen.blit(text, (745, 10))

        #display
        pygame.display.update()

        #Collsion (Gameover)
        Alive = player_sprite.ALIVE
            #fireball
        for screenshake_duration in range(1,7):
            obstacles_sprite.setRect_fireball(screenshake_duration)
            collision = pygame.sprite.spritecollide(player_sprite, obstacles, False)
            if collision:
                if death_cause == 8:
                    death_cause = 1
                if DEBUGGING_MODE==1:
                    Alive = False
                elif DEBUGGING_MODE==2:
                    print('collided FIRE BALL '+str(screenshake_duration))
                    Alive = False
                elif DEBUGGING_MODE==3 or DEBUGGING_MODE==4:
                    print('collided FIRE BALL '+str(screenshake_duration))
                else:
                    pass
            #firepillar
        for screenshake_duration in range(1,3):
            obstacles_sprite.setRect_firepillar(screenshake_duration)
            collision = pygame.sprite.spritecollide(player_sprite, obstacles, False)
            if collision:
                if death_cause == 8:
                    death_cause = 2
                if DEBUGGING_MODE==1:
                    Alive = False
                elif DEBUGGING_MODE==2:
                    print('collided PILLAR '+str(screenshake_duration))
                    Alive = False
                elif DEBUGGING_MODE==3 or DEBUGGING_MODE==4:
                    print('collided PILLAR '+str(screenshake_duration))
                else:
                    pass
            #fireground
        obstacles_sprite.setRect_fireground()
        collision = pygame.sprite.spritecollide(player_sprite, obstacles, False)
        if collision:
            if death_cause == 8:
                death_cause = 3
            if DEBUGGING_MODE==1:
                Alive = False
            elif DEBUGGING_MODE==2:
                print('collided FIRE GROUND')
                Alive = False
            elif DEBUGGING_MODE==3 or DEBUGGING_MODE==4:
                print('collided FIRE GROUND')
            else:
                pass
            #firedrop
        for screenshake_duration in range(1,3):
            obstacles_sprite.setRect_firedrop(screenshake_duration)
            collision = pygame.sprite.spritecollide(player_sprite, obstacles, False)
            if collision:
                if death_cause == 8:
                    death_cause = 4
                if screenshake_duration == 1:
                    if DEBUGGING_MODE==1:
                        Alive = False
                    elif DEBUGGING_MODE==2:
                        print('collided RIGHT METEOR')
                        Alive = False
                    elif DEBUGGING_MODE==3 or DEBUGGING_MODE==4:
                        print('collided RIGHT METEOR')
                    else:
                        pass
                elif screenshake_duration == 2:
                    if DEBUGGING_MODE==1:
                        Alive = False
                    elif DEBUGGING_MODE==2:
                        print('collided LEFT METEOR')
                        Alive = False
                    elif DEBUGGING_MODE==3 or DEBUGGING_MODE==4:
                        print('collided LEFT METEOR')
                    else:
                        pass
            #firepop
        obstacles_sprite.setRect_firepop()
        collision = pygame.sprite.spritecollide(player_sprite, obstacles, False)
        if collision:
            if death_cause == 8:
                death_cause = 5
            if DEBUGGING_MODE==1:
                Alive = False
            elif DEBUGGING_MODE==2:
                print('collided FIRE POP')
                Alive = False
            elif DEBUGGING_MODE==3 or DEBUGGING_MODE==4:
                print('collided FIRE POP')
            else:
                pass
            #flamethrow
        obstacles_sprite.setRect_flamethrow()
        collision = pygame.sprite.spritecollide(player_sprite, obstacles, False)
        if collision:
            if death_cause == 8:
                death_cause = 6
            if DEBUGGING_MODE==1:
                Alive = False
            elif DEBUGGING_MODE==2:
                print('collided FLAMETHROW')
                Alive = False
            elif DEBUGGING_MODE==3 or DEBUGGING_MODE==4:
                print('collided FLAMETHROW')
            else:
                pass
            #meteor
        for screenshake_duration in range(1,13):
            obstacles_sprite.setRect_meteor(screenshake_duration)
            collision = pygame.sprite.spritecollide(player_sprite, obstacles, False)
            if collision:
                if death_cause == 8:
                    death_cause = 7
                if DEBUGGING_MODE==1:
                    Alive = False
                elif DEBUGGING_MODE==2:
                    print('collided METEOR '+str(screenshake_duration))
                    Alive = False
                elif DEBUGGING_MODE==3 or DEBUGGING_MODE==4:
                    print('collided METEOR '+str(screenshake_duration))
                else:
                    pass
            #flamefall
        for screenshake_duration in range(1,5):
            obstacles_sprite.setRect_flamefall(screenshake_duration)
            collision = pygame.sprite.spritecollide(player_sprite, obstacles, False)
            if collision:
                if death_cause == 8:
                    death_cause = 4
                if DEBUGGING_MODE==1:
                    Alive = False
                elif DEBUGGING_MODE==2:
                    print('collided FLAME FALL '+str(screenshake_duration))
                    Alive = False
                elif DEBUGGING_MODE==3 or DEBUGGING_MODE==4:
                    print('collided FLAME FALL '+str(screenshake_duration))
                else:
                    pass

        #fps
        clock.tick(60)

    
    #gameover
    #images setup
    end1 = pygame.image.load('images_ending/end1.jpg').convert_alpha()
    end1 = pygame.transform.scale(end1, (810, 510))
    end2 = pygame.image.load('images_ending/end2.jpg').convert_alpha()
    end2 = pygame.transform.scale(end2, (810, 510))
    end3 = pygame.image.load('images_ending/end3.jpg').convert_alpha()
    end3 = pygame.transform.scale(end3, (810, 510))
    end4 = pygame.image.load('images_ending/end4.jpg').convert_alpha()
    end4 = pygame.transform.scale(end4, (810, 510))
    end5 = pygame.image.load('images_ending/end5.jpg').convert_alpha()
    end5 = pygame.transform.scale(end5, (810, 510))
    backBut = pygame.image.load('images_buttons/backBut.png').convert_alpha()
    backBut = pygame.transform.scale(backBut, (240, 106))
    backBut_select = pygame.image.load('images_buttons/backBut2.png').convert_alpha()
    backBut_select = pygame.transform.scale(backBut_select, (240, 106))
    backBut_click = pygame.image.load('images_buttons/backBut3.png').convert_alpha()
    backBut_click = pygame.transform.scale(backBut_click, (240, 106))
    #rect
    rect_backBut = backBut.get_rect(midbottom = (550,515))

    coords = (570,240)
    backBut_show = "Black"
    gameover_screen = random.choice([end1, end2, end3, end4, end5])
    endscreen_alpha=0
    dialogue = random.randint(1,2)
    death_cause_images = []
    for i in range(1,9):
        if i == 1:
            width = 150
        elif i == 2:
            width = 140
        elif i == 3:
            width = 250
        elif i == 4:
            width = 72
        elif i == 5:
            width = 100
        elif i == 6:
            width = 300
        elif i == 7:
            width = 100
        elif i == 8:
            width = 100
        filename = 'images_ending/death_' + str(i) + '.png'
        temporary_img = pygame.image.load(filename).convert_alpha()
        aspect_ratio = temporary_img.get_width() / temporary_img.get_height()
        new_height = int(width/aspect_ratio)
        temporary_img = pygame.transform.scale(temporary_img, (width, new_height))
        death_cause_images.append(temporary_img)    
    if death_cause == 1:
        coords = (570,240)
    elif death_cause == 2:
        coords = (570,247)
    elif death_cause == 3:
        coords = (520,300)
    elif death_cause == 4:
        coords = (610,148)
    elif death_cause == 5:
        coords = (600,247)
    elif death_cause == 6:
        coords = (511,247)
    elif death_cause == 7:
        coords = (570,240)
    elif death_cause == 8:
        coords = (570,240)

    endscreen = True
    while endscreen:
        gameover_screen.set_alpha(endscreen_alpha)
        screen.blit(gameover_screen,(0,0))
        if endscreen_alpha < 255:
            endscreen_alpha += 20
        screen.blit(death_cause_images[death_cause-1], coords)

        if death_cause == 1:
            textfont = pygame.font.Font('font/The Brownies.otf', 25)
            text = textfont.render('Mr.fireball', True, (0, 0, 0))
            text = pygame.transform.rotate(text, 20)
            screen.blit(text, (570,247))
            if dialogue == 1:
                textfont = pygame.font.Font('font/The Brownies.otf', 50)
                text = textfont.render('Ain\'t got much to say..', True, (0, 0, 0))
                text = pygame.transform.rotate(text, -2)
                screen.blit(text, (80,220))
                text = textfont.render('Let\'s see.. yep nope', True, (0, 0, 0))
                text = pygame.transform.rotate(text, 5)
                screen.blit(text, (80,290))
                textfont = pygame.font.Font('font/The Brownies.otf', 25)
                text = textfont.render('how? what?', True, (0, 0, 0))
                screen.blit(text, (600,193))
            else:
                textfont = pygame.font.Font('font/The Brownies.otf', 50)
                text = textfont.render('Run AWAY from them, run!', True, (0, 0, 0))
                text = pygame.transform.rotate(text, -2)
                screen.blit(text, (80,220))
                text = textfont.render('do not feed the rabbit 2099', True, (0, 0, 0))
                text = pygame.transform.rotate(text, 5)
                screen.blit(text, (20,290))
                textfont = pygame.font.Font('font/The Brownies.otf', 20)
                text = textfont.render('are those fire pops bugging ya?', True, (0, 0, 0))
                screen.blit(text, (120,400))
                textfont = pygame.font.Font('font/The Brownies.otf', 25)
                text = textfont.render('Our Classic ol\'', True, (0, 0, 0))
                screen.blit(text, (600,193))
        elif death_cause == 2:
            textfont = pygame.font.Font('font/The Brownies.otf', 25)
            text = textfont.render('BADASSITUDE explosion', True, (0, 0, 0))
            text = pygame.transform.rotate(text, 6)
            screen.blit(text, (530,210))
            if dialogue == 1:
                textfont = pygame.font.Font('font/The Brownies.otf', 50)
                text = textfont.render('Its turly.. breaking my heart..', True, (0, 0, 0))
                text = pygame.transform.rotate(text, -2)
                screen.blit(text, (10,220))
                text = textfont.render('but say, cool explosion', True, (0, 0, 0))
                text = pygame.transform.rotate(text, 5)
                screen.blit(text, (80,290))
                textfont = pygame.font.Font('font/The Brownies.otf', 25)
                text = textfont.render('hint: stay away', True, (0, 0, 0))
                screen.blit(text, (600,390))
            else:
                textfont = pygame.font.Font('font/The Brownies.otf', 50)
                text = textfont.render('Up in flames!', True, (0, 0, 0))
                text = pygame.transform.rotate(text, -2)
                screen.blit(text, (50,220))
                text = textfont.render('Well don\'t just stand there', True, (0, 0, 0))
                text = pygame.transform.rotate(text, 5)
                screen.blit(text, (80,250))
                text = textfont.render('mmh.. toasty', True, (0, 0, 0))
                text = pygame.transform.rotate(text, -10)
                screen.blit(text, (20,350))
                textfont = pygame.font.Font('font/The Brownies.otf', 25)
                text = textfont.render('hint: dodge', True, (0, 0, 0))
                screen.blit(text, (600,390))
        elif death_cause == 3:
            textfont = pygame.font.Font('font/The Brownies.otf', 25)
            text = textfont.render('fire..  yep just flames!', True, (0, 0, 0))
            text = pygame.transform.rotate(text, 6)
            screen.blit(text, (530,230))
            text = textfont.render('you\'re right it comes with the explosion', True, (0, 0, 0))
            text = pygame.transform.rotate(text, -8)
            screen.blit(text, (180,170))
            if dialogue == 1:
                textfont = pygame.font.Font('font/The Brownies.otf', 50)
                text = textfont.render('Psst.. big hint:', True, (0, 0, 0))
                text = pygame.transform.rotate(text, -4)
                screen.blit(text, (10,220))
                text = textfont.render('jump', True, (0, 0, 0))
                text = pygame.transform.rotate(text, -4)
                screen.blit(text, (100,290))
                textfont = pygame.font.Font('font/The Brownies.otf', 25)
                text = textfont.render('toasty bbq..', True, (0, 0, 0))
                screen.blit(text, (600,390))
                text = textfont.render('Martha? is that', True, (0, 0, 0))
                text = pygame.transform.rotate(text, 4)
                screen.blit(text, (350,290))
                text = textfont.render('your garden on fire?', True, (0, 0, 0))
                text = pygame.transform.rotate(text, 4)
                screen.blit(text, (350,310))             
            else:
                textfont = pygame.font.Font('font/The Brownies.otf', 50)
                text = textfont.render('It gets easier, I promise', True, (0, 0, 0))
                text = pygame.transform.rotate(text, -4)
                screen.blit(text, (10,220))
                text = textfont.render('gotta JUMP it right', True, (0, 0, 0))
                text = pygame.transform.rotate(text, -4)
                screen.blit(text, (90,290))
                textfont = pygame.font.Font('font/The Brownies.otf', 25)
                text = textfont.render('MARTHA!!', True, (0, 0, 0))
                screen.blit(text, (600,390))
                text = textfont.render('wait.. was that my wallet on the grou...', True, (0, 0, 0))
                text = pygame.transform.rotate(text, 6)
                screen.blit(text, (20,380))
                text = textfont.render('oh.. nevermind', True, (0, 0, 0))
                text = pygame.transform.rotate(text, 6)
                screen.blit(text, (20,420))
        elif death_cause == 4:
            textfont = pygame.font.Font('font/The Brownies.otf', 25)
            text = textfont.render('Super Hot', True, (0, 0, 0))
            text = pygame.transform.rotate(text, -15)
            screen.blit(text, (680,230))
            text = textfont.render('Meteor!', True, (0, 0, 0))
            text = pygame.transform.rotate(text, -15)
            screen.blit(text, (680,250))
            textfont = pygame.font.Font('font/The Brownies.otf', 50)
            text = textfont.render('Try dodging it on the edge', True, (0, 0, 0))
            text = pygame.transform.rotate(text, -2)
            screen.blit(text, (30,220))
            text = textfont.render('like at the very left or right :3', True, (0, 0, 0))
            text = pygame.transform.rotate(text, 5)
            screen.blit(text, (10,290))
            textfont = pygame.font.Font('font/The Brownies.otf', 25)
            text = textfont.render('hint: dodge', True, (0, 0, 0))
            screen.blit(text, (600,390))
            text = textfont.render('another thing to care', True, (0, 0, 0))
            screen.blit(text, (50,380))
            text = textfont.render('ugh, am I right? now pet me', True, (0, 0, 0))
            screen.blit(text, (50,400))
            textfont = pygame.font.Font('font/OpenSans-Regular.ttf', 12)
            text = textfont.render('wow that :3 came out ugly', True, (0, 0, 0))
            text = pygame.transform.rotate(text, -2)
            screen.blit(text, (50,445))
        elif death_cause == 5:
            textfont = pygame.font.Font('font/The Brownies.otf', 25)
            text = textfont.render('firepops', True, (0, 0, 0))
            text = pygame.transform.rotate(text, 15)
            screen.blit(text, (590,220))
            text = textfont.render('oh boy, you\'ll die a lot to this one', True, (0, 0, 0))
            screen.blit(text, (20,160))
            if dialogue == 1:
                textfont = pygame.font.Font('font/The Brownies.otf', 50)
                text = textfont.render('wop wop.  Warps quite quick', True, (0, 0, 0))
                text = pygame.transform.rotate(text, 4)
                screen.blit(text, (10,220))
                text = textfont.render('What would you say, Luck?', True, (0, 0, 0))
                text = pygame.transform.rotate(text, -2)
                screen.blit(text, (80,290))
                text = textfont.render('..Or reflexes', True, (0, 0, 0))
                text = pygame.transform.rotate(text, -2)
                screen.blit(text, (100,340))
                textfont = pygame.font.Font('font/The Brownies.otf', 25)
                text = textfont.render('hint: stay away', True, (0, 0, 0))
                screen.blit(text, (600,390))
                text = textfont.render('already been nerfed actually   well its dodgeable now', True, (0, 0, 0))
                screen.blit(text, (40,190))
                text = textfont.render('not a explosion.. a pop.. !', True, (0, 0, 0))
                screen.blit(text, (70,440))
            else:
                textfont = pygame.font.Font('font/The Brownies.otf', 50)
                text = textfont.render('Ever played with firecrackers?', True, (0, 0, 0))
                text = pygame.transform.rotate(text, -2)
                screen.blit(text, (35,220))
                text = textfont.render('I used to think they were', True, (0, 0, 0))
                text = pygame.transform.rotate(text,-6)
                screen.blit(text, (30,255))
                text = textfont.render('suppose to be edible crackers', True, (0, 0, 0))
                text = pygame.transform.rotate(text,-10)
                screen.blit(text, (30,290))
                text = textfont.render('mmh.. toasty', True, (0, 0, 0))
                screen.blit(text, (40,370))
                textfont = pygame.font.Font('font/The Brownies.otf', 25)
                text = textfont.render('hint: don\'t eat', True, (0, 0, 0))
                screen.blit(text, (600,390))
        elif death_cause == 6:
            textfont = pygame.font.Font('font/The Brownies.otf', 50)
            text = textfont.render('well, It means don\'t jump', True, (0, 0, 0))
            screen.blit(text, (10,190))
            textfont = pygame.font.Font('font/The Brownies.otf', 20)
            text = textfont.render('that\'s scary, .. foof!', True, (0, 0, 0))
            screen.blit(text, (20,160))
            if dialogue == 1:
                textfont = pygame.font.Font('font/The Brownies.otf', 50)
                text = textfont.render('Would you take a look at that', True, (0, 0, 0))
                text = pygame.transform.rotate(text, 4)
                screen.blit(text, (30,230))
                text = textfont.render('don\'t you dare say', True, (0, 0, 0))
                text = pygame.transform.rotate(text, -2)
                screen.blit(text, (40,300))
                text = textfont.render('that looks like a turd', True, (0, 0, 0))
                text = pygame.transform.rotate(text, -2)
                screen.blit(text, (40,330))
                textfont = pygame.font.Font('font/The Brownies.otf', 25)
                text = textfont.render('HEADS UP!', True, (0, 0, 0))
                screen.blit(text, (600,390))
                text = textfont.render('looks bad in white and black', True, (0, 0, 0))
                screen.blit(text, (15,440))
                text = textfont.render('flamethrow', True, (0, 0, 0))
                screen.blit(text, (590,220))
            else:
                textfont = pygame.font.Font('font/The Brownies.otf', 50)
                text = textfont.render('you know how I\'d', True, (0, 0, 0))
                text = pygame.transform.rotate(text, -2)
                screen.blit(text, (40,230))
                text = textfont.render('make this game impossible?', True, (0, 0, 0))
                text = pygame.transform.rotate(text, -2)
                screen.blit(text, (40,260))
                text = textfont.render('make this last 3 more seconds', True, (0, 0, 0))
                screen.blit(text, (30,310))
                textfont = pygame.font.Font('font/The Brownies.otf', 25)
                text = textfont.render('\"whats up choom\"', True, (0, 0, 0))
                screen.blit(text, (590,390))
                text = textfont.render('you\'ll never die to this again,', True, (0, 0, 0))
                screen.blit(text, (15,400))
                text = textfont.render('thus you\'ll see me again :(', True, (0, 0, 0))
                screen.blit(text, (15,420))
                text = textfont.render('turd', True, (0, 0, 0))
                screen.blit(text, (590,220))
        elif death_cause == 7:
            textfont = pygame.font.Font('font/The Brownies.otf', 25)
            text = textfont.render('stocks', True, (0, 0, 0))
            text = pygame.transform.rotate(text, -20)
            screen.blit(text, (650,227))
            if dialogue == 1:
                textfont = pygame.font.Font('font/The Brownies.otf', 25)
                text = textfont.render('\"You rise, Only to fall\"', True, (0, 0, 0))
                text = pygame.transform.rotate(text, -2)
                screen.blit(text, (80,250))
                textfont = pygame.font.Font('font/The Brownies.otf', 25)
                text = textfont.render('hint: find gap', True, (0, 0, 0))
                screen.blit(text, (595,390))
                text = textfont.render('- Ultron', True, (0, 0, 0))
                text = pygame.transform.rotate(text, -2)
                screen.blit(text, (110,270))
            else:
                textfont = pygame.font.Font('font/The Brownies.otf', 50)
                text = textfont.render('hitbox is sometimes weird on this', True, (0, 0, 0))
                text = pygame.transform.rotate(text, -2)
                screen.blit(text, (10,220))
                text = textfont.render('so I fixed it lol gluck ;D', True, (0, 0, 0))
                text = pygame.transform.rotate(text, 5)
                screen.blit(text, (20,290))
                textfont = pygame.font.Font('font/The Brownies.otf', 20)
                text = textfont.render('are those fire pops bugging ya?', True, (0, 0, 0))
                screen.blit(text, (120,400))
                textfont = pygame.font.Font('font/The Brownies.otf', 25)
                text = textfont.render('hint: luck', True, (0, 0, 0))
                screen.blit(text, (595,390))
        elif death_cause == 8:
            textfont = pygame.font.Font('font/The Brownies.otf', 25)
            text = textfont.render('clumsy hands?', True, (0, 0, 0))
            text = pygame.transform.rotate(text, -2)
            screen.blit(text, (600,220))
            text = textfont.render('hint: stand still', True, (0, 0, 0))
            screen.blit(text, (600,390))
            if dialogue == 1:
                textfont = pygame.font.Font('font/The Brownies.otf', 22)
                text = textfont.render('A game over, it\'s time to contemplate.', True, (0, 0, 0))
                screen.blit(text, (10,180))
                text = textfont.render('Don\'t worry, my friend, it\'s just a blip,', True, (0, 0, 0))
                screen.blit(text, (10,195))
                text = textfont.render('A minor setback in your keyboard trip.', True, (0, 0, 0))
                screen.blit(text, (10,210))

                text = textfont.render('Your fingers flew, like lightning strikes,', True, (0, 0, 0))
                screen.blit(text, (10,240))
                text = textfont.render('But the obstacles got the best of your likes.', True, (0, 0, 0))
                screen.blit(text, (10,255))
                text = textfont.render('Perhaps you missed the landing,', True, (0, 0, 0))
                screen.blit(text, (10,270))
                text = textfont.render('Or got tired to hard gaming.', True, (0, 0, 0))
                screen.blit(text, (10,285))

                text = textfont.render('Now take a breath, reset your stance,', True, (0, 0, 0))
                screen.blit(text, (10,315))
                text = textfont.render('Get ready to give it another chance.', True, (0, 0, 0))
                screen.blit(text, (10,330))
                text = textfont.render('For in this game, failures are just part of the ride,', True, (0, 0, 0))
                screen.blit(text, (10,345))
                text = textfont.render('After all, a minute is all you\'ll have to survive.', True, (0, 0, 0))
                screen.blit(text, (10,360))
            else:
                textfont = pygame.font.Font('font/The Brownies.otf', 40)
                text = textfont.render('Well, you don\'t see this too often', True, (0, 0, 0))
                text = pygame.transform.rotate(text, -2)
                screen.blit(text, (35,240))
        #record
        cornerbox = pygame.transform.scale(cornerbox, (300, 120))
        screen.blit(cornerbox, (600,70))

        textfont = pygame.font.Font('font/The Brownies.otf', 60)
        text = textfont.render(str(ingame_timer), True, (0, 0, 0))
        screen.blit(text, (690,110))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEMOTION:
                if rect_backBut.collidepoint(event.pos):
                    backBut_show = "Green"
                else:
                    backBut_show = "Black"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and rect_backBut.collidepoint(event.pos):
                    backBut_show = "White"
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and rect_backBut.collidepoint(event.pos):
                    endscreen = False

        if backBut_show == "Black":
            screen.blit(backBut, rect_backBut)
        elif backBut_show == "Green":
            screen.blit(backBut_select, rect_backBut)
        else:
            screen.blit(backBut_click, rect_backBut)



        pygame.display.update()
        clock.tick(30)