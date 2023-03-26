import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption('yoyo')
clock = pygame.time.Clock()
font = pygame.font.Font('OpenSans-Regular.ttf', 50)

background = pygame.image.load('sky.png')
background = pygame.transform.scale(background, (810, 510))

platform = pygame.image.load('ground.png')
platform = pygame.transform.scale(platform, (700, 100))

text = font.render('My Game', True, 'yellow')

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
    screen.blit(background, (0,0))
    screen.blit(platform, (50,400))
    screen.blit(text, (320, 150))

    pygame.display.update()
    clock.tick(60)