#!/usr/bin/env python3
"""
    - Run the script in an ipython session using '%run <name>'
    - Make sure to 'export AOC_SESSION=<your_aoc_token>'
"""

from aocd.models import Puzzle
import re
from typing import NamedTuple

# https://adventofcode.com/2016/day/9
puzzle = Puzzle(2016, 9)

data = puzzle.input_data

######################################################################
#   Part 1
######################################################################


def decompress(inp: str) -> str:
    index = 0
    output = []
    while index < len(inp):
        match = re.search(r'\((\d+)x(\d+)\)', inp[index:])
        if not match:
            output.append(inp[index:])
            break

        sub_len, repeat = match.groups()
        repeat_idx = match.end()
        start_idx = match.start()

        output.append(inp[index:index + start_idx])
        output.append(inp[index + repeat_idx:index + repeat_idx + int(sub_len)] * int(repeat))
        
        index += repeat_idx + int(sub_len)
    
    return "".join(output)


test_strings = [
    "ADVENT","A(1x5)BC","(3x3)XYZ","A(2x2)BCD(2x2)EFG",
    "(6x1)(1x3)A","X(8x2)(3x3)ABCY"
]
assert decompress(test_strings[0]) == "ADVENT"
assert decompress(test_strings[1]) == "ABBBBBC"
assert decompress(test_strings[2]) == "XYZXYZXYZ"
assert decompress(test_strings[3]) == "ABCBCDEFEFG"
assert decompress(test_strings[4]) == "(1x3)A"
assert decompress(test_strings[5]) == "X(3x3)ABC(3x3)ABCY"

print(len(decompress(data)))
# puzzle.answer_a = len(decompress(data))


######################################################################
#   Part 2
######################################################################

def decompress2(inp: str) -> int:
    index = 0
    result = 0
    while index < len(inp):
        match = re.search(r'\((\d+)x(\d+)\)', inp[index:])
        if not match:
            result += len(inp[index:])
            break

        length, num_repeat = match.groups()
        start = match.end()
        match_idx = match.start()

        result += match_idx
        result += decompress2(inp[index + start:index + start + int(length)]) * int(num_repeat)

        index += start + int(length)    
    return result

test_strings = [
    "ABCD",
    "(11x10)(6x2)(1x5)X",
    "(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN"
]
assert decompress2(test_strings[0]) == 4
assert decompress2(test_strings[1]) == 100
assert decompress2(test_strings[2]) == 445
print(decompress2(data))
# puzzle.answer_b = decompress2(data)