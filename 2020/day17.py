#!/usr/bin/env python3
"""
    - Make sure to 'export AOC_SESSION=<your_aoc_token>'
    - Run the script in an ipython session using '%run <name>'
"""

from aocd.models import Puzzle
from typing import NamedTuple, List, Dict
from collections import Counter, defaultdict

# Enter year and day
puzzle = Puzzle(2020, 17)

data = puzzle.input_data
# data = """.#.
# ..#
# ###"""
######################################################################
#   Part 1
######################################################################


def print_grid(D, z=0):
    xs = [x for x, y, z in D.keys()]
    ys = [y for x, y, z in D.keys()]

    for i in range(min(xs), max(xs)+1):
        for j in range(min(ys), max(ys)+1):
            if (i, j, z) in D.keys():
                if D[(i, j, z)] == 1:
                    print('#', end='')
                else:
                    print('.', end='')
            else:
                print('.', end='')
        print()


def neighbors(pos):
    x, y, z = pos
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            for k in [-1, 0, 1]:
                if i == j == k == 0:
                    continue
                yield (x+i, y+j, z+k)


D = {}
for i, l in enumerate(data.split('\n')):
    for j, c in enumerate(l):
        # print((i,j,c))
        if c == '#':
            D[(i, j, 0)] = 1
        else:
            D[(i, j, 0)] = 0

        for n in neighbors((i,j,0)):
          if n not in D.keys():
            D[n] = 0

# print_grid(D)


for _ in range(6):
    DD = {}
    for k, v in D.items():
        if v == 1:
            s = 0
            for n in neighbors(k):
                if n not in D.keys():
                    DD[n] = 0
                elif D[n] == 1:
                    s += 1
            if not (s == 2 or s == 3):
                DD[k] = 0
            else:
                DD[k] = 1
        elif v == 0:
            s = 0
            for n in neighbors(k):
                if n not in D.keys():
                    DD[n] = 0
                elif D[n] == 1:
                    s += 1
            if s == 3:
                DD[k] = 1
            else:
                DD[k] = 0

    D = DD.copy()
    # print_grid(D)

res = sum([1 for v in D.values() if v == 1])
print(res)

# puzzle.answer_a =


######################################################################
#   Part 2
######################################################################

def neighbors2(pos):
    x, y, z, w = pos
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            for k in [-1, 0, 1]:
                for l in [-1, 0, 1]:
                  if i == j == k == l == 0:
                      continue
                  yield (x+i, y+j, z+k, w+l)


D = {}
for i, l in enumerate(data.split('\n')):
    for j, c in enumerate(l):
        # print((i,j,c))
        if c == '#':
            D[(i, j, 0, 0)] = 1
        else:
            D[(i, j, 0, 0)] = 0

        for n in neighbors2((i,j,0,0)):
          if n not in D.keys():
            D[n] = 0


for _ in range(6):
    DD = {}
    for k, v in D.items():
        if v == 1:
            s = 0
            for n in neighbors2(k):
                if n not in D.keys():
                    DD[n] = 0
                elif D[n] == 1:
                    s += 1
            if not (s == 2 or s == 3):
                DD[k] = 0
            else:
                DD[k] = 1
        elif v == 0:
            s = 0
            for n in neighbors2(k):
                if n not in D.keys():
                    DD[n] = 0
                elif D[n] == 1:
                    s += 1
            if s == 3:
                DD[k] = 1
            else:
                DD[k] = 0

    D = DD.copy()

res = sum([1 for v in D.values() if v == 1])
print(res)

# puzzle.answer_b =
