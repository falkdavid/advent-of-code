#!/usr/bin/env python3
"""
    - Make sure to 'export AOC_SESSION=<your_aoc_token>'
    - Run the script in an ipython session using '%run <name>'
"""

from aocd.models import Puzzle
from typing import NamedTuple, List, Dict
from collections import Counter, defaultdict

# Enter year and day
puzzle = Puzzle(2020, 5)

data = puzzle.input_data
#data = """BFFFBBFRRR"""
boardingpasses = data.split('\n')
######################################################################
#   Part 1
######################################################################

B=boardingpasses

print(max([int(s.translate({ord(c):('1'if ord(c)%70>6else'0')for c in'FBRL'}),2)for s in B]))

def parse_pass(boardingpass):
  row_str = boardingpass[0:7]
  f = 0
  b = 127
  for x in row_str:
    ll = (b - f) + 1
    if x == 'F':
      b -= ll//2
    if x == 'B':
      f += ll//2
  row_nr = f
  seat_str = boardingpass[7:]
  l = 0
  r = 7
  for x in seat_str:
    ll = (r-l) + 1
    if x == 'L':
      r -= ll//2
    if x == 'R':
      l += ll//2
  seat_nr = l
  return row_nr, seat_nr

s_ids = []

for b in boardingpasses:
  r, c = parse_pass(b)
  s_id = r*8 + c
  s_ids.append(s_id)

print(max(s_ids))
# puzzle.answer_a = 


######################################################################
#   Part 2
######################################################################

sorted_ids = sorted(s_ids)

for i,x in enumerate(sorted_ids[:-1]):
  y = sorted_ids[i+1]
  if x+2 == y:
    print(x+1)
    break
# puzzle.answer_b = 