#!/usr/bin/env python3
"""
    - Make sure to 'export AOC_SESSION=<your_aoc_token>'
    - Run the script in an ipython session using '%run <name>'
"""

from os import RTLD_DEEPBIND
from aocd.models import Puzzle
from typing import NamedTuple, List, Dict
from collections import Counter, defaultdict

# Enter year and day
puzzle = Puzzle(2021, 13)

data = puzzle.input_data
# data = """6,10
# 0,14
# 9,10
# 0,3
# 10,4
# 4,11
# 6,0
# 6,12
# 4,1
# 0,13
# 10,12
# 3,4
# 3,0
# 8,4
# 1,10
# 2,14
# 8,10
# 9,0

# fold along y=7
# fold along x=5"""
points, folds = data.split("\n\n")
points = [list(map(int, l.split(","))) for l in points.split("\n")]
folds = list(map(lambda x: (x[0], int(x[1])), [
             l[11:].split('=') for l in folds.split("\n")]))
P = defaultdict(lambda: False)
for x, y in points:
    P[(x, y)] = True
######################################################################
#   Part 1
######################################################################


def fold_points(P: dict, axis: str, fold: int):
    new_P = P.copy()
    for x, y in P.keys():
        if not P[(x, y)]:
            continue

        new_P[(x, y)] = False
        if axis == 'x' and x > fold:
            new_point = (2*fold - x, y)
        elif axis == 'y' and y > fold:
            new_point = (x, 2*fold - y)
        new_P[new_point] = True

    return new_P


axis, fold = folds[0]
awnser = sum(fold_points(P, axis, fold).values())
print(awnser)
# puzzle.answer_a = awnser


######################################################################
#   Part 2
######################################################################

def print_points(P: dict):
    max_x = max([x for x, y in P.keys() if P[(x, y)]])
    max_y = max([y for x, y in P.keys() if P[(x, y)]])
    for y in range(max_y+1):
        for x in range(max_x+1):
            print('#' if P[(x, y)] else '.', end='')
        print()
    print()


for axis, fold in folds:
    P = fold_points(P, axis, fold)
print_points(P)
# puzzle.answer_b = "FJAHJGAH"
