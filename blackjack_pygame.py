import pygame as pygame
from play import Play
from gui import button
from constants import *


pygame.init()

clock = pygame.time.Clock()

#set screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('BlackJack')
screen.fill(BACKGROUD_COLOR)

pygame.draw.rect(screen, GREY, pygame.Rect(0, 0, 250, 700))
        
play_blackjack = Play()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        button(screen, "Deal", 30, 100, 150, 50, LIGHT_SLAT, DARK_SLAT, play_blackjack.deal)
        button(screen, "Hit", 30, 200, 150, 50, LIGHT_SLAT, DARK_SLAT, play_blackjack.hit)
        button(screen, "Stand", 30, 300, 150, 50, LIGHT_SLAT, DARK_SLAT, play_blackjack.stand)
        button(screen, "EXIT", 30, 500, 150, 50, LIGHT_SLAT, DARK_RED, play_blackjack.exit)
    
    pygame.display.flip()