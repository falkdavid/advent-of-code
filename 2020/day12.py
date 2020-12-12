#!/usr/bin/env python3
"""
    - Make sure to 'export AOC_SESSION=<your_aoc_token>'
    - Run the script in an ipython session using '%run <name>'
"""

from aocd.models import Puzzle
from typing import NamedTuple, List, Dict
from collections import Counter, defaultdict
from math import atan2, cos, sin, radians
# Enter year and day
puzzle = Puzzle(2020, 12)

data = puzzle.input_data.split('\n')
# data = """F10
# N3
# F7
# R90
# F11""".split('\n')
data = [(l[0], int(l[1:])) for l in data]
######################################################################
#   Part 1
######################################################################

DD = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
DR = {}
# print([atan2(*v) for v in DD.values()])
x, y = 0, 0
hr = 0
hx, hy = 1, 0
for i, n in data:
    # print(x, y, hr, hx, hy)
    if i in DD.keys():
        dx, dy = DD[i]
        x += n*dx
        y += n*dy
    elif i == 'L':
        rad = radians(n)
        hr += rad
        hx, hy = int(cos(hr)), int(sin(hr))
    elif i == 'R':
        rad = radians(n)
        hr -= rad
        hx, hy = int(cos(hr)), int(sin(hr))
    else:
        x += n*hx
        y += n*hy
# print(x, y, hr, hx, hy)
res = abs(x)+abs(y)
print(res)
# puzzle.answer_a = res


######################################################################
#   Part 2
######################################################################

x, y = 0, 0
hx, hy = 10, 1
for i, n in data:
    # print(x, y, hx, hy)
    if i in DD.keys():
        dx, dy = DD[i]
        hx += n*dx
        hy += n*dy
    elif i == 'L':
        rad = radians(n)
        xx = int(hx * cos(rad)) - int(hy * sin(rad))
        yy = int(hx * sin(rad)) + int(hy * cos(rad))
        hx = xx
        hy = yy
    elif i == 'R':
        rad = radians(n)
        xx = int(hx * cos(rad)) + int(hy * sin(rad))
        yy = -int(hx * sin(rad)) + int(hy * cos(rad))
        hx = xx
        hy = yy
    else:
        x += n*hx
        y += n*hy
res = abs(x)+abs(y)
print(res)
# puzzle.answer_b = res
