#!/usr/bin/env python3

import re

fname = "calibration.txt"

pattern_single = r"^\w*?(\d{1})\w*?$"
pattern_double = r"^\w*?(\d{1}).*(\d{1})\w*?$"

cal_sum = 0
with open(fname,"r") as file:
    for line in file:
        match = re.search(pattern_double,line)
        if (match):
            cal_val = int(match.group(1)+match.group(2))
        else:
            match = re.search(pattern_single,line)
            if (match):
                cal_val = int(match.group(1)+match.group(1))
        if (match):
            cal_sum += cal_val

print(cal_sum)
