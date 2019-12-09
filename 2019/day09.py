#!/usr/bin/env python3
"""
    - Make sure to 'export AOC_SESSION=<your_aoc_token>'
    - Run the script in an ipython session using '%run <name>'
"""

from aocd.models import Puzzle
from typing import NamedTuple, List, Dict
from collections import Counter, defaultdict

from intcodecpu import IntcodeComputer

# Enter year and day
puzzle = Puzzle(2019, 9)

data = puzzle.input_data
prog = list(map(int, data.split(',')))

######################################################################
#   Part 1
######################################################################

cpu = IntcodeComputer()
print(cpu.run(prog, [1])[0])
# puzzle.answer_a = cpu.run(prog, [1])[0]


######################################################################
#   Part 2
######################################################################

print(cpu.run(prog, [2])[0])
# puzzle.answer_b = cpu.run(prog, [2])[0]