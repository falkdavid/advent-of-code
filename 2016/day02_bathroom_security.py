#!/usr/bin/env python3
"""
    - Run the script in an ipython session using '%run <name>'
    - Make sure to 'export AOC_SESSION=<your_aoc_token>'
"""

from aocd.models import Puzzle
from typing import List, Dict

# https://adventofcode.com/2016/day/2
puzzle = Puzzle(2016, 2)

data = puzzle.input_data
instructions = data.split('\n')

######################################################################
#   Part 1
######################################################################

# 1 2 3
# 4 5 6
# 7 8 9

# state machine to track movment over keypad
alph = "UDLR"
t_f = {'1':'1412','2':'2513','3':'3623','4':'1745',
       '5':'2846','6':'3956','7':'4778','8':'5879','9':'6989'}

def get_mapping(tf: Dict) -> Dict:
    return {k:{alph[i]:v[i] for i in range(len(alph))} 
                            for k,v in t_f.items()}

t_f_mapping = get_mapping(t_f)

def feed_word(word: str, start: str ='5') -> str:
    state = start
    for c in word:
        new_state = t_f_mapping[state][c]
        state = new_state
    return state

def get_code(instrs: List[str], start: str = '5') -> str:
    state = start
    code = []
    for instr in instrs:
        state = feed_word(instr, state)
        code.append(state)

    return "".join(code)

test_instrs = """ULL
RRDDD
LURDL
UUUUD"""
assert get_code(test_instrs.split('\n')) == "1985"

print(get_code(instructions))

# puzzle.answer_a = get_code(instructions)


######################################################################
#   Part 2
######################################################################

#     1
#   2 3 4
# 5 6 7 8 9
#   A B C
#     D

# Update transition function for new keypad

t_f = {'1':'1311','2':'2623','3':'1724','4':'4834','5':'5556',
       '6':'2A57','7':'3B68','8':'4C79','9':'9989','A':'6AAB',
       'B':'7DAC','C':'8CBC','D':'BDDD'}

t_f_mapping = get_mapping(t_f)

assert get_code(test_instrs.split('\n')) == "5DB3"

print(get_code(instructions))

# puzzle.answer_b = get_code(instructions)