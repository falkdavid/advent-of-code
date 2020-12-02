#!/usr/bin/env python3
"""
    - Make sure to 'export AOC_SESSION=<your_aoc_token>'
    - Run the script in an ipython session using '%run <name>'
"""

from aocd.models import Puzzle
from typing import NamedTuple, List, Dict
from collections import Counter, defaultdict
import re
import itertools

# Enter year and day
puzzle = Puzzle(2020, 2)

data = puzzle.input_data.split('\n')

######################################################################
#   Part 1
######################################################################

result = 0
for x in data:
    pattern, pw = x.split(": ")
    min_, max_, letter = re.search(r'([0-9]+)-([0-9]+) ([a-z])', x).groups()
    c = Counter(pw)
    if c[letter] and int(min_) <= c[letter] <= int(max_):
        result += 1

print(result)
# puzzle.answer_a = result


######################################################################
#   Part 2
######################################################################

result = 0
for x in data:
    pattern, pw = x.split(": ")
    min_, max_, letter = re.search(r'([0-9]+)-([0-9]+) ([a-z])', x).groups()
    if (pw[int(min_)-1] == letter) != (pw[int(max_)-1] == letter):
        result += 1

print(result)
# puzzle.answer_b = 