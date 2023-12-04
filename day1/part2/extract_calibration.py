#!/usr/bin/env python3

import re

#fname = "test.txt"
fname = "calibration.txt"

pattern_single = r"^\w*?(\d{1})\w*?$"
pattern_double = r"^\w*?(\d{1}).*(\d{1})\w*?$"

words = {"one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"}

cal_sum = 0
with open(fname,"r") as file:
    for line in file:

        # match words
        word_dict_front = {line.index(word):words[word] 
                           for word in words.keys() if word in line}
        word_dict_back = {len(line)-line[::-1].index(word[::-1])-len(word):words[word] 
                          for word in words.keys() if word in line}
        word_dict = {**word_dict_front,**word_dict_back}

        # match digits
        match = re.search(pattern_double,line)
        if (match):
            digit_dict = {match.start(1):match.group(1),match.start(2):match.group(2)}
        else:
            match = re.search(pattern_single,line)
            if (match):
                digit_dict = {match.start(1):match.group(1),match.start(1):match.group(1)}
            else:
                digit_dict = {}

        # first, laste entry
        idx1 = len(line)+1
        idx2 = -1
        if (word_dict):
            idx1 = min(idx1,*word_dict.keys())
            idx2 = max(idx2,*word_dict.keys())

        if (digit_dict):
            idx1 = min(idx1,*digit_dict.keys())
            idx2 = max(idx2,*digit_dict.keys())

        # value of first, last entry
        if (idx1 in word_dict.keys()):
            digit1 = word_dict[idx1]
        else:
            digit1 = digit_dict[idx1]

        if (idx2 in word_dict.keys()):
            digit2 = word_dict[idx2]
        else:
            digit2 = digit_dict[idx2]

        cal_val = int(digit1+digit2)
        cal_sum += cal_val

print(cal_sum)
