#!/usr/bin/env python3

#fname = "test.txt"
fname = "input.txt"

with open(fname,"r") as file:
    line = next(file)
    times = list(map(int,line.split(":")[1].split()))
    line = next(file)
    distances = list(map(int,line.split(":")[1].split()))

product = 1
for ii,time in enumerate(times):
    num_wins = 0
    for ct in range(time):
        dst = ct*(time-ct)
        if (dst<=distances[ii]):
            continue
        else:
            num_wins += 1

    product *= num_wins

print(product)
