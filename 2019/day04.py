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
puzzle = Puzzle(2019, 4)

data = puzzle.input_data
A,B = tuple(map(int, data.split('-')))
######################################################################
#   Part 1
######################################################################

def check_passwd(passwd):
    last = ' '
    for c in str(passwd):
        if ord(c) < ord(last):
            return False
        last = c

    c = Counter(str(passwd))
    for v in c.values():
        if v > 1:
            return True
    return False

def num_passwds(start, end):
    return sum([check_passwd(i) for i in range(start, end+1)])

assert check_passwd(111111) == True
assert check_passwd(223450) == False
assert check_passwd(123789) == False
print(num_passwds(A, B))
# puzzle.answer_a = num_passwds(A, B)


######################################################################
#   Part 2
######################################################################

def check_passwd2(passwd):
    last = ' '
    for c in str(passwd):
        if ord(c) < ord(last):
            return False
        last = c

    c = Counter(str(passwd))
    if 2 in c.values():
        return True

    return False

def num_passwds2(start, end):
    return sum([check_passwd2(i) for i in range(start, end+1)])

assert check_passwd2(112233) == True
assert check_passwd2(123444) == False
assert check_passwd2(111122) == True
print(num_passwds2(A, B))
# puzzle.answer_b = num_passwds2(A, B)