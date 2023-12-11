# DO NOT CHANGE THIS FILE

from deck import Deck
from time import sleep
from card_utility import SUITS, RANKS, get_id_from_indices
from search_and_sort import insertion_sort, selection_sort, bubble_sort, linear_search, binary_search


# Set this to a lower value to speed up your testing
SLEEP_TIME = 0.5


def main():
    print("""\
  Welcome to the Deckinator!
 _____           _____
|Q  ww|  _____  |7    |  _____
| ^ {(| |4    | | o o | |A .  |
|(.)%%| | v v | |o o o| | /.\ |
| |%%%| |     | | o o | |(_._)|
|_%%%O| | v v | |____L| |  |  |
        |____h|         |____V|
""")

    # Deal a new hand of cards to the player
    player_hand = new_hand()

    done = False

    # Program Loop
    while not done:
        # Display the menu
        print("What would you like to do? ")
        print("\t1) Show Hand")
        print("\t2) Sort Hand by Rank")  # Do insertion sort
        print("\t3) Sort Hand by Suit")  # Do selection sort
        print("\t4) Linear Search")
        print("\t5) Binary Search")  # Use bubble sort first
        print("\t6) Deal New Hand")
        print("\t7) Quit")
        selection = int(input("Choose an option: "))

        # Process the menu selection
        if selection == 1:
            print_hand(player_hand)
        elif selection == 2:
            thinking("\tPerforming Insertion Sort")
            insertion_sort(player_hand)
        elif selection == 3:
            thinking("\tPerforming Selection Sort")
            selection_sort(player_hand)
        elif selection == 4:
            card_id = search_selection_menu()
            thinking("\tPerforming Linear Search")
            linear_search(player_hand, card_id)
        elif selection == 5:
            thinking("\tPerforming Bubble Sort")
            bubble_sort(player_hand)
            card_id = search_selection_menu()
            thinking("\tPerforming Binary Search")
            binary_search(player_hand, card_id)
        elif selection == 6:
            player_hand = new_hand()
        elif selection == 7:
            done = True

    print("Thanks for playing Deckinator")


# Deal a new hand of 10 cards
def new_hand():
    thinking("Shuffling")
    deck = Deck()
    thinking("Dealing Hand")
    tmp_hand = []

    # Deal 10 cards from the deck
    for i in range(10):
        tmp_hand.append(deck.draw())

    return tmp_hand


# Display the search selection menu
# Return the id of the card that will match the selected options
def search_selection_menu():
    print("Select a card to search for")
    rank_index = rank_selection_menu()
    suit_index = suit_selection_menu()

    print("\tSearching for the " + RANKS[rank_index] + " of " + SUITS[suit_index])

    return get_id_from_indices(rank_index, suit_index)


# Display a menu to choose a suit
# Return the index value of the suit selected
def suit_selection_menu():
    for i in range(len(SUITS)):
        print("\t" + str(i + 1) + ") " + SUITS[i])

    return int(input("Choose a Suit: ")) - 1


# Display a menu to choose a rank
# Return the index value of the rank selected
def rank_selection_menu():
    for i in range(len(RANKS)):
        print("\t" + str(i + 1) + ") " + RANKS[i])

    return int(input("Choose a Rank: ")) - 1


# Display the hand
def print_hand(hand):
    for i in range(len(hand)):
        print(str(i) + ".\t" + str(hand[i]))
    print()


# Display a thinking message
def thinking(msg):
    print(msg, end="", flush=True)
    for i in range(3):
        print(".", end="", flush=True)
        sleep(SLEEP_TIME)
    print("\n")


main()
