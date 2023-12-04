#!/usr/bin/env python3

#fname = "test.txt"
fname = "input.txt"

cubes = {"red": 12,"green": 13,"blue": 14}

id_sum = 0
with open(fname,"r") as file:
    for line in file:
        valid = True

        game_name,rounds = line.split(":")

        game_id = game_name.split()[1]
        rounds_list = [map(str.strip,rnd.strip().split(",")) 
                       for rnd in rounds.split(";")]

        for rnd in rounds_list:
            for draw in rnd:
                number = draw.split()[0]
                color = draw.split()[1]
                if (int(number)>cubes[color]):
                    valid = False

        if (valid):
            id_sum += int(game_id)

print(id_sum)



