#!/usr/bin/env python3
"""
    - Make sure to 'export AOC_SESSION=<your_aoc_token>'
    - Run the script in an ipython session using '%run <name>'
"""

from aocd.models import Puzzle
from typing import NamedTuple, List, Dict
from collections import Counter, defaultdict

# Enter year and day
puzzle = Puzzle(2021, 4)

data = puzzle.input_data
lines = data.split('\n')
numbers = [int(d) for d in lines[0].split(',')]


def get_boards(lines):
    boards = []
    for l in lines:
        if l == "":
            boards.append(list())
        else:
            boards[-1].append([int(d) for d in l.split()])
    return boards


boards = get_boards(lines[1:])
######################################################################
#   Part 1
######################################################################
won = set()


def iterate_colums(board):
    for i in range(len(board)):
        yield [row[i] for row in board]


def get_unmarked(board):
    return [n for row in board for n in row if n not in won]


def has_won(board):
    for row in board:
        if all([n in won for n in row]):
            return sum(row)
    for column in iterate_colums(board):
        if all([n in won for n in column]):
            return sum(column)
    return 0


def get_win_score(numbers, boards):
    for N in numbers:
        won.add(N)
        for b in boards:
            if has_won(b):
                return sum(get_unmarked(b)) * N


print(get_win_score(numbers, boards))
# puzzle.answer_a = get_win_score(numbers, boards)


######################################################################
#   Part 2
######################################################################
won = set()
boards2 = boards[:]


def get_win_score2(numbers, boards):
    for N in numbers:
        won.add(N)
        b_copy = boards[:]
        for b in b_copy:
            if has_won(b):
                if len(boards) == 1:
                    return sum(get_unmarked(b)) * N
                else:
                    boards.remove(b)

print(get_win_score2(numbers, boards2))
# puzzle.answer_b =
