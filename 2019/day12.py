#!/usr/bin/env python3
"""
    - Make sure to 'export AOC_SESSION=<your_aoc_token>'
    - Run the script in an ipython session using '%run <name>'
"""

from aocd.models import Puzzle
from typing import NamedTuple, List, Dict
from collections import Counter, defaultdict
import re
import itertools
from math import gcd

# Enter year and day
puzzle = Puzzle(2019, 12)

data = puzzle.input_data
lines = data.split('\n')
######################################################################
#   Part 1
######################################################################

class Moon(object):

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

        self.dx = 0
        self.dy = 0
        self.dz = 0


    def gravity(self, other):
        if self.x < other.x:
            self.dx += 1
            other

    def move(self):
        self.x += self.dx
        self.y += self.dy
        self.z += self.dz

    def energy(self):
        return (abs(self.x) + abs(self.y) + abs(self.z))*(abs(self.dx) + abs(self.dy) + abs(self.dz)) 

    def __repr__(self):
        return f"<x={self.x}, y={self.y}, z={self.z}>"

def get_moons(lines):
    moons = []
    for l in lines:
        x, y, z = re.match(r'<x=(-?\d+), y=(-?\d+), z=(-?\d+)>', l).groups()
        moons.append(Moon(int(x), int(y), int(z)))

    return moons

def simulate(moons, steps=1000):
    for step in range(steps):
        # gravity
        for m, other in itertools.combinations(moons, 2):
            if m.x < other.x:
                m.dx += 1
                other.dx -= 1
            elif m.x > other.x:
                m.dx -= 1
                other.dx += 1

            if m.y < other.y:
                m.dy += 1
                other.dy -= 1
            elif m.y > other.y:
                m.dy -= 1
                other.dy += 1

            if m.z < other.z:
                m.dz += 1
                other.dz -= 1
            elif m.z > other.z:
                m.dz -= 1
                other.dz += 1

        for m in moons:
            m.move()

    return sum([m.energy() for m in moons])

test_lines = """<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>""".split('\n')

test_moons = get_moons(test_lines)
assert simulate(test_moons, 10) == 179

moons = get_moons(lines)
print(simulate(moons))
# puzzle.answer_a = simulate(moons)


######################################################################
#   Part 2
######################################################################

def simulate2(moons):
    seenx = set()
    seeny = set()
    seenz = set()

    foundx = 0
    foundy = 0
    foundz = 0

    step = 0
    while True:
        # gravity
        for m, other in itertools.combinations(moons, 2):
            if m.x < other.x:
                m.dx += 1
                other.dx -= 1
            elif m.x > other.x:
                m.dx -= 1
                other.dx += 1

            if m.y < other.y:
                m.dy += 1
                other.dy -= 1
            elif m.y > other.y:
                m.dy -= 1
                other.dy += 1

            if m.z < other.z:
                m.dz += 1
                other.dz -= 1
            elif m.z > other.z:
                m.dz -= 1
                other.dz += 1

        for m in moons:
            m.move()
        
        posx = tuple([(m.x, m.dx) for m in moons])
        posy = tuple([(m.y, m.dy) for m in moons])
        posz = tuple([(m.z, m.dz) for m in moons])
        if posx in seenx:
            if not foundx:
                foundx = step
        else:
            seenx.add(posx)

        if posy in seeny:
             if not foundy:
                foundy = step
        else:
            seeny.add(posy)

        if posz in seenz:
             if not foundz:
                foundz = step
        else:
            seenz.add(posz)

        if foundx and foundy and foundz:
            break

        step += 1

    lcmxy = foundx*foundy//gcd(foundx, foundy)
    return lcmxy*foundz//gcd(lcmxy, foundz)

print(simulate2(moons))
# puzzle.answer_b = simulate2(moons)

