#!/usr/bin/env python3
"""
    - Make sure to 'export AOC_SESSION=<your_aoc_token>'
    - Run the script in an ipython session using '%run <name>'
"""

from aocd.models import Puzzle
from typing import NamedTuple, List, Dict
from collections import Counter, defaultdict

# Enter year and day
puzzle = Puzzle(2020, 6)

data = puzzle.input_data
group_str = data.split("\n\n")


######################################################################
#   Part 1
######################################################################
x = 0

for g in group_str:
  x += len(set(g.replace("\n", "")))

print(x)
  
  
# puzzle.answer_a = 


######################################################################
#   Part 2
######################################################################

x = 0

for g in group_str:
  n = len(g.split("\n"))
  c = Counter(g.replace("\n", ""))
  for value in c.values():
    if value == n:
      x += 1

print(x)

# puzzle.answer_b = 