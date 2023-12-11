# DO NOT CHANGE THIS FILE

import random
from card import Card
from card_utility import RANKS
from card_utility import SUITS


class Deck:
    def __init__(self):
        self.shuffle()

    # Call to create a brand new shuffled deck of cards
    # Creates a deck based on RANKS and SUITS so there is a unique card for every
    # possible combination of RANK and SUIT
    def shuffle(self):
        self.__deck = []
        for i in range(len(RANKS) * len(SUITS)):
            self.__deck.append(Card(i))

        # Uncomment these lines if you want to see the id values with associated Rank and Suit before shuffling
        # for i in range(len(self.__deck)):
        #     print(i, self.__deck[i])

        random.shuffle(self.__deck)

    # Deal a single card from the top of the deck
    def draw(self):
        return self.__deck.pop()
