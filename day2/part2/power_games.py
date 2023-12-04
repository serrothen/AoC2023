#!/usr/bin/env python3

from functools import reduce

#fname = "test.txt"
fname = "input.txt"


power_sum = 0
with open(fname,"r") as file:
    for line in file:
        cubes = {"red": 0,"green": 0,"blue": 0}

        game_name,rounds = line.split(":")

        game_id = game_name.split()[1]
        rounds_list = [map(str.strip,rnd.strip().split(",")) 
                       for rnd in rounds.split(";")]

        for rnd in rounds_list:
            for draw in rnd:
                number = draw.split()[0]
                color = draw.split()[1]
                if (int(number)>cubes[color]):
                    cubes[color] = int(number)

        power = reduce(lambda x,y: x*y, cubes.values())

        power_sum += power

print(power_sum)



