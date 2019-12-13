#!/usr/bin/env python3
"""
    - Make sure to 'export AOC_SESSION=<your_aoc_token>'
    - Run the script in an ipython session using '%run <name>'
"""

from aocd.models import Puzzle
from typing import NamedTuple, List, Dict
from collections import Counter, defaultdict
from intcodecpu import IntcodeComputer
from queue import Queue
from time import sleep
import curses

# Enter year and day
puzzle = Puzzle(2019, 13)

data = puzzle.input_data
prog = list(map(int, data.split(',')))
######################################################################
#   Part 1
######################################################################

cpu = IntcodeComputer()
outs = cpu.run(prog)

res = 0
Grid = defaultdict(int)
for i in range(0, len(outs), 3):
    x, y, id = outs[i:i+3]
    Grid[(x, y)] = id
    if id == 2:
        res += 1

print(res)
# puzzle.answer_a = res


######################################################################
#   Part 2
######################################################################

class Arcade(object):

    def __init__(self, prog):
        self.cpu = IntcodeComputer()
        self.cpu.init()
        self.cpu.load_prog(prog)
        self.out_buffer = []
        self.screen = defaultdict(int)
        self.current_score = 0
        self.ball_pos = 0
        self.paddle_pos = 21
        self.stdscr = None

    def draw_screen(self, visible):
        for i in range(0, len(self.out_buffer), 3):
            x, y, id = self.out_buffer[i:i+3]
            if x == -1 and y == 0:
                self.current_score = id
            else:
                self.screen[(x, y)] = id

            if id == 3:
                self.paddle_pos = x
            if id == 4:
                if x != self.ball_pos:
                    if self.paddle_pos > x:
                        self.cpu.put_input(-1)
                    elif self.paddle_pos < x:
                        self.cpu.put_input(1)
                    else:
                        self.cpu.put_input(0)

                    self.ball_pos = x

        if visible:
            self.stdscr.clear()
            for j in range(25+1):
                for i in range(42+1):
                    id = self.screen[(i, j)]
                    if id == 0:
                        self.stdscr.addstr(j, i, ' ')
                    if id == 1:
                        self.stdscr.addstr(j, i, '|')
                    if id == 2:
                        self.stdscr.addstr(j, i, '#')
                    if id == 3:
                        self.stdscr.addstr(j, i, '_')
                    if id == 4:
                        self.stdscr.addstr(j, i, 'o')
                    if j == 0 and i == 42:
                        self.stdscr.addstr(j, i+1, f" Score: {self.current_score}")

            self.stdscr.refresh()

        self.out_buffer = []

    def play_game(self, visible=False):
        self.out_buffer = []
        if visible: self.stdscr = curses.initscr(); curses.curs_set(False)
        self.cpu.mem[0] = 2
        self.cpu.running = True
        self.out_buffer = self.cpu.exec_until_output(num=3*26*43)

        while self.cpu.running:
            self.cpu.exec_next()
            if not self.cpu.outs.empty():
                self.out_buffer.append(self.cpu.get_output())

            if len(self.out_buffer) >= 3:
                self.draw_screen(visible)
                if visible: sleep(0.001)

        if visible: curses.endwin()
        return self.current_score



arcade = Arcade(prog)
score = arcade.play_game(visible=False)
    
print(score)
# puzzle.answer_b = score