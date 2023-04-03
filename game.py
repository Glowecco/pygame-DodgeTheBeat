import pygame
from Class_player import Player
from sys import exit

def level1(screen, clock):
    # setup
    pygame.init()

    #constants
    bgm1 = pygame.mixer.Sound('bgm.mp3')
    bgm1.set_volume(0.4)
    
    Alive = True

    #background surfaces
    background = pygame.image.load('bgi/sky.png').convert()
    background = pygame.transform.scale(background, (810, 510))
    platform = pygame.image.load('bgi/ground.png').convert_alpha()
    platform = pygame.transform.scale(platform, (700, 100))

    #download player images
    file_extensions = '.png'
    stand_images = []
    run_images = []
    for i in range(1, 9):
        filename = f"{'playerStand/rabbit -'}{i}{file_extensions}"
        image = pygame.image.load(filename).convert_alpha()
        image = pygame.transform.scale(image, (27, 42))
        stand_images.append(image)
    jump_image = pygame.image.load('playerJump/rabbit jump -2.png').convert_alpha()
    jump_image = pygame.transform.scale(jump_image, (28, 45))
    for i in range(1, 11):
        filename = f"{'playerRun/rabbit run -'}{i}{file_extensions}"
        image = pygame.image.load(filename).convert_alpha()
        image = pygame.transform.scale(image, (30, 43.5))
        run_images.append(image)

    #save Player class to >> player
    player = pygame.sprite.GroupSingle()
    player.add(Player(stand_images, jump_image, run_images))
    player_sprite = player.sprite
    #main loop
    bgm1.play()
    while Alive:
        #check for quit 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        #update and draw
        screen.blit(background, (0,0))
        screen.blit(platform, (50,400))
        player.update()
        player.draw(screen)
        pygame.display.update()
        Alive = player_sprite.ALIVE
  
        #fps
        clock.tick(60)
    bgm1.stop()

