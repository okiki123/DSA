# Alice has some cards with numbers written on them. 
# She arranges the cards in decreasing order, and lays them out face down in a sequence on a table. 
# She challenges Bob to pick out the card containing a given number by turning over as few cards as possible. 
# Write a function to help Bob locate the card.

# Brute Force Approach
def locate_position(cards, query):
    position = 0
    while position < len(cards):
        if cards[position] == query:
            return position
        position += 1
    return -1

# Using Binary Search Algorithm
def locate_position(cards, query):
    lo = 0
    hi = len(cards) - 1
    while lo <= hi:
        mid = (lo + hi) / 2
        mid_number = cards[mid]
        if mid_number == query:
            return mid
        elif mid_number < query:
            hi = mid - 1
        elif mid_number > query:
            lo = mid + 1
    return -1

