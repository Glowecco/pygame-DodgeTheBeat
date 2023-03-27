import pygame
from sys import exit

def playerAnimation():
    global playerShow, playerCostume_Index, playerCostume_Index_2, animationSpeed, keys

    if playerRect.bottom == 400 and running==False: #stand
        playerShow = playerCostume_StandJump[int(playerCostume_Index)]
        playerCostume_Index += animationSpeed
        if playerCostume_Index >= 7.7:
            animationSpeed = - 0.3
        elif playerCostume_Index < 0.3:
            animationSpeed = 0.3
    elif playerRect.bottom != 400: #jump
        playerShow = playerJump
    elif keys[pygame.K_LEFT]:
        if playerCostume_Index_2 >= 9.7:
            animationSpeed = -0.5
        elif playerCostume_Index_2 < 0:
            animationSpeed = 0.5
        playerShow = playerCostume_Run[int(playerCostume_Index_2)]
        playerCostume_Index_2 += animationSpeed
        print(playerCostume_Index_2)
        print('speed?: '+str(animationSpeed))   
    elif keys[pygame.K_RIGHT]:
        if playerCostume_Index_2 >= 9.7:
            animationSpeed = -0.5
        elif playerCostume_Index_2 < 0:
            animationSpeed = 0.5
        playerShow = playerCostume_Run[int(playerCostume_Index_2)]
        playerCostume_Index_2 += animationSpeed
        print(playerCostume_Index_2)
        print('speed?: '+str(animationSpeed))



pygame.init()
animationSpeed = 0.3
flipLeft = False
running = False
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
playerStand_1 = pygame.image.load('playerStand/rabbit -1.png').convert_alpha()
playerStand_1 = pygame.transform.scale(playerStand_1, (27, 42))
playerStand_2 = pygame.image.load('playerStand/rabbit -2.png').convert_alpha()
playerStand_2 = pygame.transform.scale(playerStand_2, (27, 42))
playerStand_3 = pygame.image.load('playerStand/rabbit -3.png').convert_alpha()
playerStand_3 = pygame.transform.scale(playerStand_3, (27, 42))
playerStand_4 = pygame.image.load('playerStand/rabbit -4.png').convert_alpha()
playerStand_4 = pygame.transform.scale(playerStand_4, (27, 42))
playerStand_5 = pygame.image.load('playerStand/rabbit -5.png').convert_alpha()
playerStand_5 = pygame.transform.scale(playerStand_5, (27, 42))
playerStand_6 = pygame.image.load('playerStand/rabbit -6.png').convert_alpha()
playerStand_6 = pygame.transform.scale(playerStand_6, (27, 42))
playerStand_7 = pygame.image.load('playerStand/rabbit -7.png').convert_alpha()
playerStand_7 = pygame.transform.scale(playerStand_7, (27, 42))
playerStand_8 = pygame.image.load('playerStand/rabbit -8.png').convert_alpha()
playerStand_8 = pygame.transform.scale(playerStand_8, (27, 42))
playerJump = pygame.image.load('playerJump/rabbit jump -2.png').convert_alpha()
playerJump = pygame.transform.scale(playerJump, (28, 45))
playerRun_1 = pygame.image.load('playerRun/rabbit run -1.png').convert_alpha()
playerRun_1 = pygame.transform.scale(playerRun_1, (30, 43.5))
playerRun_2 = pygame.image.load('playerRun/rabbit run -2.png').convert_alpha()
playerRun_2 = pygame.transform.scale(playerRun_2, (30, 43.5))
playerRun_3 = pygame.image.load('playerRun/rabbit run -3.png').convert_alpha()
playerRun_3 = pygame.transform.scale(playerRun_3, (30, 43.5))
playerRun_4 = pygame.image.load('playerRun/rabbit run -4.png').convert_alpha()
playerRun_4 = pygame.transform.scale(playerRun_4, (30, 43.5))
playerRun_5 = pygame.image.load('playerRun/rabbit run -5.png').convert_alpha()
playerRun_5 = pygame.transform.scale(playerRun_5, (30, 43.5))
playerRun_6 = pygame.image.load('playerRun/rabbit run -6.png').convert_alpha()
playerRun_6 = pygame.transform.scale(playerRun_6, (30, 43.5))
playerRun_7 = pygame.image.load('playerRun/rabbit run -7.png').convert_alpha()
playerRun_7 = pygame.transform.scale(playerRun_7, (30, 43.5))
playerRun_8 = pygame.image.load('playerRun/rabbit run -8.png').convert_alpha()
playerRun_8 = pygame.transform.scale(playerRun_8, (30, 43.5))
playerRun_9 = pygame.image.load('playerRun/rabbit run -9.png').convert_alpha()
playerRun_9 = pygame.transform.scale(playerRun_9, (30, 43.5))
playerRun_10 = pygame.image.load('playerRun/rabbit run -10.png').convert_alpha()
playerRun_10 = pygame.transform.scale(playerRun_10, (30, 43.5))

playerCostume_Index = 0
playerCostume_Index_2 = 0
playerCostume_StandJump = [playerStand_1, playerStand_2, playerStand_3, playerStand_4
    , playerStand_5, playerStand_6, playerStand_7, playerStand_8]
playerCostume_Run = [playerRun_1, playerRun_2, playerRun_3, playerRun_4, 
    playerRun_5, playerRun_6, playerRun_7, playerRun_8, playerRun_9, playerRun_10, ]

playerShow = playerStand_1

playerRect = playerShow.get_rect(midbottom = (400,400))
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
                gravity = -7
    
    #player move left and right
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        playerRect.left -= 4
        flipLeft = True
        running = True
    elif keys[pygame.K_RIGHT]:
        playerRect.right += 4
        flipLeft = False
        running = True
    else:
        running = False
        
    #draw on screen
    playerAnimation()
    playerShow = pygame.transform.flip(playerShow, flipLeft, False)
    screen.blit(background, (0,0))
    screen.blit(platform, (50,400))
    screen.blit(playerShow, playerRect)

    #fall physics
    gravity += 0.3
    playerRect.y += gravity
    if playerRect.bottom >= 400: 
        playerRect.bottom = 400

    #fps and update screen
    pygame.display.update()
    clock.tick(60)