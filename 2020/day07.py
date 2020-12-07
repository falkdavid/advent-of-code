#!/usr/bin/env python3
"""
    - Make sure to 'export AOC_SESSION=<your_aoc_token>'
    - Run the script in an ipython session using '%run <name>'
"""

from aocd.models import Puzzle
from typing import NamedTuple, List, Dict
from collections import Counter, defaultdict

# Enter year and day
puzzle = Puzzle(2020, 7)

data = puzzle.input_data
lines = data.split("\n")
######################################################################
#   Part 1
######################################################################

D = {}

for l in lines:
  key,rest = l.split("bags contain")
  values = rest.split(',')
  key = key.strip()
  
  D[key] = []
  for v in values:
    if v != " no other bags.":
      n, col1, col2, _rest = v.strip().split(' ')
      D[key].append((n, " ".join([col1, col2])))


print(D)
# puzzle.answer_a = 


######################################################################
#   Part 2
######################################################################


# puzzle.answer_b = 