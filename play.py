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
        self.is_cards_dealt = False # manage if cards are been dealt to player and dealer
        
    def blackjack(self, screen):

        self.dealer.calc_hand()
        self.player.calc_hand()

        show_dealer_card = pygame.image.load('img/' + self.dealer.card_img[1] + '.png').convert()
        
        if self.player.calc_hand() == 21 and self.dealer.calc_hand() == 21:
            screen.blit(show_dealer_card, (550, 200))
            black_jack("Both with BlackJack!", 500, 250, GREY, screen)
            time.sleep(4)
            self.play_or_exit(screen)
        elif self.player.calc_hand() == 21:
            screen.blit(show_dealer_card, (550, 200))
            black_jack("You got BlackJack!", 500, 250, GREEN, screen)
            time.sleep(4)
            self.play_or_exit(screen)
        elif self.dealer.value == 21:
            screen.blit(show_dealer_card, (550, 200))
            black_jack("Dealer has BlackJack!", 500, 250, RED, screen)
            time.sleep(4)
            self.play_or_exit(screen)
            
        self.player.value = 0
        self.dealer.value = 0

    def deal(self, screen):
        # Mostrar el mensaje una vez que el jugador haga clic en 'Deal'
        game_texts("The dealer hits on 16 and stands on 17", 575, 25, screen)

        for i in range(2):
            dealer_card = self.deck.deal()
            player_card = self.deck.deal()
        
            if dealer_card is not None:
                self.dealer.add_card(dealer_card)
            if player_card is not None:
                self.player.add_card(player_card)
    
        self.dealer.display_cards()
        self.player.display_cards()
        self.is_cards_dealt = True
        self.player_card = 1
         
        dealer_card = pygame.image.load('img/' + self.dealer.card_img[0] + '.png').convert()
        dealer_card_2 = pygame.image.load('img/back.png').convert()
        player_card = pygame.image.load('img/' + self.player.card_img[0] + '.png').convert()
        player_card_2 = pygame.image.load('img/' + self.player.card_img[1] + '.png').convert()

        game_texts("Dealer's hand is:", 500, 150, screen)
        screen.blit(dealer_card, (400, 200))
        screen.blit(dealer_card_2, (550, 200))
        game_texts("Your's hand is:", 500, 400, screen)
        # Mostrar el valor total del jugador debajo de las cartas
        game_texts(f"Value: {self.player.calc_hand()}", 368, 621, screen)
        screen.blit(player_card, (300, 450))
        screen.blit(player_card_2, (410, 450))
        self.blackjack(screen)
       
       
    def hit(self, screen):
        if not self.is_cards_dealt:
             # Show message to dealt cards first
            game_texts("Please deal the cards first!", 500, 300, screen)
            pygame.display.update()
            time.sleep(0.5) 
            
             # Delete drawing the backgroud on top of this
            pygame.draw.rect(screen, BACKGROUD_COLOR, (250, 280, 500, 40))
            pygame.display.update()
            return
        self.player.add_card(self.deck.deal())
        self.blackjack(screen)
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
            game_finish("You Busted!", 500, 250, RED, screen)
            time.sleep(4)
            self.play_or_exit(screen)
            
        self.player.value = 0

        if self.player_card > 4:
            sys.exit()
            
            
    def stand(self, screen):
        if not self.is_cards_dealt:
                # Mostrar mensaje para que se repartan cartas primero
            game_texts("Please deal the cards first!", 500, 300, screen)
            pygame.display.update()
            time.sleep(0.5)
            pygame.draw.rect(screen, BACKGROUD_COLOR, (250, 280, 500, 40))
            pygame.display.update()
            return

        # Mostrar las cartas del dealer
        screen.blit(pygame.image.load('img/' + self.dealer.card_img[1] + '.png').convert(), (550, 200))

        # Verificar que el dealer siga pidiendo cartas según las reglas
        while self.dealer.calc_hand() <= 16:
            card = self.deck.deal()
            self.dealer.add_card(card)
            self.dealer.display_cards()

        # Actualizar la pantalla con las nuevas cartas
        for i, img in enumerate(self.dealer.card_img[2:], start=2):
            dealer_card = pygame.image.load(f'img/{img}.png').convert()
            screen.blit(dealer_card, (660 + (i - 2) * 110, 200))

        pygame.display.update()

        # Verificar si el dealer se pasó de 21
        if self.dealer.value > 21:
            game_finish("You Won!", 500, 250, GREEN, screen)
        elif self.player.value > self.dealer.value:
            game_finish("You Won!", 500, 250, GREEN, screen)
        elif self.player.value < self.dealer.value:
            game_finish("Dealer Wins!", 500, 250, RED, screen)
        else:
            game_finish("It's a Tie!", 500, 250, GREY, screen)
        
        time.sleep(4)
        self.play_or_exit(screen)    
    
    def play_or_exit(self, screen):
        game_texts("Play again press Deal!", 200, 80, screen)
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
    
    def exit(self, *args):
        sys.exit()