#!/usr/bin/env python3

from collections import deque

#fname = "test.txt"
fname = "input.txt"

num_cards = 0
cards = deque([0])
with open(fname,"r") as file:
    for line in file:

        card = line.split(":")[0]
        numbers = line.split(":")[1]
        win = numbers.split("|")[0].split()
        own = numbers.split("|")[1].split()

        own_win = [num for num in own if num in win]

        # current card
        num_cards += 1

        # won copies of current card
        if (len(cards)>0):
            num_copies = cards.popleft()
            num_cards += num_copies 
        else:
            num_copies = 0

        # won copies of future cards
        for ii in range(len(own_win)):
            if (ii<len(cards)):
                cards[ii] += 1+num_copies
            else:
                cards.append(1+num_copies)

print(num_cards)
