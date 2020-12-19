#!/usr/bin/env python3
"""
    - Make sure to 'export AOC_SESSION=<your_aoc_token>'
    - Run the script in an ipython session using '%run <name>'
"""

from aocd.models import Puzzle
from typing import NamedTuple, List, Dict
from collections import Counter, defaultdict

# Enter year and day
puzzle = Puzzle(2020, 16)

data = puzzle.input_data.split('\n\n')
######################################################################
#   Part 1
######################################################################
ranges = [(int(x.split('-')[0]), int(x.split('-')[1]))
          for l in data[0].split('\n') for x in l.split(": ")[1].split(' or ')]

nums = [x for l in data[1].split('\n')[1:] + data[2].split('\n')[1:]
        for x in list(map(int, l.split(',')))]

D = set()
for i in range(max(nums)):
    for j, k in ranges:
        if j <= i <= k:
            D.add(i)

res = 0
for n in nums:
    if n not in D:
        res += n

print(res)
# puzzle.answer_a =


######################################################################
#   Part 2
######################################################################
ranges = [(int(x.split('-')[0]), int(x.split('-')[1])) for l in data[0].split('\n')
          for x in l.split(": ")[1].split(' or ')]
ranges = list(zip(ranges[::2], ranges[1::2]))
# print(ranges)
my_t = [x for l in data[1].split('\n')[1:] for x in list(
    map(int, l.split(',')))[:len(ranges)]]
their = [list(map(int, l.split(',')))[:len(ranges)]
         for l in data[2].split('\n')[1:]]
their = [x for x in their if all([i in D for i in x])]

#rule : ticket_pos
candidates = {i:[] for i in range(len(ranges))}
for i, ((k, l), (u, v)) in enumerate(ranges):
    for j in range(len(ranges)):
        found = True
        for x in range(len(their)):
            n = their[x][j]
            if not (k <= n <= l) and not (u <= n <= v):
                # print(i, j, n, ((k, l), (u, v)))
                found = False
        if found:
            candidates[i].append(j)
            # print(i, j)

mapping = {}
while len(mapping.keys()) != len(ranges):
  rm = -1
  for k,v in candidates.items():
    if len(v) == 1:
      mapping[k] = v[0]
      rm = v[0]

  if rm != -1:
    for v in candidates.values():
      if rm in v:
        v.remove(rm)
  else:
    break
print(mapping)
res = 1
for x in range(6):
  res *= my_t[mapping[x]]

print(res)
# puzzle.answer_b =
