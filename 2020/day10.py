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
puzzle = Puzzle(2020, 10)

data = list(map(int, puzzle.input_data.split('\n')))
# data = list(map(int, """28
# 33
# 18
# 42
# 31
# 14
# 46
# 20
# 48
# 47
# 24
# 23
# 49
# 45
# 19
# 38
# 39
# 11
# 1
# 32
# 25
# 35
# 8
# 17
# 7
# 9
# 4
# 2
# 34
# 10
# 3""".split('\n')))
######################################################################
#   Part 1
######################################################################

nums = sorted(data)
ones = 1
threes = 1
for x, y in zip(nums[::1], nums[1::1]):
    # print(x, y)
    if y - x == 1:
        ones += 1
    if y - x == 3:
        threes += 1

res = ones * threes
print(res)

# puzzle.answer_a = res


######################################################################
#   Part 2
######################################################################

res = 1
D = {}
for i, n in enumerate([0]+nums):
    for x in nums[i:i+3]:
        if 0 < x-n < 4:
            if n in D.keys():
                D[n].append(x)
            else:
                D[n] = [x]
DD = {k: 0 for k in D.keys()}
DD[0] = 1
for n in nums:
    s = 0
    for k, v in D.items():
        if k < n:
            if n in v:
                s += DD[k]
                # print(n, k, v)
    DD[n] = s

print(DD[max(nums)])
# puzzle.answer_b =
