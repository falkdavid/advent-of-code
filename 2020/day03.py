#!/usr/bin/env python3
"""
    - Make sure to 'export AOC_SESSION=<your_aoc_token>'
    - Run the script in an ipython session using '%run <name>'
"""

from aocd.models import Puzzle
from typing import NamedTuple, List, Dict
from collections import Counter, defaultdict

# Enter year and day
puzzle = Puzzle(2020, 3)

data = puzzle.input_data
lines = data.split('\n')

height = len(lines)
width = len(lines[0])
######################################################################
#   Part 1
######################################################################
x = 0

trees = 0
for l in lines:
    c = l[x % width]
    if c == '#':
        trees += 1
    x += 3

print(trees)
# puzzle.answer_a = trees


######################################################################
#   Part 2
######################################################################

dd = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]


result = 1
for dx, dy in dd:
    y = 0
    x = 0

    trees = 0
    for y in range(0, len(lines), dy):
        l = lines[y]
        c = l[x % width]
        if c == '#':
            trees += 1
        x += dx

    result *= trees

print(result)
# puzzle.answer_b = 