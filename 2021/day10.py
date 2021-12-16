#!/usr/bin/env python3
"""
    - Make sure to 'export AOC_SESSION=<your_aoc_token>'
    - Run the script in an ipython session using '%run <name>'
"""

from aocd.models import Puzzle
from typing import NamedTuple, List, Dict
from collections import Counter, defaultdict

from requests.api import get

# Enter year and day
puzzle = Puzzle(2021, 10)

data = puzzle.input_data
# data = """[({(<(())[]>[[{[]{<()<>>
# [(()[<>])]({[<{<<[]>>(
# {([(<{}[<>[]}>{[]{[(<()>
# (((({<>}<{<{<>}{[]{[]{}
# [[<[([]))<([[{}[[()]]]
# [{[{({}]{}}([{[{{{}}([]
# {<[[]]>}<{[{[{[]{()[[[]
# [<(<(<(<{}))><([]([]()
# <{([([[(<>()){}]>(<<{{
# <{([{{}}[<[[[<>{}]]]>[]]"""
lines = data.split('\n')
######################################################################
#   Part 1
######################################################################

# ): 3 points.
# ]: 57 points.
# }: 1197 points.
# >: 25137 points.

M = {'(': ')', '[': ']', '{': '}', '<': '>'}
P = {')': 3, ']': 57, '}': 1197, '>': 25137}


def matching(b1, b2):
    if M[b1] == b2:
        return True
    return False


def get_error(line):
    stack = [line[0]]
    for l in line[1:]:
        if l in M.keys():
            stack.append(l)
        elif l in M.values():
            if matching(stack[-1], l):
                stack.pop()
            else:
                # print(f"expected {M[stack[-1]]} but got {l}")
                return l
    return None


awnser = 0
for l in lines:
    if (c := get_error(l)):
        awnser += P[c]

print(awnser)
# puzzle.answer_a = awnser

######################################################################
#   Part 2
######################################################################

def complete_line(line):
    stack = [line[0]]
    for l in line[1:]:
        if l in M.keys():
            stack.append(l)
        elif l in M.values():
            if matching(stack[-1], l):
                stack.pop()
            else:
                return None

    return [M[c] for c in stack[::-1]]


def get_score(line):
    C = complete_line(line)
    if not C:
        return None
    res = 0
    for c in C:
        res *= 5
        res += list(M.values()).index(c) + 1
    return res


awnsers = []
for l in lines:
    score = get_score(l)
    if score:
        awnsers.append(score)
awnsers.sort()

median = awnsers[len(awnsers)//2]
print(median)
# puzzle.answer_b = median
