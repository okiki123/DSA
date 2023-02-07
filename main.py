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

# List/Arrays in Python
stock_prices = [298, 305, 320, 301, 292]

#Lookup by index = o(1)

def check_number(stock_prices):
    for i in range(len(stock_prices)):
        if stock_prices[i] == 301:
            return i

#Lookup by value = o(n)

max = int(input('Enter your number'))

odd_number = []

for i in range(1, max):
    if i % 2 == 1:
        odd_number.append(i)
        