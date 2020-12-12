#!/usr/bin/env python3
"""
    - Make sure to 'export AOC_SESSION=<your_aoc_token>'
    - Run the script in an ipython session using '%run <name>'
"""

from aocd.models import Puzzle
from typing import NamedTuple, List, Dict
from collections import Counter, defaultdict

# Enter year and day
puzzle = Puzzle(2020, 11)

data = puzzle.input_data
# data = """#.##.##.##
# #######.##
# #.#.#..#..
# ####.##.##
# #.##.##.##
# #.#####.##
# ..#.#.....
# ##########
# #.######.#
# #.#####.##"""
grid = data.split('\n')
######################################################################
#   Part 1
######################################################################

G = {}
for y, l in enumerate(grid):
    for x, c in enumerate(l):
        G[(x, y)] = c

# for i, l in enumerate(G):
#     for j, c in enumerate(l):
#         if c == '.':
#             continue
#         n = G[i-1:i+2]
#         print(n)


def get_first_awnser():
    G1 = G.copy()
    G2 = {}
    changed = True
    while changed:
        G2 = G1.copy()
        changed = False
        for k, v in G1.items():
            if v == '.':
                continue
            else:
                o = 0
                for d in [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]:
                    adj_k = (k[0]+d[0], k[1]+d[1])
                    if adj_k in G1.keys() and G1[adj_k] == '#':
                        o += 1
                if v == 'L' and o == 0:
                    G2[k] = '#'
                    changed = True
                elif v == '#' and o > 3:
                    G2[k] = 'L'
                    changed = True
        G1 = G2.copy()

    return sum(1 for v in G1.values() if v == '#')


print(get_first_awnser())
# puzzle.answer_a = get_first_awnser()


######################################################################
#   Part 2
######################################################################

def get_second_awnser():
    G1 = G.copy()
    G2 = {}
    changed = True
    while changed:
        G2 = G1.copy()
        changed = False
        for k, v in G1.items():
            if v == '.':
                continue
            else:
                o = 0
                for dx, dy in [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]:
                    a = 1
                    adj_k = (k[0]+dx, k[1]+dy)
                    while adj_k in G1.keys() and G1[adj_k] == '.':
                        a += 1
                        adj_k = (k[0]+(dx*a), k[1]+(dy*a))
                    if adj_k in G1.keys() and G1[adj_k] == '#':
                        o += 1
                if v == 'L' and o == 0:
                    G2[k] = '#'
                    changed = True
                if v == '#' and o > 4:
                    G2[k] = 'L'
                    changed = True
        G1 = G2.copy()
    # print(G1)
    return sum(1 for v in G1.values() if v == '#')


print(get_second_awnser())
# puzzle.answer_b =
