#!/usr/bin/env python3

from collections import defaultdict
from functools import reduce

def lookaround(loc,view,is_part):
    """Check surrounding symbols."""

    coord = [-1,-1]
    try: 
        if (view[0][loc-1]=="*"):
            is_part = True
            coord = [loc-1,0]
        if (view[1][loc-1]=="*"):
            is_part = True
            coord = [loc-1,1]
        if (view[2][loc-1]=="*"):
            is_part = True
            coord = [loc-1,2]
    except IndexError:
        print("left edge")
    
    if (view[0][loc]=="*"):
        is_part = True
        coord = [loc,0]
    if (view[2][loc]=="*"):
        is_part = True
        coord = [loc,2]
    
    try:
        if (view[0][loc+1]=="*"):
            is_part = True
            coord = [loc+1,0]
        if (view[1][loc+1]=="*"):
            is_part = True
            coord = [loc+1,1]
        if (view[2][loc+1]=="*"):
            is_part = True
            coord = [loc+1,2]
    except IndexError:
        print("right edge")

    return is_part,coord


def print_contrib(loc,view,contrib):
    """Print parts and their environment."""

    lc = len(contrib)
    # top row
    try:
        print(view[0][loc-lc-1],end="")
    except IndexError:
        print("left edge")
    print(view[0][loc-lc:loc],end="")
    try:
        print(view[0][loc],end="")
    except IndexError:
        print("right edge")
    print()

    # center row
    try:
        print(view[1][loc-lc-1],end="")
    except IndexError:
        print("left edge")
    print(contrib,end="")
    try:
        print(view[1][loc],end="")
    except IndexError:
        print("right edge")
    print()

    # bottom row
    try:
        print(view[2][loc-lc-1],end="")
    except IndexError:
        print("left edge")
    print(view[2][loc-lc:loc],end="")
    try:
        print(view[2][loc],end="")
    except IndexError:
        print("right edge")
    print()
    print()


def scan_line(view,gears,line_index):
    """Scan line for parts."""

    is_part = False
    number = []
    for ii,symbol in enumerate(view[1]):

        if (symbol.isnumeric()):
            number.append(symbol)
            if (not is_part):
                is_part,coord = lookaround(ii,view,is_part)
                coord[1]+=line_index-1
        else:
            if (is_part):

                gears[f"{*coord,}"].append(int("".join(number)))
#                print_contrib(ii,view,"".join(number))
            is_part = False
            number = []

    if (is_part):
        gears[f"{*coord,}"].append(int("".join(number)))
#        print_contrib(ii,view,"".join(number))

#    print()

    return gears


#fname = "test.txt"
fname = "input.txt"

line_index = 0
gears = defaultdict(list)
view = []
with open(fname,"r") as file:

    # first line
    line = next(file)
    view.append("."*len(line))
    view.append(line.strip())
    line = next(file)
    view.append(line.strip())

    gears = scan_line(view,gears,line_index)
    line_index += 1


    # center line
    for line in file:
        view[0] = view[1]
        view[1] = view[2]
        view[2] = line.strip()

        gears = scan_line(view,gears,line_index)
        line_index += 1
        

    # last line
    view[0] = view[1]
    view[1] = view[2]
    view[2] = "."*len(view[1])

    gears = scan_line(view,gears,line_index)

gear_sum = sum([reduce(lambda x,y: x*y,gear) \
                for gear in gears.values() if len(gear)>1])

print(gear_sum)
