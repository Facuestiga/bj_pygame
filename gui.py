import pygame
from constants import *

###text object render
def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

def end_text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


#game text display
def game_texts(text, x, y, screen):
    TextSurf, TextRect = text_objects(text, TEXT_FONT)
    TextRect.center = (x, y)
    screen.blit(TextSurf, TextRect)

    pygame.display.update()

 
def game_finish(text, x, y, color, screen):
    TextSurf, TextRect = end_text_objects(text, GAME_END, color)
    TextRect.center = (x, y)
    screen.blit(TextSurf, TextRect)
    pygame.display.update()

def black_jack(text, x, y, color, screen):
    TextSurf, TextRect = end_text_objects(text, BLACKJACK, color)
    TextRect.center = (x, y)
    screen.blit(TextSurf, TextRect)
    pygame.display.update()
    
#button display
def button(screen,msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x, y, w, h))
        if click[0] == 1 != None:
            action(screen)
    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))

    TextSurf, TextRect = text_objects(msg, FONT)
    TextRect.center = ((x + (w/2)), (y + (h/2)))
    screen.blit(TextSurf, TextRect)