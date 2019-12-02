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
puzzle = Puzzle(2019, 2)

data = puzzle.input_data
opcodes = list(map(int, data.split(',')))
######################################################################
#   Part 1
######################################################################

def simulate(ops, noun, verb):
    ops[1] = noun
    ops[2] = verb
    for i in range(0, len(ops), 4):
        try:
            instr = ops[i]
            if instr == 1:
                a = ops[ops[i+1]]
                b = ops[ops[i+2]]
                ops[ops[i+3]] = a + b
            elif instr == 2:
                a = ops[ops[i+1]]
                b = ops[ops[i+2]]
                ops[ops[i+3]] = a * b
            elif instr == 99:
                break
        except:
            raise RuntimeError("Error")

    return ops[0]

assert simulate([1,9,10,3,2,3,11,0,99,30,40,50],9,10) == 3500
print(simulate(list(opcodes), 12, 2))
# puzzle.answer_a = simulate(opcodes, 12, 2)


######################################################################
#   Part 2
######################################################################

def find_output(opcodes, value):
    noun = 1
    verb = 1
    for noun in range(0, 100):
        for verb in range(0, 100):
            ops = list(opcodes)
            try:
                res = simulate(ops, noun, verb)
            except:
                continue

            if res == value:
                return 100 * noun + verb
    return None

print(find_output(opcodes, 19690720))
# puzzle.answer_b = find_output(opcodes, 19690720)