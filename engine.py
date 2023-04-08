import pygame
from sys import exit
from Class_player import Player
from menu import startMenu
from game import level1

#window setup
pygame.init()
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption('Dodge the Beat')

#constants
clock = pygame.time.Clock()
font = pygame.font.Font('font/OpenSans-Regular.ttf', 50)

while True:
    startMenu(screen, clock)
    level1(screen, clock)
