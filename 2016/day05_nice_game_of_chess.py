#!/usr/bin/env python3
"""
    - Run the script in an ipython session using '%run <name>'
    - Make sure to 'export AOC_SESSION=<your_aoc_token>'
"""

from aocd.models import Puzzle
from hashlib import md5

# Enter year and day
puzzle = Puzzle(2016, 5)

data = puzzle.input_data

######################################################################
#   Part 1
######################################################################

def get_password(inp: str) -> str:
    pwd = []
    index = 0
    prev_index = 0
    while len(pwd) < 8:
        test = inp + str(index)
        try_hash = md5(test.encode()).hexdigest()
        if try_hash.startswith('00000'):
            pwd.append(try_hash[5])
            prev_index = index
        index += 1

    return "".join(pwd)

# assert get_password("abc") == "18f47a30"
pwd = get_password(data)
print(pwd)
# puzzle.answer_a = get_password(data)


######################################################################
#   Part 2
######################################################################

def get_password2(inp: str) -> str:
    pwd = list("_"*8)
    index = 0
    found = 0
    while found < 8:
        string = (inp + str(index)).encode()
        try_hash = md5(string).hexdigest()
        if try_hash.startswith('00000'):
            pos = int(try_hash[5], 16)
            if pos < 8 and pwd[pos] == '_':
                pwd[pos] = try_hash[6]
                found += 1
        index += 1

    return "".join(pwd)

# assert get_password2("abc") == "05ace8e3"
pwd = get_password2(data)
print(pwd)
# puzzle.answer_b = get_password2(data)