#!/usr/bin/env python3
"""
    - Make sure to 'export AOC_SESSION=<your_aoc_token>'
    - Run the script in an ipython session using '%run <name>'
"""

from aocd.models import Puzzle
from typing import NamedTuple, List, Dict
from collections import Counter, defaultdict
import numpy as np

# Enter year and day
puzzle = Puzzle(2021, 6)

data = puzzle.input_data
# data = """3,4,3,1,2"""
numbers = [int(n) for n in data.split(',')]
######################################################################
#   Part 1
######################################################################


def part1(numbers, days=80):
    N = sorted(numbers[:])

    for day in range(days):
        tmp = N
        new = tmp.count(0)

        tmp = [x-1 for x in tmp][new:]

        try:
            i = tmp.index(7)
            tmp[i:i] = [6 for _ in range(new)]
        except ValueError:
            tmp.extend([6 for _ in range(new)])
        tmp.extend([8 for _ in range(new)])
        N = tmp
    return len(N)

print(part1(numbers))
# puzzle.answer_a = part1(numbers)


######################################################################
#   Part 2
######################################################################

def part2(numbers, days=256):
    number_zeros = [0 for _ in range(days+1)]
    number_zeros[0] = sum(1 for n in numbers if n == 0)
    for i in range(1, days+1):
        number_zeros[i] += sum([1 for n in numbers if ((i - n) % 7) == 0])
        if i > 8:
            number_zeros[i] += sum([number_zeros[j] for j in range(i-8) if ((i - j - 9) % 7) == 0])

    return sum(number_zeros[:-1]) + len(numbers)


print(part2(numbers))
# puzzle.answer_b = part2(numbers)
