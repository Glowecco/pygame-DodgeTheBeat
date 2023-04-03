import pygame
from sys import exit

def startMenu(screen, clock):

    #constants
    startButton_location = (400,250)

    #main loop
    inMenu = True
    while inMenu:
        menuScreen = pygame.image.load('bgi/menu.png').convert()
        menuScreen = pygame.transform.scale(menuScreen, (810, 510))
        start_button = pygame.image.load('buttons/startBut.png').convert()
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
        clock.tick(60)