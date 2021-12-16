#!/usr/bin/env python3
"""
    - Make sure to 'export AOC_SESSION=<your_aoc_token>'
    - Run the script in an ipython session using '%run <name>'
"""

from aocd.models import Puzzle
from typing import NamedTuple, List, Dict
from collections import Counter, defaultdict

# Enter year and day
puzzle = Puzzle(2021, 3)

data = puzzle.input_data
# data = """00100
# 11110
# 10110
# 10111
# 10101
# 01111
# 00111
# 11100
# 10000
# 11001
# 00010
# 01010"""
numbers = data.split()
N = list(map(lambda x: int(x, 2), numbers))
######################################################################
#   Part 1
######################################################################

l = len(numbers[0])
L = len(N)
gamma = 0
for i in range(l):
    bit = 1 << i
    s = sum([(n & bit) >> i for n in N])
    gamma |= int(s > (L//2)) << i

epsilon = gamma ^ int("1"*l, 2)

print(gamma * epsilon)
# puzzle.answer_a = gamma * epsilon


######################################################################
#   Part 2
######################################################################
ogr = 0
csr = 0
match_ogr = [format(n, f"0{l}b") for n in N]
match_csr = [format(n, f"0{l}b") for n in N]

for i in range(l):

    if len(match_ogr) > 1:
        c = Counter([n[i] for n in match_ogr])
        if len(c) == 2:
            a, b = c.most_common(2)
            most_common = a[0] if a[1] > b[1] else '1'

            tmp = [m for m in match_ogr if m[i] == most_common]
            if len(tmp) > 0:
                match_ogr = tmp

    if len(match_csr) > 1:
        c = Counter([n[i] for n in match_csr])
        if len(c) == 2:
            a, b = c.most_common(2)
            least_common = b[0] if a[1] > b[1] else '0'

            tmp = [m for m in match_csr if m[i] == least_common]
            if len(tmp) > 0:
                match_csr = tmp

print(int(match_ogr[0], 2) * int(match_csr[0], 2))
# puzzle.answer_b = int(match_ogr[0], 2) * int(match_csr[0], 2)
