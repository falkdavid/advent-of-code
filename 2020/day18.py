#!/usr/bin/env python3
"""
    - Make sure to 'export AOC_SESSION=<your_aoc_token>'
    - Run the script in an ipython session using '%run <name>'
"""

from aocd.models import Puzzle
from typing import NamedTuple, List, Dict
from collections import Counter, defaultdict
import re
# Enter year and day
puzzle = Puzzle(2020, 18)

data = puzzle.input_data
lines = [l.replace(' ', '') for l in data.split('\n')]
######################################################################
#   Part 1
######################################################################
def E(e):
  if len(e)==1:
    return int(e)
  

def eval_expr(e):
    # expr is a number
    if re.match(r'^\d+$', e):
        return int(e)

    p, a, m = 0, -1, -1
    idx = len(e)-1
    while idx >= 0:
        c = e[idx]
        if p == 0:
            if c == '+':
                a = idx
                break
            elif c == '*':
                m = idx
                break
        if c == ')':
            p += 1
        elif c == '(':
            p -= 1
        idx -= 1

    # expr is in paran
    if a == m == -1:
        return eval_expr(e[1:-1])

    # expr is an addition
    if a > m:
        return eval_expr(e[:a]) + eval_expr(e[a+1:])

    # expr is a multiplication
    if m > a:
        return eval_expr(e[:m]) * eval_expr(e[m+1:])


res = 0
for l in lines:
    res += eval_expr(l)

print(res)
# puzzle.answer_a =


######################################################################
#   Part 2
######################################################################

def eval_expr2(e):
  # print(e)
  # expr is a number
  if re.match(r'^\d+$', e):
    return int(e)

  p, a, m = 0, -1, -1
  idx = len(e)-1
  while idx >= 0:
    c = e[idx]
    if p == 0:
      if c == '+' and a<0:
        a = idx
      elif c == '*' and m<0:
        m = idx

    if c == ')':
      p += 1
    elif c == '(':
      p -= 1

    idx -= 1

  # expr is in paran
  if a == m == -1:
    return eval_expr2(e[1:-1])

  # expr is a multiplication
  if m > 0:
    return eval_expr2(e[:m]) * eval_expr2(e[m+1:])

  # expr is an addition
  if a > 0:
    return eval_expr2(e[:a]) + eval_expr2(e[a+1:])

# print(eval_expr2("5*9*(7*3*3+9*3+(8+6*4))"))
res = 0
for l in lines:
    res += eval_expr2(l)

print(res)
# puzzle.answer_b =
