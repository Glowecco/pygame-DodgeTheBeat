import pygame
from playerClass import Player
from sys import exit

#constants
pygame.init()
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption('Dodge the Beat')
clock = pygame.time.Clock()
font = pygame.font.Font('font/OpenSans-Regular.ttf', 50)

#background surfaces
background = pygame.image.load('bgi/sky.png').convert()
background = pygame.transform.scale(background, (810, 510))
platform = pygame.image.load('bgi/ground.png').convert_alpha()
platform = pygame.transform.scale(platform, (700, 100))

#texts
text = font.render('My Game', True, 'yellow')

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

#save class to >>player
player = pygame.sprite.GroupSingle()
player.add(Player(stand_images, jump_image, run_images))

#main loop
gravity = -1
while True:
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
    #fps
    clock.tick(60)

#for music: https://www.youtube.com/watch?v=Qz8hMjq2ARU