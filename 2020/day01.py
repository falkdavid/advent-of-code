#!/usr/bin/env python3
"""
    - Make sure to 'export AOC_SESSION=<your_aoc_token>'
    - Run the script in an ipython session using '%run <name>'
"""

from aocd.models import Puzzle
from typing import NamedTuple, List, Dict
from collections import Counter, defaultdict

# Enter year and day
puzzle = Puzzle(2020, 1)

data = list(map(int, puzzle.input_data.split()))

######################################################################
#   Part 1
######################################################################

result = 0
for x in data:
    for y in data:
        if x+y == 2020:
            result = x*y
            break
        
print(result)
# puzzle.answer_a = result


######################################################################
#   Part 2
######################################################################

for x in data:
    for y in data:
        for z in data:
            if x+y+z == 2020:
                result = x*y*z

print(result)
# puzzle.answer_b = result