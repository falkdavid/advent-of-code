#!/usr/bin/env python3
"""
    - Make sure to 'export AOC_SESSION=<your_aoc_token>'
    - Run the script in an ipython session using '%run <name>'
"""

from aocd.models import Puzzle
from typing import NamedTuple, List, Dict
from collections import Counter, defaultdict

# Enter year and day
puzzle = Puzzle(2020, 7)

data = puzzle.input_data
lines = data.split("\n")
######################################################################
#   Part 1
######################################################################

D = {}

for l in lines:
  key,rest = l.split("bags contain")
  values = rest.split(',')
  key = key.strip()
  
  D[key] = []
  for v in values:
    if v != " no other bags.":
      n, col1, col2, _rest = v.strip().split(' ')
      D[key].append((n, " ".join([col1, col2])))

D_inv = {}

for k,v in D.items():
  for vv in v:
    if vv[1] not in D_inv.keys():
      D_inv[vv[1]] = [k]
    else:
      D_inv[vv[1]].append(k)

result = 0
s = "shiny gold"

seen = set()
seen.add(s)

queue = []
queue.append(s)
while queue:
  curr = queue.pop(0)
  if curr in D_inv.keys():
    for v in D_inv[curr]:
      if v not in seen:
        seen.add(v)
        queue.append(v)
        result += 1

print(result)
# puzzle.answer_a = result


######################################################################
#   Part 2
######################################################################

def get_size(key,):
  if key in D.keys():
    if len(D[key]) == 0:
      return 1
    else:
      r = 1
      for x,v in D[key]:
        r += int(x) * get_size(v)
      return r
  else:
    return 1

print(get_size("shiny gold"))
# puzzle.answer_b = get_size("shiny gold")