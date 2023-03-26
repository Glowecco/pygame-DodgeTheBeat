import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption('Dodge the Beat')
clock = pygame.time.Clock()
font = pygame.font.Font('font/OpenSans-Regular.ttf', 50)

#surface 1
background = pygame.image.load('bgi/sky.png').convert()
background = pygame.transform.scale(background, (810, 510))

#surface 2
platform = pygame.image.load('bgi/ground.png').convert_alpha()
platform = pygame.transform.scale(platform, (700, 100))

#texts
text = font.render('My Game', True, 'yellow')

#player
player = pygame.image.load('player/rabbit -1.png').convert_alpha()
player = pygame.transform.scale(player, (27, 42))
playerRect = player.get_rect(midbottom = (400,400))
gravity = 0

#main loop
while True:
    #check for quit and player jump
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN and playerRect.bottom >= 400:
            if event.key == pygame.K_UP:
                gravity = -9
    
    #player move left and right
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        playerRect.left -= 3
    if keys[pygame.K_RIGHT]:
        playerRect.right += 3
        
    #draw on screen
    screen.blit(background, (0,0))
    screen.blit(platform, (50,400))
    screen.blit(player, playerRect)

    #fall physics
    gravity += 0.3
    playerRect.y += gravity
    if playerRect.bottom >= 400: 
        playerRect.bottom = 400

    #fps and update screen
    pygame.display.update()
    clock.tick(60)