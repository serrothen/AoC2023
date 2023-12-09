#!/usr/bin/env python3

#fname = "test.txt"
fname = "input.txt"

ext_sum = 0
with open(fname,"r") as file:
    for line in file:
        sequence = list(map(int,line.strip().split()))

        tmp0 = sequence
        is_zero = all([val==0 for val in tmp0])
        last_val = []
        while (not is_zero):
            last_val.append(tmp0[-1])
            # list of differences
            tmp0 = [tmp0[ii+1]-tmp0[ii] for ii in range(len(tmp0)-1)]
            is_zero = all([val==0 for val in tmp0])

        ext_sum += sum(last_val)

print(ext_sum)
