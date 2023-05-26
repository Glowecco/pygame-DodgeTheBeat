import pygame
from Class_player import Player
from Class_obstacles import Obstacle
from sys import exit

def level1(screen, clock):
    # setup
    pygame.init()
    Alive = True
    DEBUGGING_MODE = 3
    '''
    __DEBUGGING_MODE manual__
    1: dies on collision 
    2: dies on collision & prints collision
    3: immortal & prints collisions
    4: immortal & doesn't print any collision
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
        obstacles.update(screen, start_time)
        #update and draw player
        player.update()
        player.draw(screen)
        pygame.display.update()

        #Collsion (Gameover)
        Alive = player_sprite.ALIVE
        for i in range(1,7):
            obstacles_sprite.setRect_fireball(i)
            collision = pygame.sprite.spritecollide(player_sprite, obstacles, False)
            if collision:
                if DEBUGGING_MODE==1:
                    Alive = False
                elif DEBUGGING_MODE==2:
                    print('collided FIRE BALL '+str(i))
                    Alive = False
                elif DEBUGGING_MODE==3:
                    print('collided FIRE BALL '+str(i))
                else:
                    pass
        for i in range(1,3):
            obstacles_sprite.setRect_firepillar(i)
            collision = pygame.sprite.spritecollide(player_sprite, obstacles, False)
            if collision:
                if DEBUGGING_MODE==1:
                    Alive = False
                elif DEBUGGING_MODE==2:
                    print('collided PILLAR '+str(i))
                    Alive = False
                elif DEBUGGING_MODE==3:
                    print('collided PILLAR '+str(i))
                else:
                    pass
        obstacles_sprite.setRect_fireground()
        collision = pygame.sprite.spritecollide(player_sprite, obstacles, False)
        if collision:
            if DEBUGGING_MODE==1:
                Alive = False
            elif DEBUGGING_MODE==2:
                print('collided FIRE GROUND')
                Alive = False
            elif DEBUGGING_MODE==3:
                print('collided FIRE GROUND')
            else:
                pass
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
                    elif DEBUGGING_MODE==3:
                        print('collided RIGHT METEOR')
                    else:
                        pass
                elif i == 2:
                    if DEBUGGING_MODE==1:
                        Alive = False
                    elif DEBUGGING_MODE==2:
                        print('collided LEFT METEOR')
                        Alive = False
                    elif DEBUGGING_MODE==3:
                        print('collided LEFT METEOR')
                    else:
                        pass
        obstacles_sprite.setRect_firepop()
        collision = pygame.sprite.spritecollide(player_sprite, obstacles, False)
        if collision:
            if DEBUGGING_MODE==1:
                Alive = False
            elif DEBUGGING_MODE==2:
                print('collided FIRE POP')
                Alive = False
            elif DEBUGGING_MODE==3:
                print('collided FIRE POP')
            else:
                pass
                
        obstacles_sprite.setRect_flamethrow()
        collision = pygame.sprite.spritecollide(player_sprite, obstacles, False)
        if collision:
            if DEBUGGING_MODE==1:
                Alive = False
            elif DEBUGGING_MODE==2:
                print('collided FLAMETHROW')
                Alive = False
            elif DEBUGGING_MODE==3:
                print('collided FLAMETHROW')
            else:
                pass
                
        #fps
        clock.tick(60)


