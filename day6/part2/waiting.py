#!/usr/bin/env python3

import math

def dst(x,time,distance):
    """Difference between own distance and record distance."""

    return x**2 - time*x + distance

def bisection(time,distance,lower,higher,tol=1e-6):
    """
    Bisection to find which charge time was
    used to reach the record distance.
    """

    dst_l = dst(lower,time,distance)
    dst_u = dst(higher,time,distance)

    # root at boundary
    if (abs(dst_l)<tol):
        return lower
    if (abs(dst_u)<tol):
        return higher

    # no root
    if (dst_l*dst_u > 0):
        print(f"No root in interval [{lower},{higher}].")

    # bisection
    if (dst_l*dst_u < 0):

        while (abs(higher-lower)>tol):

            # evaluate function at center
            middle = (lower+higher)/2.0
            dst_m = dst(middle,time,distance)
       
            # move boundaries surrounding root
            if (dst_m*dst_l>0):
                lower = middle
            else:
                higher = middle

        return middle


#fname = "test.txt"
fname = "input.txt"

with open(fname,"r") as file:
    line = next(file)
    time = int(line.split(":")[1].strip())
    line = next(file)
    distance = int(line.split(":")[1].strip())

# charge time for record distance
lower = 0
higher = int(time/2.0)
root = bisection(time,distance,lower,higher)
int_root = math.floor(root)

# low charging time above floor 
# high charging time below ceil: subtract -1
print(time-2*int_root-1)
