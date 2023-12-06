#!/usr/bin/env python3

def lookaround(loc,view,is_part):
    """Check surrounding symbols."""

    try: 
        if (view[0][loc-1]!="." and not view[0][loc-1].isnumeric()):
            is_part = True
        elif (view[1][loc-1]!="." and not view[1][loc-1].isnumeric()):
            is_part = True
        elif (view[2][loc-1]!="." and not view[2][loc-1].isnumeric()):
            is_part = True
    except IndexError:
        print("left edge")
    
    if (view[0][loc]!="." and not view[0][loc].isnumeric()):
        is_part = True
    elif (view[2][loc]!="." and not view[2][loc].isnumeric()):
        is_part = True
    
    try:
        if (view[0][loc+1]!="." and not view[0][loc+1].isnumeric()):
            is_part = True
        elif (view[1][loc+1]!="." and not view[1][loc+1].isnumeric()):
            is_part = True
        elif (view[2][loc+1]!="." and not view[2][loc+1].isnumeric()):
            is_part = True
    except IndexError:
        print("right edge")

    return is_part


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


def scan_line(view,part_sum):
    """Scan line for parts."""

    is_part = False
    number = []
    for ii,symbol in enumerate(view[1]):

        if (symbol.isnumeric()):
            number.append(symbol)
            if (not is_part):
                is_part = lookaround(ii,view,is_part)
        else:
            if (is_part):
                part_sum += int("".join(number))
#                print_contrib(ii,view,"".join(number))
            is_part = False
            number = []

    if (is_part):
        part_sum += int("".join(number))
#        print_contrib(ii,view,"".join(number))

#    print()

    return part_sum


#fname = "test.txt"
fname = "input.txt"

part_sum = 0
view = []
with open(fname,"r") as file:

    # first line
    line = next(file)
    view.append("."*len(line))
    view.append(line.strip())
    line = next(file)
    view.append(line.strip())

    part_sum = scan_line(view,part_sum)


    # center line
    for line in file:
        view[0] = view[1]
        view[1] = view[2]
        view[2] = line.strip()

        part_sum = scan_line(view,part_sum)
        

    # last line
    view[0] = view[1]
    view[1] = view[2]
    view[2] = "."*len(view[1])

    part_sum = scan_line(view,part_sum)

print(part_sum)
