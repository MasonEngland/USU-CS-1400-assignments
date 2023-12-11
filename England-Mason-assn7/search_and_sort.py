# Mason England 
# CS 1400 MWF - 8:30 AMx
# You may change this file

from card_utility import SUITS, RANKS, get_id_from_indices


def insertion_sort(card_list):
    """
    Perform an insertion sort by Card rank
    """
    for i in range(0, len(card_list)):
        curr_element = card_list[i]
        j = i - 1
        while j >= 0 and RANKS.index(card_list[j].get_rank()) > RANKS.index(curr_element.get_rank()):
            card_list[j + 1] = card_list[j]
            j -= 1

        card_list[j + 1] = curr_element

    print("\tInsertion Sort done\n")


def selection_sort(card_list):
    """
    Perform a selection sort by Card suit
    """
    for i in range(len(card_list) - 1):
        curr_min_index = i

        for j in range(i + 1, len(card_list)):
            if SUITS.index(card_list[curr_min_index].get_suit()) > SUITS.index(card_list[j].get_suit()):
                curr_min_index = j

        if curr_min_index != i:
            card_list[i], card_list[curr_min_index] = card_list[curr_min_index], card_list[i]

    print("\tSelection Sort done\n")


def bubble_sort(card_list):
    """
    Perform a bubble sort by Card ID
    """
    did_swap = True
    while did_swap:
        did_swap = False

        for i in range(len(card_list) - 1):
            if card_list[i].get_id() > card_list[i + 1].get_id():
                card_list[i], card_list[i + 1] = card_list[i + 1], card_list[i]
                did_swap = True


    print("\tBubble Sort done\n")


def linear_search(card_list, card_id):
    """
    Perform a LINEAR search on a list of Cards,
    identifying a match by the Card's ID

    If the Card is found, print its index in the list
    Print an approprate message if the Card is not found
    """
    for i in range(len(card_list)):
        if card_id == card_list[i].get_id():
            print("Your card is at index " + str(i) + "\n")
            return
    print("Your card was not found\n")


def binary_search(card_list, card_id):
    """
    Perform a BINARY search on a list of Cards,
    identifying a match by the Card's ID

    If the Card is found, print its index in the list
    Print an approprate message if the Card is not found
    """
    low = 0
    high = len(card_list) - 1
    while high >= low:
        mid = (high + low) // 2
        if card_id == card_list[mid].get_id():
            print("Your card is at index " + str(mid) + "\n")
            return
        elif card_id < card_list[mid].get_id():
            high = mid - 1
        elif card_id > card_list[mid].get_id():
            low = mid + 1
    print("Your card was not found\n")
