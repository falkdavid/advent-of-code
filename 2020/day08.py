#!/usr/bin/env python3
"""
    - Make sure to 'export AOC_SESSION=<your_aoc_token>'
    - Run the script in an ipython session using '%run <name>'
"""

from aocd.models import Puzzle
from typing import NamedTuple, List, Dict
from collections import Counter, defaultdict

# Enter year and day
puzzle = Puzzle(2020, 8)

data = puzzle.input_data

######################################################################
#   Part 1
######################################################################


class GameConsole:
  def nop(self, x1):
    return
  def acc(self, x1):
    self.a += x1
    return
  def jmp(self, x1):
    self.ip += x1
    return

  def execute_instr(self):
    if self.ip == len(self.program):
      return 1
    op, x1 = self.program[self.ip]
    self.INSTR[op](x1)
    if op != 'jmp':
      self.ip += 1
    return 0

  def reset(self):
    self.a = 0
    self.ip = 0

  def __init__(self, program, ip=0):
    self.INSTR = {
      'nop' : self.nop,
      'acc' : self.acc,
      'jmp' : self.jmp,
    }

    self.program = []
    self.a = 0
    self.ip = ip

    instr_strs = program.split("\n")
    for s in instr_strs:
      op, x = s.split()
      self.program.append((op, int(x)))


gc = GameConsole(data)
N = len(gc.program)
seen = set()
while gc.ip not in seen:
  seen.add(gc.ip)
  gc.execute_instr()

print(gc.a)
# puzzle.answer_a = gc.a


######################################################################
#   Part 2
######################################################################

found_acc = None
for i in range(N):
  old_prg = gc.program[:]
  if gc.program[i][0] == 'nop':
    gc.program[i] = ('jmp', gc.program[i][1])
  elif gc.program[i][0] == 'jmp':
    gc.program[i] = ('nop', gc.program[i][1])

  seen = set()
  while gc.ip not in seen:
    seen.add(gc.ip)
    if gc.execute_instr() == 1:
      found_acc = gc.a

  gc.program = old_prg[:]
  gc.reset()

  if found_acc:
    break

print(found_acc)
# puzzle.answer_b = found_acc