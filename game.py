import pygame
from Class_player import Player
from Class_obstacles import Obstacle
from sys import exit

timer_term = 0
official_timer = 0

def level1(screen, clock):
    # setup
    pygame.init()
    Alive = True

    #constants
    bgm1 = pygame.mixer.Sound('mp3/bgm.mp3')
    bgm1.set_volume(0.4)
    start_time = pygame.time.get_ticks()

    #background surfaces
    background = pygame.image.load('bgi/sky.png').convert()
    background = pygame.transform.scale(background, (810, 510))
    platform = pygame.image.load('bgi/ground.png').convert_alpha()
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
                print('collided!'+str(i))
                #Alive = False
                pass
        for i in range(1,3):
            obstacles_sprite.setRect_firepillar(i)
            collision = pygame.sprite.spritecollide(player_sprite, obstacles, False)
            if collision:
                print('collide PILLAR'+str(i))
                #Alive = False
                pass
        obstacles_sprite.setRect_fireground()
        collision = pygame.sprite.spritecollide(player_sprite, obstacles, False)
        if collision:
            print('collide FIRE GROUND')
            #Alive = False
            pass
        for i in range(1,3):
            obstacles_sprite.setRect_firedrop(i)
            collision = pygame.sprite.spritecollide(player_sprite, obstacles, False)
            if collision:
                if i == 1:
                    print('collide RIGHT METEOR')
                elif i == 2:
                    print('collide LEFT METEOR')

        #fps
        clock.tick(60)


