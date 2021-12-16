#!/usr/bin/env python3
"""
    - Make sure to 'export AOC_SESSION=<your_aoc_token>'
    - Run the script in an ipython session using '%run <name>'
"""

from aocd.models import Puzzle
from typing import NamedTuple, List, Dict
from collections import Counter, defaultdict

# Enter year and day
puzzle = Puzzle(2021, 11)

data = puzzle.input_data
# data = """5483143223
# 2745854711
# 5264556173
# 6141336146
# 6357385478
# 4167524645
# 2176841721
# 6882881134
# 4846848554
# 5283751526"""
lines = data.split('\n')
######################################################################
#   Part 1
######################################################################

def get_grid(lines):
    G = defaultdict(int)
    for y, l in enumerate(lines):
        for x, d in enumerate(l):
            G[(x, y)] = int(d)
    return G

def print_grid(G: dict):
    for y in range(10):
        print("".join([str(G[(x, y)]) for x in range(10)]))
    print()

def iter_neighbor_cells(G, pos):
    for x in range(pos[0]-1, pos[0]+2):
        for y in range(pos[1]-1, pos[1]+2):
            if (x, y) != pos and (x, y) in G.keys():
                yield (x, y)

def handle_flashes(G: dict):
    flash = set()
    while any([v > 9 for v in G.values()]):
        for k,v in G.items():
            if v > 9:
                flash.add(k)
                for kn in iter_neighbor_cells(G, k):
                    if kn not in flash:
                        G[kn] += 1
                G[k] = 0
    return len(flash)

G = get_grid(lines)

awnser = 0
for step in range(100):
    for k,v in G.items():
        G[k] = v+1

    awnser += handle_flashes(G)

print(awnser)
# puzzle.answer_a = awnser

######################################################################
#   Part 2
######################################################################

G = get_grid(lines)

def find_simul_flash(G, limit=1000):
    for i in range(limit):
        for k,v in G.items():
            G[k] = v+1
        if handle_flashes(G) == 100:
            return i + 1

awnser = find_simul_flash(G)
print(awnser)
# puzzle.answer_b = awnser
