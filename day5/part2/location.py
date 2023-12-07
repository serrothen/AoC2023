#!/usr/bin/env python3

#fname = "test.txt"
fname = "input.txt"

def apply_maps(seed_ranges,maps):
    """Apply maps to seed ranges."""

    # apply maps to ranges
    seed_ranges_new = []
    seed_ranges_mapped_old = []
    seed_ranges_mapped_new = []
    for sr in seed_ranges:
        for mp in maps:
            # sr contains lower or upper boundary of mp
            # sr is inside mp
            if ((sr[0] <= mp[0] and sr[1] >= mp[0]) or 
                (sr[0] <= mp[0]+mp[2]-1 and sr[1] >= mp[0]+mp[2]-1) or
                (sr[0] >= mp[0] and sr[1] <= mp[0]+mp[2]-1)):
    
                # apply mapping
                tmp = [max(sr[0],mp[0]), min(sr[1],mp[0]+mp[2]-1)]
                seed_ranges_new.append([entry-mp[0]+mp[1] for entry in tmp])
    
                # memorize mapped ranges with old and new borders
                seed_ranges_mapped_new.append(tmp)
                seed_ranges_mapped_old.append(sr)
    
    # keep parts of ranges without maps
    seed_ranges_mapped_new.sort()
    for sr in seed_ranges:
    
        # non-mapped parts
        if (sr not in seed_ranges_mapped_old):
            seed_ranges_new.append(sr)
            continue
    
        lower_sr = sr[0]
        for srm in seed_ranges_mapped_new:
    
            # detect gaps between mapped parts and non-mapped parts
            if (lower_sr < srm[0] and sr[0]<=lower_sr and sr[1]>=srm[0]-1):
                tmp = [lower_sr,srm[0]-1]
                seed_ranges_new.append(tmp)
            lower_sr = srm[1]+1
    
        # detect gap behind all mapped parts
        if (lower_sr > sr[0] and lower_sr < sr[1]):
            tmp = [lower_sr,sr[1]]
            seed_ranges_new.append(tmp)
    
    return seed_ranges_new


with open(fname,"r") as file:

    # get seed ranges
    line = next(file)
    seed_line = list(map(int,line.split(": ")[1].split()))
    seed_ranges = [[seed_line[ii],seed_line[ii]+seed_line[ii+1]-1]
                   for ii in range(0,len(seed_line),2)]
    seed_ranges.sort()
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

            seed_ranges = apply_maps(seed_ranges,maps)
   

        # last line is not empty
        except StopIteration:
            seed_ranges = apply_maps(seed_ranges,maps)
            break

print(min(seed_ranges)[0])
