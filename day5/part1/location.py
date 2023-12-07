#!/usr/bin/env python3

#fname = "test.txt"
fname = "input.txt"

def apply_maps(seeds,maps):
    """Apply maps to seed ranges."""

    for ii,seed in enumerate(seeds):
        for mp in maps:
            if (seed >= mp[0] and seed < mp[0]+mp[2]):
                seeds[ii] = seed - mp[0] + mp[1]

    return seeds


with open(fname,"r") as file:

    # get seeds
    line = next(file)
    seeds = list(map(int,line.split(": ")[1].split()))
    next(file)

    # workout maps
    while True:

        try:
            next(file)
            line = next(file).strip()
            maps = []
            # create maps
            while(bool(line)):
    
                dst0,src0,length = list(map(int,line.split()))
                maps.append([src0,dst0,length])
    
                line = next(file).strip()
   
            seeds = apply_maps(seeds,maps)
        
        # last line is not empty
        except StopIteration:
            seeds = apply_maps(seeds,maps)
            break

print(min(seeds))
