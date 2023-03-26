import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption('yoyo')
clock = pygame.time.Clock()
font = pygame.font.Font('font/OpenSans-Regular.ttf', 50)

#surface 1
background = pygame.image.load('bgi/sky.png')
background = pygame.transform.scale(background, (810, 510))

#surface 2
platform = pygame.image.load('bgi/ground.png')
platform = pygame.transform.scale(platform, (700, 100))

#texts
text = font.render('My Game', True, 'yellow')

#main loop
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
    screen.blit(background, (0,0))
    screen.blit(platform, (50,400))

    pygame.display.update()
    clock.tick(60)