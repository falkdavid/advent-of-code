#!/usr/bin/env python3
"""
    - Make sure to 'export AOC_SESSION=<your_aoc_token>'
    - Run the script in an ipython session using '%run <name>'
"""

from aocd.models import Puzzle
from typing import NamedTuple, List, Dict
from collections import Counter, defaultdict

# Enter year and day
puzzle = Puzzle(2019, 5)

data = puzzle.input_data
prog = list(map(int, data.split(',')))
######################################################################
#   Part 1
######################################################################

def simulate(prog):
    i = 0
    while prog[i] != 99:
        try:
            instr = prog[i]
            op = instr % 100
            m1 = (instr // 100) % 10
            m2 = (instr // 1000) % 10
            m3 = (instr // 1000) % 10
            if op == 1:
                if m1 == 0:
                    a = prog[prog[i+1]]
                else:
                    a = prog[i+1]
                
                if m2 == 0:
                    b = prog[prog[i+2]]
                else:
                    b = prog[i+2]
                
                prog[prog[i+3]] = a + b
                i += 4
            elif op == 2:
                if m1 == 0:
                    a = prog[prog[i+1]]
                else:
                    a = prog[i+1]
                
                if m2 == 0:
                    b = prog[prog[i+2]]
                else:
                    b = prog[i+2]

                prog[prog[i+3]] = a * b
                i += 4
            elif op == 3:
                val = int(input("Enter Number > "))
                prog[prog[i+1]] = val
                i += 2
            elif op == 4:
                if m1 == 0:
                    print(f"Out: {prog[prog[i+1]]}")
                else:
                    print(f"Out: {prog[i+1]}")
                i += 2
            elif op == 5:
                if m1 == 0:
                    a = prog[prog[i+1]]
                else:
                    a = prog[i+1]

                if m2 == 0:
                    b = prog[prog[i+2]]
                else:
                    b = prog[i+2]

                if a != 0:
                    i = b
                else:
                    i += 3
                
            elif op == 6:
                if m1 == 0:
                    a = prog[prog[i+1]]
                else:
                    a = prog[i+1]

                if m2 == 0:
                    b = prog[prog[i+2]]
                else:
                    b = prog[i+2]

                if a == 0:
                    i = b
                else:
                    i += 3

            elif op == 7:
                if m1 == 0:
                    a = prog[prog[i+1]]
                else:
                    a = prog[i+1]

                if m2 == 0:
                    b = prog[prog[i+2]]
                else:
                    b = prog[i+2]

                if a < b:
                    prog[prog[i+3]] = 1
                else:
                    prog[prog[i+3]] = 0
                
                i += 4
            elif op == 8:
                if m1 == 0:
                    a = prog[prog[i+1]]
                else:
                    a = prog[i+1]

                if m2 == 0:
                    b = prog[prog[i+2]]
                else:
                    b = prog[i+2]

                if a == b:
                    prog[prog[i+3]] = 1
                else:
                    prog[prog[i+3]] = 0
                
                i += 4
        except:
            raise RuntimeError("Error")

simulate(prog)

# puzzle.answer_a = 12440243


######################################################################
#   Part 2
######################################################################

simulate(prog)

# puzzle.answer_b = 15486302