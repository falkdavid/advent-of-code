#!/usr/bin/env python3
"""
    - Make sure to 'export AOC_SESSION=<your_aoc_token>'
    - Run the script in an ipython session using '%run <name>'
"""

from aocd.models import Puzzle
from typing import NamedTuple, List, Dict
from collections import Counter, defaultdict

# Enter year and day
puzzle = Puzzle(2020, 15)

data = puzzle.input_data
# data = "0,3,6"
numbers = list(map(int, data.split(',')))
######################################################################
#   Part 1
######################################################################

spoken = {}
prev_number = numbers[0]
num = numbers[0]
for i in range(2020):
    if i < len(numbers):
        num = numbers[i]
        spoken[num] = [i+1, i+1]
    else:
        if prev_number not in spoken.keys():
            num = 0
        else:
            num = spoken[prev_number][1] - spoken[prev_number][0]
        if num not in spoken.keys():
            spoken[num] = [i+1, i+1]
        else:
            spoken[num][0] = spoken[num][1]
            spoken[num][1] = i+1

    # print(i+1, num, prev_number, spoken[num], spoken[prev_number])
    prev_number = num


print(num)
# puzzle.answer_a = num


######################################################################
#   Part 2
######################################################################


# puzzle.answer_b =
