import pygame
from sys import exit

from game import level1 #importing levels from "game.py"
#Level selection screen
def levelSelect(screen):
    #images
    menuScreen = pygame.image.load('images_background/menu.jpg').convert()
    menuScreen = pygame.transform.scale(menuScreen, (810, 510))

    #main loop
    inLevSel = True
    while inLevSel:
        screen.blit(menuScreen, (0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()      
        
        pygame.display.update()

#Menu screen
def startMenu(screen):
    #constants
    startButton_location = (400,200)
    charButton_location = (400, 275)
    creditButton_location = (400, 350)
    #variables
    startBut_show = "White"
    characterBut_show = "White"
    creditBut_show = "White"

    #images
    menuScreen = pygame.image.load('images_background/menu.jpg').convert()
    menuScreen = pygame.transform.scale(menuScreen, (810, 510))
    start_button = pygame.image.load('images_buttons/levelBut.png').convert_alpha()
    start_button = pygame.transform.scale(start_button, (200, 55))
    start_button_select = pygame.image.load('images_buttons/levelBut-.png').convert_alpha()
    start_button_select = pygame.transform.scale(start_button_select, (200, 55))
    characterBut = pygame.image.load('images_buttons/charBut.png').convert_alpha()
    characterBut = pygame.transform.scale(characterBut, (200, 55))
    characterBut_select = pygame.image.load('images_buttons/charBut-.png').convert_alpha()
    characterBut_select = pygame.transform.scale(characterBut_select, (200, 55))
    creditBut = pygame.image.load('images_buttons/creditBut.png').convert_alpha()
    creditBut = pygame.transform.scale(creditBut, (200, 55))
    creditBut_select = pygame.image.load('images_buttons/creditBut-.png').convert_alpha()
    creditBut_select = pygame.transform.scale(creditBut_select, (200, 55))
    #rects
    startBut_rect = start_button.get_rect(midbottom = startButton_location)
    charBut_rect = characterBut.get_rect(midbottom = charButton_location)
    creditBut_rect = creditBut.get_rect(midbottom = creditButton_location)

    #main loop
    inMenu = True
    while inMenu:

        #display menu background
        screen.blit(menuScreen, (0,0))

        #detections and display buttons
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and startBut_rect.collidepoint(event.pos):
                    inMenu = False
            if event.type == pygame.MOUSEMOTION:
                    if startBut_rect.collidepoint(event.pos):
                        startBut_show = "Black"
                    else:
                        startBut_show = "White"
                    if charBut_rect.collidepoint(event.pos):
                        characterBut_show = "Black"
                    else:
                        characterBut_show = "White"
                    if creditBut_rect.collidepoint(event.pos):
                        creditBut_show = "Black"
                    else:
                        creditBut_show = "White"
        if startBut_show == "Black":
            screen.blit(start_button_select, startBut_rect)
        else:
            screen.blit(start_button, startBut_rect)
        if characterBut_show == "Black":
             screen.blit(characterBut_select, charBut_rect)
        else:
            screen.blit(characterBut, charBut_rect)
        if creditBut_show == "Black":
             screen.blit(creditBut_select, creditBut_rect)
        else:
            screen.blit(creditBut, creditBut_rect)
        #update
        pygame.display.update()

#window setup
pygame.init()
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption('Dodge the Beat')

#constants
clock = pygame.time.Clock()
font = pygame.font.Font('font/AspectRatio-3D.ttf', 25)
textfont = pygame.font.Font('font/The Brownies.otf', 25)

#START
while True:
    startMenu(screen)
    level1(screen, clock, font, textfont)
    # level2(screen, clock)