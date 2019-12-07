#!/usr/bin/env python3
"""
    - Make sure to 'export AOC_SESSION=<your_aoc_token>'
    - Run the script in an ipython session using '%run <name>'
"""

from aocd.models import Puzzle
from typing import NamedTuple, List, Dict
from collections import Counter, defaultdict
from itertools import permutations
from queue import Queue

from intcodecpu import IntcodeComputer

# Enter year and day
puzzle = Puzzle(2019, 7)

data = puzzle.input_data
prog = list(map(int, data.split(',')))

######################################################################
#   Part 1
######################################################################
cpu = IntcodeComputer()

def find_max_comb(prog):
    res = []
    for c in permutations(list(range(5)), 5):
        last_res = 0
        for i in range(5):
            phase_setting = c[i]

            outs = cpu.run(prog, [phase_setting, last_res])

            last_res = outs[0]
            res.append(last_res)

    return max(res)

print(find_max_comb(prog))
# puzzle.answer_a = find_max_comb(prog)

######################################################################
#   Part 2
######################################################################

def run_phase_settings(prog, phase_setting):
    amps = [IntcodeComputer() for i in range(5)]

    for i, amp in enumerate(amps):
        amp.load_prog(prog)
        amp.put_input(phase_setting[i])
        amp.running = True

    amps[0].put_input(0)

    last_output = 0
    current_amp = 0
    while amps[-1].running:
        amp = amps[current_amp]
        while True:
            amp.exec_next()
            if not amp.running:
                current_amp = (current_amp + 1) % 5
                break

            out = amp.get_output()
            if out is not None:
                last_output = out
                current_amp = (current_amp + 1) % 5
                amps[current_amp].put_input(last_output)
                break

    return last_output

test1_prog = list(map(int, "3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5".split(',')))
#print(run_phase_settings(test1_prog, (9,8,7,6,5)))
assert run_phase_settings(test1_prog, (9,8,7,6,5)) == 139629729

def find_max_comb2(prog):
    res = []
    for c in permutations(list(range(5, 10))):
        res.append(run_phase_settings(prog, c))

    return max(res)


print(find_max_comb2(prog))
# puzzle.answer_b = 