#!/usr/bin/env python3
"""
    - Run the script in an ipython session using '%run <name>'
    - Make sure to 'export AOC_SESSION=<your_aoc_token>'
"""

from aocd.models import Puzzle
from typing import NamedTuple, List
import re


# https://adventofcode.com/2016/day/3
puzzle = Puzzle(2016, 3)

data = puzzle.input_data
tri_data = data.split('\n')

######################################################################
#   Part 1
######################################################################

class Triangle(NamedTuple):
    a: int
    b: int
    c: int

    def valid(self) -> bool:
        if self.a + self.b > self.c and \
           self.a + self.c > self.b and \
           self.b + self.c > self.a:

            return True
        else:
            return False

def get_triangles(tris_list: List[str]) -> List[Triangle]:
    tris = []
    for l in tris_list:
        a, b, c = [int(l[i*5:(i+1)*5]) for i in range(3)]
        tris.append(Triangle(a, b, c))
    return tris

def get_valid_tris(tris: List[Triangle]) -> List[Triangle]:
    return [t for t in tris if t.valid()]

triangles = get_triangles(tri_data)
print(len(get_valid_tris(triangles)))
# puzzle.answer_a = len(get_valid_tris(triangles))


######################################################################
#   Part 2
######################################################################

def get_triangles_vertically(tris_list: List[str]) -> List[Triangle]:
    tris = []
    for i in range(0, len(tris_list), 3):
        for j in range(3):
            a, b, c = [int(tris_list[i+k][j*5:(j+1)*5]) for k in range(3)]
            tris.append(Triangle(a, b, c))
    return tris

triangles = get_triangles_vertically(tri_data)
print(len(get_valid_tris(triangles)))
# puzzle.answer_b = len(get_valid_tris(triangles))