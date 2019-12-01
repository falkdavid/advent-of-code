#!/usr/bin/env python3
"""
    - Make sure to 'export AOC_SESSION=<your_aoc_token>'
    - Run the script in an ipython session using '%run <name>'
"""

from aocd.models import Puzzle
from typing import NamedTuple, List, Dict
from collections import Counter, defaultdict
import re

# Enter year and day
puzzle = Puzzle(2019, 1)

data = puzzle.input_data
lines = data.split('\n')

######################################################################
#   Part 1
######################################################################

def get_sum_fuel(lines):
    result = 0
    for l in lines:
        mass = int(l)
        result += mass // 3 - 2

    return result

print(get_sum_fuel(lines))
# puzzle.answer_a = get_sum_fuel(lines)


######################################################################
#   Part 2
######################################################################

def get_sum_fuel_2(lines):
    result = 0
    for l in lines:
        mass = int(l)
        fuel = mass // 3 - 2
        while fuel > 0:
            result += fuel
            fuel = fuel // 3 - 2

    return result

assert get_sum_fuel_2([100756]) == 50346
print(get_sum_fuel_2(lines))
# puzzle.answer_b = get_sum_fuel_2(lines)