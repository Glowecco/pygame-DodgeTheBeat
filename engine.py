import pygame
import webbrowser as wb
from sys import exit
from game import level1 #importing levels from "game.py"

#Global
winner = "cache"
goBack_Button_coords = (25,45)
total_coins = 0
coin_coords = (750,10)
skill_selection = 0

#Character setting screen
def characterSetting(screen):
    global total_coins, skill_selection
    goBack_show = "Dim"
    right_arrow_show = "Dim"
    left_arrow_show = "Dim"
    right_arrow_mini_show = "Dim"
    left_arrow_mini_show = "Dim"
    #images
    shopScreen = pygame.image.load('images_background/5.png').convert()
    shopScreen = pygame.transform.scale(shopScreen, (800, 500))
    goBack_button = pygame.image.load('images_buttons/goBackBut.png').convert_alpha()
    goBack_button = pygame.transform.scale(goBack_button, (50, 50))
    goBack_button_select = pygame.image.load('images_buttons/goBackBut_select.png').convert_alpha()
    goBack_button_select = pygame.transform.scale(goBack_button_select, (50, 50))
    coin_icon = pygame.image.load('images_icons/coinIcon.png').convert_alpha()
    coin_icon = pygame.transform.scale(coin_icon, (50, 50))
    rabbit_choice = pygame.image.load('images_player/playerRun/rabbit run -1.png').convert_alpha()
    rabbit_choice = pygame.transform.scale(rabbit_choice, (120, 174))
    left_arrow = pygame.image.load('images_buttons/left.png').convert_alpha()
    left_arrow = pygame.transform.scale(left_arrow, (32, 64))
    right_arrow = pygame.image.load('images_buttons/right.png').convert_alpha()
    right_arrow = pygame.transform.scale(right_arrow, (32, 64))
    left_arrow_select = pygame.image.load('images_buttons/left_select.png').convert_alpha()
    left_arrow_select = pygame.transform.scale(left_arrow_select, (32, 64))
    right_arrow_select = pygame.image.load('images_buttons/right_select.png').convert_alpha()
    right_arrow_select = pygame.transform.scale(right_arrow_select, (32, 64))
    skill_icon_dash = pygame.image.load('images_icons/dash.png').convert_alpha()
    skill_icon_dash = pygame.transform.scale(skill_icon_dash, (48, 48))
    left_arrow_mini = pygame.transform.scale(left_arrow, (16, 32))
    right_arrow_mini = pygame.transform.scale(right_arrow, (16, 32))
    left_arrow_mini_select = pygame.transform.scale(left_arrow_select, (16, 32))
    right_arrow_mini_select = pygame.transform.scale(right_arrow_select, (16, 32))
    no_skill = pygame.image.load('images_icons/no_skill.png').convert_alpha()
    no_skill = pygame.transform.scale(no_skill, (45, 45))
    #rects 
    rect_goBack = goBack_button.get_rect(midbottom = goBack_Button_coords)
    rect_leftArrow_mini = left_arrow_mini.get_rect(midbottom = (342,285))
    rect_rightArrow_mini = right_arrow_mini.get_rect(midbottom = (467,285))
    rect_leftArrow = left_arrow.get_rect(midbottom = (285,170))
    rect_rightArrow = right_arrow.get_rect(midbottom = (530,170))
    #main loop
    inCharSet = True
    while inCharSet:
        screen.blit(shopScreen, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()      
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and rect_goBack.collidepoint(event.pos):
                    return(True)
                elif event.button == 1 and rect_leftArrow_mini.collidepoint(event.pos):
                    skill_selection = 1
                elif event.button == 1 and rect_rightArrow_mini.collidepoint(event.pos):
                    skill_selection = 0
            if event.type == pygame.MOUSEMOTION:
                if rect_goBack.collidepoint(event.pos):
                    goBack_show = 'Light'
                else: 
                    goBack_show = 'Dim'
                if rect_leftArrow.collidepoint(event.pos):
                    left_arrow_show = 'Light'
                else: 
                    left_arrow_show = 'Dim'
                if rect_rightArrow.collidepoint(event.pos):
                    right_arrow_show = 'Light'
                else: 
                    right_arrow_show = 'Dim'
                if rect_leftArrow_mini.collidepoint(event.pos):
                    left_arrow_mini_show = 'Light'
                else: 
                    left_arrow_mini_show = 'Dim'
                if rect_rightArrow_mini.collidepoint(event.pos):
                    right_arrow_mini_show = 'Light'
                else: 
                    right_arrow_mini_show = 'Dim'
                
        if goBack_show == "Light":
            screen.blit(goBack_button_select, rect_goBack)
        else:
            screen.blit(goBack_button, rect_goBack)

        if left_arrow_show == "Light":
            screen.blit(left_arrow_select, rect_leftArrow)
        else:
            screen.blit(left_arrow, rect_leftArrow)
        if right_arrow_show == "Light":
            screen.blit(right_arrow_select, rect_rightArrow)
        else:
            screen.blit(right_arrow, rect_rightArrow)
        
        if left_arrow_mini_show == "Light":
            screen.blit(left_arrow_mini_select, rect_leftArrow_mini)
        else:
            screen.blit(left_arrow_mini, rect_leftArrow_mini)

        if right_arrow_mini_show == "Light":
            screen.blit(right_arrow_mini_select, rect_rightArrow_mini)
        else:
            screen.blit(right_arrow_mini, rect_rightArrow_mini)
        
        screen.blit(coin_icon, coin_coords)
        textfont = pygame.font.Font('font/The Brownies.otf', 30)
        text = textfont.render(str(total_coins), True, (0, 0, 0))
        text = pygame.transform.rotate(text, -2)
        screen.blit(text, (710,20))

        screen.blit(rabbit_choice, (350,50))
        textfont = pygame.font.Font('font/The Brownies.otf', 40)
        text = textfont.render('Character:', True, (0, 0, 0))
        screen.blit(text, (170,50))
        text = textfont.render('Ability:', True, (0, 0, 0))
        screen.blit(text, (220,250))
        textfont = pygame.font.Font('font/OpenSans-Regular.ttf', 20)
        text = textfont.render('Survive longer for more coins', True, (0, 0, 0))
        screen.blit(text, (10,460))
    
        if skill_selection == 0:
            screen.blit(no_skill, (383,250))
        elif skill_selection == 1:
            screen.blit(skill_icon_dash, (383,250))
            textfont = pygame.font.Font('font/OpenSans-Regular.ttf', 30)
            text = textfont.render('press \'x\' key to Dash', True, (0, 0, 0))
            screen.blit(text, (400,300))

        pygame.display.update()
        clock.tick(10)
#Level selection screen
def levelSelect(screen):
    #constants
    level1_Button_coords = (120,200)
    #variables
    level1_show = "UP"
    goBack_show = "Light"
    #images
    menuScreen = pygame.image.load('images_background/menu.jpg').convert()
    menuScreen = pygame.transform.scale(menuScreen, (800, 500))
    level1_button = pygame.image.load('images_buttons/key1_up.png').convert_alpha()
    level1_button = pygame.transform.scale(level1_button, (64, 64))
    level1_button_select = pygame.image.load('images_buttons/key1_down.png').convert_alpha()
    level1_button_select = pygame.transform.scale(level1_button_select, (64, 64))
    goBack_button = pygame.image.load('images_buttons/goBackBut.png').convert_alpha()
    goBack_button = pygame.transform.scale(goBack_button, (50, 50))
    goBack_button_select = pygame.image.load('images_buttons/goBackBut_select.png').convert_alpha()
    goBack_button_select = pygame.transform.scale(goBack_button_select, (50, 50))
    #rect
    rect_level1 = level1_button.get_rect(midbottom = level1_Button_coords)
    rect_goBack = goBack_button.get_rect(midbottom = goBack_Button_coords)

    #main loop
    inLevSel = True
    while inLevSel:
        screen.blit(menuScreen, (0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()      
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and rect_level1.collidepoint(event.pos):
                    return(False)
                elif event.button == 1 and rect_goBack.collidepoint(event.pos):
                    return(True)
            if event.type == pygame.MOUSEMOTION:
                if rect_level1.collidepoint(event.pos):
                    level1_show = "DOWN"
                else:
                    level1_show = "UP"
                if rect_goBack.collidepoint(event.pos):
                    goBack_show = 'Light'
                else: 
                    goBack_show = 'Dim'
                    
        if level1_show == "DOWN":
            screen.blit(level1_button_select, rect_level1)
        else:
            screen.blit(level1_button, rect_level1)

        if goBack_show == "Light":
            screen.blit(goBack_button_select, rect_goBack)
        else:
            screen.blit(goBack_button, rect_goBack)

        pygame.display.update()
        clock.tick(10)

#Credits screen
def credits(screen):   
    goBack_show = "Dim"
    #images
    creditsScreen = pygame.image.load('images_background/credits.jpg').convert()
    creditsScreen = pygame.transform.scale(creditsScreen, (800, 500))
    goBack_button = pygame.image.load('images_buttons/goBackBut.png').convert_alpha()
    goBack_button = pygame.transform.scale(goBack_button, (50, 50))
    goBack_button_select = pygame.image.load('images_buttons/goBackBut_select.png').convert_alpha()
    goBack_button_select = pygame.transform.scale(goBack_button_select, (50, 50))
    #rects
    rect_goBack = goBack_button.get_rect(midbottom = goBack_Button_coords)
    github_link = pygame.Rect(0,0,320,15)
    github_link.midbottom = (490,320)
    patreon_link = pygame.Rect(0,0,400,15)
    patreon_link.midbottom = (50,498)

    #main loop
    inCredits = True
    while inCredits:
        screen.blit(creditsScreen, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()      
            elif event.type == pygame.MOUSEMOTION:
                    if rect_goBack.collidepoint(event.pos):
                        goBack_show = 'Light'
                    else: 
                        goBack_show = 'Dim'
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and rect_goBack.collidepoint(event.pos):
                    inCredits = False
                elif event.button == 1 and github_link.collidepoint(event.pos):
                    wb.open("https://github.com/Glowecco/pygame-DodgeTheBeat")
                elif event.button == 1 and patreon_link.collidepoint(event.pos):
                    wb.open("https://www.patreon.com/user?u=31429527")
        if goBack_show == "Light":
            screen.blit(goBack_button_select, rect_goBack)
        else:
            screen.blit(goBack_button, rect_goBack)
        # pygame.draw.rect(screen, (0, 0, 255), github_link)
        # pygame.draw.rect(screen, (0, 0, 255), patreon_link)
        pygame.display.update()
        clock.tick(10)

#Menu screen
def startMenu(screen, earning):
    global total_coins
    total_coins += int(earning)
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
    staricon = pygame.image.load('images_icons/star.png').convert_alpha()
    staricon = pygame.transform.scale(staricon, (75, 51))
    #rects
    levelBut_rect = start_button.get_rect(midbottom = startButton_location)
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
                if event.button == 1 and levelBut_rect.collidepoint(event.pos):
                    inMenu = levelSelect(screen)
                elif event.button == 1 and creditBut_rect.collidepoint(event.pos):
                    credits(screen)
                    screen.blit(menuScreen, (0,0))
                elif event.button == 1 and charBut_rect.collidepoint(event.pos):
                    characterSetting(screen)
                    screen.blit(menuScreen, (0,0))
            if event.type == pygame.MOUSEMOTION:
                    if levelBut_rect.collidepoint(event.pos):
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
        if inMenu == True:
            if startBut_show == "Black":
                screen.blit(start_button_select, levelBut_rect)
            else:
                screen.blit(start_button, levelBut_rect)
            if characterBut_show == "Black":
                screen.blit(characterBut_select, charBut_rect)
            else:
                screen.blit(characterBut, charBut_rect)
            if creditBut_show == "Black":
                screen.blit(creditBut_select, creditBut_rect)
            else:
                screen.blit(creditBut, creditBut_rect)
        #update
        if winner == True:
            screen.blit(staricon, (-20,-5))
        pygame.display.update()
        clock.tick(10)

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
    if winner == True:
        startMenu(screen, 60)
    elif type(winner) == float:
        startMenu(screen, winner)
    else:
        startMenu(screen, 0)

    if winner == True:
        level1(screen, clock, font, textfont, winner, skill_selection)
    else:
        winner = level1(screen, clock, font, textfont, winner, skill_selection)

    # level2(screen, clock)