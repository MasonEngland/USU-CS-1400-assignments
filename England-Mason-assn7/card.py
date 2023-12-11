# DO NOT CHANGE THIS FILE

from card_utility import RANKS
from card_utility import SUITS


class Card:
    def __init__(self, id):
        self.__id = id

    def get_id(self):
        """
        Return the ID of the card
        """
        return self.__id

    def get_rank(self):
        """
        Return the rank of the card
        """
        return RANKS[self.__id % len(RANKS)]

    def get_suit(self):
        """
        Return the suit of the card
        """
        return SUITS[self.__id // len(RANKS)]

    def __str__(self):
        """
        The string shown when this object is displayed with print()
        """
        return self.get_rank() + " of " + self.get_suit()
