#!/usr/bin/env python3
"""
    - Run the script in an ipython session using '%run <name>'
    - Make sure to 'export AOC_SESSION=<your_aoc_token>'
"""

from aocd.models import Puzzle
from collections import Counter
from typing import List

# https://adventofcode.com/2016/day/6
puzzle = Puzzle(2016, 6)

data = puzzle.input_data
lines = data.split('\n')
######################################################################
#   Part 1
######################################################################

def get_columns(lines: List[str]) -> List[str]:
    return ["".join(lines[row][col] for row in range(len(lines)))
                                    for col in range(len(lines[0]))]

def get_most_common_in_column(cols: List[str]) -> str:
    return "".join([m[0] for c in cols for m in Counter(c).most_common(1)])

test_data = """eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar""".split('\n')

assert get_most_common_in_column(get_columns(test_data)) == "easter"

columns = get_columns(lines)
print(get_most_common_in_column(columns))

# puzzle.answer_a = get_most_common_in_column(columns)


######################################################################
#   Part 2
######################################################################

def get_least_common_in_column(cols: List[str]) -> str:
    return "".join([sorted(Counter(c).most_common(), 
                           key=lambda x: x[1])[0][0] 
                           for c in cols])

assert get_least_common_in_column(get_columns(test_data)) == "advent"
print(get_least_common_in_column(columns))

# puzzle.answer_b = get_least_common_in_column(columns)