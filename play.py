import pygame
import time
from constants import *
from deck import Deck
from hand import Hand
from gui import *
import sys

class Play:
    def __init__(self):
        self.deck = Deck()
        self.dealer = Hand()
        self.player = Hand()
        self.deck.shuffle()
        
    def blackjack(self, screen):

        self.dealer.calc_hand()
        self.player.calc_hand()

        show_dealer_card = pygame.image.load('img/' + self.dealer.card_img[1] + '.png').convert()
        
        if self.player.value == 21 and self.dealer.value == 21:
            screen.blit(show_dealer_card, (550, 200))
            black_jack("Both with BlackJack!", 500, 250, GREY)
            time.sleep(4)
            self.play_or_exit()
        elif self.player.value == 21:
            screen.blit(show_dealer_card, (550, 200))
            black_jack("You got BlackJack!", 500, 250, GREEN)
            time.sleep(4)
            self.play_or_exit()
        elif self.dealer.value == 21:
            screen.blit(show_dealer_card, (550, 200))
            black_jack("Dealer has BlackJack!", 500, 250, RED)
            time.sleep(4)
            self.play_or_exit()
            
        self.player.value = 0
        self.dealer.value = 0

    def deal(self, screen):
        for i in range(2):
            self.dealer.add_card(self.deck.deal)
            self.player.add_card(self.deck.deal)
        self.dealer.display_cards()
        self.player.display_cards()
        self.player_card = 1
        dealer_card = pygame.image.load('img/' + self.dealer.card_img[0] + '.png').convert()
        dealer_card_2 = pygame.image.load('img/back.png').convert()
            
        player_card = pygame.image.load('img/' + self.player.card_img[0] + '.png').convert()
        player_card_2 = pygame.image.load('img/' + self.player.card_img[1] + '.png').convert()

        
        game_texts("Dealer's hand is:", 500, 150)

        screen.blit(dealer_card, (400, 200))
        screen.blit(dealer_card_2, (550, 200))

        game_texts("Your's hand is:", 500, 400)
        
        screen.blit(player_card, (300, 450))
        screen.blit(player_card_2, (410, 450))
        self.blackjack()
            
            

    def hit(self, screen):
        self.player.add_card(self.deck.deal())
        self.blackjack()
        self.player_card += 1
        
        if self.player_card == 2:
            self.player.calc_hand()
            self.player.display_cards()
            player_card_3 = pygame.image.load('img/' + self.player.card_img[2] + '.png').convert()
            screen.blit(player_card_3, (520, 450))

        if self.player_card == 3:
            self.player.calc_hand()
            self.player.display_cards()
            player_card_4 = pygame.image.load('img/' + self.player.card_img[3] + '.png').convert()
            screen.blit(player_card_4, (630, 450))
                
        if self.player.value > 21:
            show_dealer_card = pygame.image.load('img/' + self.dealer.card_img[1] + '.png').convert()
            screen.blit(show_dealer_card, (550, 200))
            game_finish("You Busted!", 500, 250, RED)
            time.sleep(4)
            self.play_or_exit()
            
        self.player.value = 0

        if self.player_card > 4:
            sys.exit()
            
            
    def stand(self, screen):
        show_dealer_card = pygame.image.load('img/' + self.dealer.card_img[1] + '.png').convert()
        screen.blit(show_dealer_card, (550, 200))
        self.blackjack()
        self.dealer.calc_hand()
        self.player.calc_hand()
        if self.player.value > self.dealer.value:
            game_finish("You Won!", 500, 250, GREEN)
            time.sleep(4)
            self.play_or_exit()
        elif self.player.value < self.dealer.value:
            game_finish("Dealer Wins!", 500, 250, RED)
            time.sleep(4)
            self.play_or_exit()
        else:
            game_finish("It's a Tie!", 500, 250, GREY)
            time.sleep(4)
            self.play_or_exit()
        
    
    def exit(self):
        sys.exit()
    
    def play_or_exit(self, screen):
        game_texts("Play again press Deal!", 200, 80)
        time.sleep(3)
        self.player.value = 0
        self.dealer.value = 0
        self.deck = Deck()
        self.dealer = Hand()
        self.player = Hand()
        self.deck.shuffle()
        screen.fill(BACKGROUD_COLOR)
        pygame.draw.rect(screen, GREY, pygame.Rect(0, 0, 250, 700))
        pygame.display.update()