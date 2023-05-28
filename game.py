import pygame
from Class_player import Player
from Class_obstacles import Obstacle

from sys import exit

def level1(screen, clock):
    # setup
    pygame.init()
    Alive = True
    DEBUGGING_MODE = 2
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

    #background surfaces
    background = pygame.image.load('images_background/sky.png').convert()
    background = pygame.transform.scale(background, (810, 510))
    platform = pygame.image.load('images_background/ground.png').convert_alpha()
    platform = pygame.transform.scale(platform, (700, 100))

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
        #check for quit 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                bgm1.stop()
                pygame.quit()
                exit()
        if Alive == False:
            bgm1.stop()
            break

        #draw background
        screen.blit(background, (0,0))
        screen.blit(platform, (50,400))

        #update and draw obstacles
        obstacles.update(screen, start_time, DEBUGGING_MODE)
        #update and draw player
        player.update()
        player.draw(screen)
        pygame.display.update()

        #Collsion (Gameover)
        Alive = player_sprite.ALIVE
            #fireball
        for i in range(1,7):
            obstacles_sprite.setRect_fireball(i)
            collision = pygame.sprite.spritecollide(player_sprite, obstacles, False)
            if collision:
                if DEBUGGING_MODE==1:
                    Alive = False
                elif DEBUGGING_MODE==2:
                    print('collided FIRE BALL '+str(i))
                    Alive = False
                elif DEBUGGING_MODE==3 or DEBUGGING_MODE==4:
                    print('collided FIRE BALL '+str(i))
                else:
                    pass
            #firepillar
        for i in range(1,3):
            obstacles_sprite.setRect_firepillar(i)
            collision = pygame.sprite.spritecollide(player_sprite, obstacles, False)
            if collision:
                if DEBUGGING_MODE==1:
                    Alive = False
                elif DEBUGGING_MODE==2:
                    print('collided PILLAR '+str(i))
                    Alive = False
                elif DEBUGGING_MODE==3 or DEBUGGING_MODE==4:
                    print('collided PILLAR '+str(i))
                else:
                    pass
            #fireground
        obstacles_sprite.setRect_fireground()
        collision = pygame.sprite.spritecollide(player_sprite, obstacles, False)
        if collision:
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
        for i in range(1,3):
            obstacles_sprite.setRect_firedrop(i)
            collision = pygame.sprite.spritecollide(player_sprite, obstacles, False)
            if collision:
                if i == 1:
                    if DEBUGGING_MODE==1:
                        Alive = False
                    elif DEBUGGING_MODE==2:
                        print('collided RIGHT METEOR')
                        Alive = False
                    elif DEBUGGING_MODE==3 or DEBUGGING_MODE==4:
                        print('collided RIGHT METEOR')
                    else:
                        pass
                elif i == 2:
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
        for i in range(1,13):
            obstacles_sprite.setRect_meteor(i)
            collision = pygame.sprite.spritecollide(player_sprite, obstacles, False)
            if collision:
                if DEBUGGING_MODE==1:
                    Alive = False
                elif DEBUGGING_MODE==2:
                    print('collided METEOR '+str(i))
                    Alive = False
                elif DEBUGGING_MODE==3 or DEBUGGING_MODE==4:
                    print('collided METEOR '+str(i))
                else:
                    pass
            #flamefall
        for i in range(1,5):
            obstacles_sprite.setRect_flamefall(i)
            collision = pygame.sprite.spritecollide(player_sprite, obstacles, False)
            if collision:
                if DEBUGGING_MODE==1:
                    Alive = False
                elif DEBUGGING_MODE==2:
                    print('collided FLAME FALL '+str(i))
                    Alive = False
                elif DEBUGGING_MODE==3 or DEBUGGING_MODE==4:
                    print('collided FLAME FALL '+str(i))
                else:
                    pass
        #fps
        clock.tick(60)


