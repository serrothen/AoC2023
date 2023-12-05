#!/usr/bin/env python3

fname = "test.txt"
#fname = "input.txt"

part_sum = 0
view = []
with open(fname,"r") as file:
    line = next(file)
    view.append(line)
    line = next(file)
    view.append(line)
    # upper left corner
    if (symbol.isnumeric()):
        if (view[0][1]!="." and not view[0][1].isnumeric()):
            part_sum += int(symbol)
        elif (view[1][0]!="." and not view[1][0].isnumeric()):
            part_sum += int(symbol)
        elif (view[1][1]!="." and not view[1][1].isnumeric()):
            part_sum += int(symbol)
    # upper edge
    for ii,symbol in enumerate(view[0][1:-1]):
        if (symbol.isnumeric()):
            if (view[0][ii-1]!="." and not view[0][ii-1].isnumeric()):
                part_sum += int(symbol)
            elif (view[0][ii+1]!="." and not view[0][ii+1].isnumeric()):
                part_sum += int(symbol)
            elif (view[1][ii-1]!="." and not view[1][ii-1].isnumeric()):
                part_sum += int(symbol)
            elif (view[1][ii]!="." and not view[1][ii].isnumeric()):
                part_sum += int(symbol)
            elif (view[1][ii+1]!="." and not view[1][ii+1].isnumeric()):
                part_sum += int(symbol)
    # upper right corner
    if (symbol.isnumeric()):
        if (view[0][-2]!="." and not view[0][-2].isnumeric()):
            part_sum += int(symbol)
        elif (view[1][-1]!="." and not view[1][-1].isnumeric()):
            part_sum += int(symbol)
        elif (view[1][-2]!="." and not view[1][-2].isnumeric()):
            part_sum += int(symbol)
    line = next(file)
    view.append(line)
    # left edge
    if (symbol.isnumeric()):
        if (view[0][0]!="." and not view[0][0].isnumeric()):
            part_sum += int(symbol)
        elif (view[0][1]!="." and not view[0][1].isnumeric()):
            part_sum += int(symbol)
        elif (view[1][1]!="." and not view[1][1].isnumeric()):
            part_sum += int(symbol)
        elif (view[2][0]!="." and not view[2][0].isnumeric()):
            part_sum += int(symbol)
        elif (view[2][1]!="." and not view[2][i1].isnumeric()):
            part_sum += int(symbol)
    
    # center
    for ii,symbol in enumerate(view[1][1:-1]):
        if (symbol.isnumeric()):
            if (view[0][ii-1]!="." and not view[0][ii-1].isnumeric()):
                part_sum += int(symbol)
            elif (view[0][ii]!="." and not view[0][ii].isnumeric()):
                part_sum += int(symbol)
            elif (view[0][ii+1]!="." and not view[1][ii+1].isnumeric()):
                part_sum += int(symbol)
            elif (view[1][ii-1]!="." and not view[1][ii-1].isnumeric()):
                part_sum += int(symbol)
            elif (view[1][ii+1]!="." and not view[1][ii+1].isnumeric()):
                part_sum += int(symbol)
            elif (view[2][ii-1]!="." and not view[2][ii-1].isnumeric()):
                part_sum += int(symbol)
            elif (view[2][ii]!="." and not view[2][ii].isnumeric()):
                part_sum += int(symbol)
            elif (view[2][ii+1]!="." and not view[2][ii+1].isnumeric()):
                part_sum += int(symbol)
    # right edge
    for ii,symbol in enumerate(view[1][1:-1]):
        if (view[0][-2]!="." and not view[0][-2].isnumeric()):
            part_sum += int(symbol)
        elif (view[0][-1]!="." and not view[0][-1].isnumeric()):
            part_sum += int(symbol)
        elif (view[1][-2]!="." and not view[1][-2].isnumeric()):
            part_sum += int(symbol)
        elif (view[2][-2]!="." and not view[2][-2].isnumeric()):
            part_sum += int(symbol)
        elif (view[2][-1]!="." and not view[2][-1].isnumeric()):
            part_sum += int(symbol)
    
     for line in file:
         view[0] = view[1]
         view[1] = view[2]
         view[2] = line
    
         for ii,symbol in enumerate(view[1][1:-1]):
             if (symbol.isnumeric()):
                 if (view[0][ii-1]!="." and not view[0][ii-1].isnumeric()):
                     part_sum += int(symbol)
                 elif (view[0][ii]!="." and not view[0][ii].isnumeric()):
                     part_sum += int(symbol)
                 elif (view[0][ii+1]!="." and not view[0][ii+1].isnumeric()):
                     part_sum += int(symbol)
                 elif (view[1][ii-1]!="." and not view[1][ii-1].isnumeric()):
                     part_sum += int(symbol)
                 elif (view[1][ii+1]!="." and not view[1][ii+1].isnumeric()):
                     part_sum += int(symbol)
                 elif (view[2][ii-1]!="." and not view[2][ii-1].isnumeric()):
                     part_sum += int(symbol)
                 elif (view[2][ii]!="." and not view[2][ii].isnumeric()):
                     part_sum += int(symbol)
                 elif (view[2][ii+1]!="." and not view[2][ii+1].isnumeric()):
                     part_sum += int(symbol)
    
    # lower edge
    for ii,symbol in enumerate(view[2][1:-1]):
        if (symbol.isnumeric()):
            if (view[2][ii-1]!="." and not view[2][ii-1].isnumeric()):
                part_sum += int(symbol)
            elif (view[2][ii+1]!="." and not view[2][ii+1].isnumeric()):
                part_sum += int(symbol)
            elif (view[1][ii-1]!="." and not view[1][ii-1].isnumeric()):
                part_sum += int(symbol)
            elif (view[1][ii]!="." and not view[1][ii].isnumeric()):
                part_sum += int(symbol)
            elif (view[1][ii+1]!="." and not view[1][ii+1].isnumeric()):
                part_sum += int(symbol)
