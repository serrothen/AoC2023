#!/usr/bin/env python3

#fname = "test.txt"
fname = "input.txt"

ext_sum = 0
with open(fname,"r") as file:
    for line in file:
        sequence = list(map(int,line.strip().split()))

        tmp0 = sequence
        is_zero = all([val==0 for val in tmp0])
        first_val = []
        while (not is_zero):
            first_val.append(tmp0[0])
            # list of differences
            tmp0 = [tmp0[ii+1]-tmp0[ii] for ii in range(len(tmp0)-1)]
            is_zero = all([val==0 for val in tmp0])

        # expanding subsequent subtractions
        ext_sum += sum(first_val[::2]) - sum(first_val[1::2])

print(ext_sum)
