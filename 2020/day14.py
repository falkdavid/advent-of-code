#!/usr/bin/env python3
"""
    - Make sure to 'export AOC_SESSION=<your_aoc_token>'
    - Run the script in an ipython session using '%run <name>'
"""

from aocd.models import Puzzle
from typing import NamedTuple, List, Dict
from collections import Counter, defaultdict
from itertools import combinations, permutations
import re
# Enter year and day
puzzle = Puzzle(2020, 14)

data = puzzle.input_data
lines = data.split('\n')
######################################################################
#   Part 1
######################################################################


def apply_mask(mask, value):
    output = value
    mask_or = int(mask.replace('X', '0'), 2)
    mask_and = int(mask.replace('X', '1'), 2)

    output = output | mask_or
    output = output & mask_and

    return output


mem = {}
current_mask = "X"*34
for l in lines:
    if l.startswith("mask"):
        current_mask = l.split('=')[1].strip()
    else:
        loc, val = re.search(r'mem\[(\d+)\] = (\d+)', l).groups()
        mem[int(loc)] = apply_mask(current_mask, int(val))

res = sum(mem.values())
print(res)
# puzzle.answer_a = res


######################################################################
#   Part 2
######################################################################

def get_adresses(mask, adr):
    out_adr = adr
    mask_or = int(mask.replace('X', '0'), 2)
    out_adr = out_adr | mask_or

    outs = []
    floats = [len(mask)-(i+1) for i, c in enumerate(mask) if c == 'X']
    # print(floats, out_adr)
    for i in range(len(floats)+1):
        for c in combinations(floats, i):
            inv = [x for x in floats if x not in c]
            out = out_adr
            for x in c:
                out |= (1 << x)

            for x in inv:
                out &= ~(1 << x)

            outs.append(out)

    return outs


# print(get_adresses("000000000000000000000000000000X1001X", 42))

mem = {}
current_mask = "X"*34
for l in lines:
    if l.startswith("mask"):
        current_mask = l.split('=')[1].strip()
    else:
        loc, val = re.search(r'mem\[(\d+)\] = (\d+)', l).groups()
        for a in get_adresses(current_mask, int(loc)):
          mem[a] = int(val)


res = sum(mem.values())
print(res)

# puzzle.answer_b = res
