#!/usr/bin/env python3
"""
    - Make sure to 'export AOC_SESSION=<your_aoc_token>'
    - Run the script in an ipython session using '%run <name>'
"""

from aocd.models import Puzzle
from typing import NamedTuple, List, Dict
from collections import Counter, defaultdict
from itertools import combinations

# Enter year and day
puzzle = Puzzle(2020, 9)

data = list(map(int, puzzle.input_data.split('\n')))
######################################################################
#   Part 1
######################################################################

res = 0
for i, n in enumerate(data[25:]):
    pos_ns = set(map(sum, combinations(data[i:i+25], 2)))
    if n not in pos_ns:
        res = n
        break

print(res)
# puzzle.answer_a = res


######################################################################
#   Part 2
######################################################################

found = False
goal = res
i = data.index(res)
j = i - 1
while i > 0 and j > 0 and not found:
    s = sum(data[j:i])
    if s > goal:
        i -= 1
        j = i - 1
        continue
    elif s < goal:
        j -= 1
        continue
    else:
        found = True

res2 = min(data[j:i]) + max(data[j:i])
print(res2)
# puzzle.answer_b = res2