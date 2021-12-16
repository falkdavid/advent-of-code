#!/usr/bin/env python3
"""
    - Make sure to 'export AOC_SESSION=<your_aoc_token>'
    - Run the script in an ipython session using '%run <name>'
"""

from aocd.models import Puzzle
from typing import NamedTuple, List, Dict
from collections import Counter, defaultdict

# Enter year and day
puzzle = Puzzle(2021, 8)

data = puzzle.input_data
# data = """acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf
# be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
# edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc"""
lines = data.split("\n")
S = [[p.strip().split() for p in l.split(" | ")] for l in lines]

######################################################################
#   Part 1
######################################################################

awnser_a = 0
for s in S:
    for d in s[1]:
        if len(d) in (2, 3, 4, 7):
            awnser_a += 1
print(awnser_a)
# puzzle.answer_a = awnser_a


######################################################################
#   Part 2
######################################################################


def get_digits(inp):
    s1 = set([d for d in inp if len(d) == 2][0])
    s7 = set([d for d in inp if len(d) == 3][0])
    s4 = set([d for d in inp if len(d) == 4][0])
    s8 = set([d for d in inp if len(d) == 7][0])

    s2 = set([d for d in inp
              if len(d) == 5 and len(set(d).intersection(s4)) == 2
              ][0])
    s3 = set([d for d in inp
              if len(d) == 5 and len(set(d).intersection(s2)) == 4
              ][0])
    s5 = set([d for d in inp
              if len(d) == 5 and set(d) != s2 and set(d) != s3
              ][0])

    s6 = set([d for d in inp
              if len(d) == 6 and len(set(d).intersection(s1)) == 1
              ][0])
    s0 = set([d for d in inp
              if len(d) == 6 and len(set(d).intersection(s4)) == 3 and set(d) != s6
              ][0])
    s9 = set([d for d in inp
              if len(d) == 6 and set(d) != s6 and set(d) != s0
              ][0])

    return s0, s1, s2, s3, s4, s5, s6, s7, s8, s9


awnser_2 = 0
for s in S:
    digits = get_digits(s[0])
    number = int("".join([str(digits.index(set(d))) for d in s[1]]))
    awnser_2 += number

print(awnser_2)
# puzzle.answer_b = awnser_2
