# DO NOT CHANGE THIS FILE

SUITS = [
    "Hearts",
    "Diamonds",
    "Spades",
    "Clubs",
]

RANKS = [
    "Ace",
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
    "Jack",
    "Queen",
    "King",
]


def get_id_from_indices(rank_index, suit_index):
    return suit_index * len(RANKS) + rank_index
