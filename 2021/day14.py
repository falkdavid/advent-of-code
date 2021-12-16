#!/usr/bin/env python3
"""
    - Make sure to 'export AOC_SESSION=<your_aoc_token>'
    - Run the script in an ipython session using '%run <name>'
"""

from aocd.models import Puzzle
from typing import NamedTuple, List, Dict
from collections import Counter, defaultdict

# Enter year and day
puzzle = Puzzle(2021, 14)

data = puzzle.input_data
# data = """NNCB

# CH -> B
# HH -> N
# CB -> H
# NH -> C
# HB -> C
# HC -> B
# HN -> C
# NN -> C
# BH -> H
# NC -> B
# NB -> B
# BN -> B
# BB -> N
# BC -> B
# CC -> N
# CN -> C"""
input, rules = data.split('\n\n')
input = list(input.strip())
rules = rules.split('\n')
R = {}
for r in rules:
    k, v = r.split(" -> ") 
    R[k] = v

######################################################################
#   Part 1
######################################################################

str1 = "".join(input)
for _ in range(10):
    str2 = []
    for i in range(len(str1) - 1):
        ss = str1[i:i+2]
        str2.append(ss[0])
        if ss in R.keys():
            str2.append(R[ss])
    str2.append(str1[-1])
    str1 = "".join(str2)

c = Counter(str2)
awnser = max(c.values()) - min(c.values())
print(awnser)
# puzzle.answer_a = awnser


######################################################################
#   Part 2
######################################################################

c1 = Counter()
I = "".join(input)
for i in range(len(I) - 1):
    ss = I[i:i+2]
    c1[ss] += 1

for _ in range(40):
    c2 = Counter()
    for k,v in c1.items():
        c2[k[0]+R[k]] += v
        c2[R[k]+k[1]] += v
    c1 = c2.copy()

C = Counter()
for k,v in c1.items():
    C[k[0]] += v
C[I[-1]] += 1

awnser = max(C.values()) - min(C.values())
print(awnser)
# puzzle.answer_b = 