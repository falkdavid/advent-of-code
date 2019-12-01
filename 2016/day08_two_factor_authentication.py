#!/usr/bin/env python3
"""
    - Run the script in an ipython session using '%run <name>'
    - Make sure to 'export AOC_SESSION=<your_aoc_token>'
"""

from aocd.models import Puzzle
from collections import deque
from typing import List
import re 


# https://adventofcode.com/2016/day/8
puzzle = Puzzle(2016, 8)

data = puzzle.input_data
lines = data.split('\n')
######################################################################
#   Part 1
######################################################################

class Screen(object):

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

        self.pixels = [['.' for c in range(self.width)] 
                            for r in range(self.height)] 

    def __repr__(self) -> str:
        return "\n".join("".join(p) for p in self.pixels)

    def rect(self, a: int, b: int):
        for c in range(a):
            for r in range(b):
                self.pixels[r][c] = '#'

    def rotate_row(self, a: int, by: int):
        r = deque(self.pixels[a])
        r.rotate(by)
        self.pixels[a] = list(r)

    def rotate_column(self, a: int, by: int):
        c = deque([self.pixels[i][a] for i in range(self.height)])
        c.rotate(by)
        for i, x in enumerate(list(c)):
            self.pixels[i][a] = x

    def count_lit(self) -> int:
        return sum([p == '#' for c in self.pixels for p in c])

def parse_instructions(lines: List[str], screen: Screen) -> Screen:
    for l in lines:
        l = l.strip()
        
        if "rect" in l:
            a, b = re.match(r"rect (\d+)x(\d+)", l).groups()
            screen.rect(int(a), int(b))

        elif "row" in l:
            a, b = re.match(r"rotate row y=(\d+) by (\d+)", l).groups()
            screen.rotate_row(int(a), int(b))

        elif "column" in l:
            a, b = re.match(r"rotate column x=(\d+) by (\d+)", l).groups()
            screen.rotate_column(int(a), int(b))

    return screen
        

screen = Screen(50, 6)
parse_instructions(lines, screen)
print(screen.count_lit())
# puzzle.answer_a = screen.count_lit()


######################################################################
#   Part 2
######################################################################

print(screen)
# puzzle.answer_b = "AFBUPZBJPS"