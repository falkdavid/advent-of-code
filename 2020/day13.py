#!/usr/bin/env python3
"""
    - Make sure to 'export AOC_SESSION=<your_aoc_token>'
    - Run the script in an ipython session using '%run <name>'
"""

from aocd.models import Puzzle
from typing import NamedTuple, List, Dict
from collections import Counter, defaultdict
from math import prod
# Enter year and day
puzzle = Puzzle(2020, 13)

data = puzzle.input_data.split('\n')
N = int(data[0])
nums = [int(x) for x in data[1].split(',') if x != 'x']
######################################################################
#   Part 1
######################################################################

X = min([(x-(N % x), x) for x in nums], key=lambda x: x[0])
res = X[0]*X[1]

print(res)
# puzzle.answer_a = res


######################################################################
#   Part 2
######################################################################
# test = "1789,37,47,1889"
nums = [(i, int(x)) for i, x in enumerate(data[1].split(',')) if x != 'x']
M = prod([m for _, m in nums])

def ext_gcd(a, b):
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1

    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t

    return old_s, old_t


R = 0
for a, m in nums:
    Mi = M // m
    _, s = ext_gcd(m, Mi)
    R += a * s*Mi

res = M - R % M
print(res)

# puzzle.answer_b = res
