#!/usr/bin/env python3
"""
    - Make sure to 'export AOC_SESSION=<your_aoc_token>'
    - Run the script in an ipython session using '%run <name>'
"""

from functools import reduce
from aocd.models import Puzzle
from typing import NamedTuple, List, Dict
from collections import Counter, defaultdict, deque

# Enter year and day
puzzle = Puzzle(2021, 9)

data = puzzle.input_data
# data = """2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678"""
lines = data.split('\n')
######################################################################
#   Part 1
######################################################################
D = defaultdict(lambda: 10)


def iter_neighbors(pos: tuple):
    for x, y in [(pos[0] - 1, pos[1]), (pos[0] + 1, pos[1]), (pos[0], pos[1] - 1), (pos[0], pos[1] + 1)]:
        yield (x, y)


for y, l in enumerate(lines):
    for x, d in enumerate([int(x) for x in l]):
        D[(x, y)] = d

B = []
awnser = 0
for k, v in D.items():
    if all([D[(x, y)] > v for x, y in iter_neighbors(k) if (x, y) in D.keys()]):
        awnser += v + 1
        B.append(k)

print(awnser)
# puzzle.answer_a = awnser

######################################################################
#   Part 2
######################################################################

def flood_fill(D : dict, pos : tuple):
    r = 1
    s = set([pos])
    q = deque([pos])
    while q:
        p = q.popleft()
        for v in iter_neighbors(p):
            if v not in s and (v in D.keys() and D[v] < 9):
                s.add(v)
                q.append(v)
                r += 1
    return r

BS = [flood_fill(D, v) for v in B]
awnser = reduce(lambda x, y: x*y, sorted(BS, reverse=True)[:3])

print(awnser)
# puzzle.answer_b = awnser
