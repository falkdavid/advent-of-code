#!/usr/bin/env python3
"""
    - Make sure to 'export AOC_SESSION=<your_aoc_token>'
    - Run the script in an ipython session using '%run <name>'
"""

from aocd.models import Puzzle
from typing import NamedTuple, List, Dict
from collections import Counter, defaultdict
from statistics import median

# Enter year and day
puzzle = Puzzle(2021, 7)

data = puzzle.input_data
num = [int(x) for x in data.split(",")]
######################################################################
#   Part 1
######################################################################

def get_fuel(nums, y):
    return sum([abs(y - x) for x in nums])
    
awnser_a = get_fuel(num, int(median(num)))
print(awnser_a)
# puzzle.answer_a = awnser_a


######################################################################
#   Part 2
######################################################################
mean = int(round(sum(num)/len(num)))

def get_fuel2(nums, y):
    return sum([int((abs(y - x) + 1) * (abs(y - x)/2)) for x in nums])

awnser_b = min([get_fuel2(num, y) for y in [mean-1, mean+1]])
print(awnser_b)
# puzzle.answer_b = awnser_b