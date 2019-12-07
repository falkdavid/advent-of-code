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
puzzle = Puzzle(2019, 3)

data = puzzle.input_data
lines = data.split('\n')

######################################################################
#   Part 1
######################################################################
DX = {'U':0, 'D':0, 'L': -1, 'R': 1}
DY = {'U':1, 'D':-1, 'L': 0, 'R': 0}
def get_wires(lines):
    p = []
    for l in lines:
        x, y = (0, 0)
        wire = []
        for d in l.split(','):
            facing = d[0]
            steps = int(d[1:])
            dx = DX[facing]
            dy = DY[facing]
            new_p = [(x+i*dx, y+i*dy) for i in range(1, steps+1)]
            x += steps*dx
            y += steps*dy
            
            wire.extend(new_p)
        p.append(wire)
    return p

def get_intersections(wires):
    intersections = []
    for i in range(len(wires)):
        c = set(wires[i])
        for j, other in enumerate(wires):
            other = set(other)
            if j != i:
                inter = list(c.intersection(other))
                intersections.extend(inter)
    return intersections

def get_closest_intersection(wires):
    intersections = get_intersections(wires)
    closest = min(intersections, key=manhatten)
    return closest

def manhatten(p):
    return abs(p[0]) + abs(p[1])

wires = get_wires(lines)

test_wires = get_wires("""R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83""".split('\n'))
test_closest = get_closest_intersection(test_wires)
assert manhatten(test_closest) == 159
print(manhatten(get_closest_intersection(wires)))
# puzzle.answer_a = manhatten(get_closest_intersection(wires))


######################################################################
#   Part 2
######################################################################

def get_sum_wires(wires):
    its = get_intersections(wires)
    sums = []
    for it in its:
        s = 0
        for w in wires:
            if it in w:
                s += w.index(it)+1
        sums.append(s)
    return min(sums)

assert get_sum_wires(test_wires) == 610
print(get_sum_wires(wires))
# puzzle.answer_b = get_sum_wires(wires)