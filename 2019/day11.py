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
puzzle = Puzzle(2019, 11)

data = puzzle.input_data
prog = list(map(int, data.split(',')))
######################################################################
#   Part 1
######################################################################


D = {(0, 'N'):'E',(1, 'N'):'W',
     (0, 'W'):'N',(1, 'W'):'S',
     (0, 'S'):'W',(1, 'S'):'E',
     (0, 'E'):'S',(1, 'E'):'N',
     'N':(0, 1), 'W':(1, 0), 'E':(-1, 0), 'S':(0, -1)}

def run_robot(prog, start_on=0):
    num = 0
    F = defaultdict(int)
    V = defaultdict(int)
    facing = 'N'
    x, y = 0, 0
    F[(x, y)] = start_on

    cpu = IntcodeComputer()
    cpu.init()
    cpu.load_prog(prog)

    cpu.running = True
    while cpu.running:

        color = F[(x, y)]
        cpu.put_input(color)

        outs = cpu.exec_until_output(2)
        if len(outs) == 2:
            new_color, turn = outs
            if new_color and (x, y) not in V:
                num += 1
            V[(x, y)] = 1
            F[(x, y)] = new_color

            facing = D[turn, facing]
            dx, dy = D[facing]
            x += dx
            y += dy
        else:
            break

        #print(F)

    return num, F

num, _ = run_robot(prog)
print(num)
# puzzle.answer_a = num


######################################################################
#   Part 2
######################################################################

def print_panels(prog):
    _, F = run_robot(prog, start_on=1)
    min_p = min(F.keys(), key=lambda x: x[0]+x[1])
    max_p = max(F.keys(), key=lambda x: x[0]+x[1])

    width = abs(min_p[0]) + abs(max_p[0])
    heigth = abs(min_p[1]) + abs(max_p[1])

    for j in range(heigth+1, -2, -1):
        for i in range(-1, width+1):
            print('#' if F[(i+min_p[0], j+min_p[1])] else ' ', end='')
        print()

print_panels(prog)
# puzzle.answer_b = "KRZEAJHB"