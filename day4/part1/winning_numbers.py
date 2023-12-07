#!/usr/bin/env python3

#fname = "test.txt"
fname = "input.txt"

points = 0
with open(fname,"r") as file:
    for line in file:

        numbers = line.split(":")[1]
        win = numbers.split("|")[0].split()
        own = numbers.split("|")[1].split()

        own_win = [num for num in own if num in win]

        num_win = len(own_win)
        if (num_win>0):
            points += 2**(num_win-1)

print(points)
