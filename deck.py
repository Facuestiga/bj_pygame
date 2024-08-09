import random
from constants import *

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for value in RANKS:
            for suit in SUITS:
                self.cards.append((value, suit))
  
    def shuffle(self):
        random.shuffle(self.cards)
        

    def deal(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else :
            return None
            