import pygame
from sys import exit

from game import level1 #importing levels from "game.py"

#Menu screen
def startMenu(screen):
    #constants
    startButton_location = (400,250)

    #main loop
    inMenu = True
    while inMenu:
        menuScreen = pygame.image.load('images_background/menu.png').convert()
        menuScreen = pygame.transform.scale(menuScreen, (810, 510))
        start_button = pygame.image.load('images_buttons/startBut.png').convert()
        start_button = pygame.transform.scale(start_button, (160, 54))
        start_rect = start_button.get_rect(midbottom = startButton_location)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and start_rect.collidepoint(event.pos):
                    inMenu = False
                    
        screen.blit(menuScreen, (0,0))
        screen.blit(start_button, start_button.get_rect(midbottom = startButton_location))    
        pygame.display.update()

#window setup
pygame.init()
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption('Dodge the Beat')

#constants
clock = pygame.time.Clock()
font = pygame.font.Font('font/OpenSans-Regular.ttf', 50)

#START
while True:
    startMenu(screen)
    level1(screen, clock)
    # level2(screen, clock)