#!/usr/bin/env python3
"""
    - Make sure to 'export AOC_SESSION=<your_aoc_token>'
    - Run the script in an ipython session using '%run <name>'
"""

from aocd.models import Puzzle
from typing import NamedTuple, List, Dict
from collections import Counter, defaultdict

# Enter year and day
puzzle = Puzzle(2021, 5)

data = puzzle.input_data
lines = data.split('\n')
LS = [[tuple(map(int, c.split(','))) for c in l.split(" -> ")] for l in lines]
######################################################################
#   Part 1
######################################################################

P = defaultdict(int)


def bidi_range(start, end):
    return range(start, end + 1) if start <= end else range(
        start, end - 1, -1)


def iter_points_on_seg(seg):
    ((x1, y1), (x2, y2)) = seg
    if x1 == x2:
        ys = bidi_range(y1, y2)
        for y in ys:
            yield x1, y
    if y1 == y2:
        xs = bidi_range(x1, x2)
        for x in xs:
            yield x, y1
    if abs(x1 - x2) == abs(y1 - y2):
        xs = bidi_range(x1, x2)
        ys = bidi_range(y1, y2)

        for x, y in zip(xs, ys):
            yield x, y


for s in LS:
    if s[0][0] == s[1][0] or s[0][1] == s[1][1]:
        for p in iter_points_on_seg(s):
            P[p] += 1

result = 0
for k, v in P.items():
    if v > 1:
        result += 1

print(result)
# puzzle.answer_a = result


######################################################################
#   Part 2
######################################################################

for s in LS:
    if abs(s[0][0] - s[1][0]) == abs(s[0][1] - s[1][1]):
        for p in iter_points_on_seg(s):
            P[p] += 1

result = 0
for k, v in P.items():
    if v > 1:
        result += 1

print(result)
# puzzle.answer_b = result
