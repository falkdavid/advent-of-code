#!/usr/bin/env python3
"""
    - Make sure to 'export AOC_SESSION=<your_aoc_token>'
    - Run the script in an ipython session using '%run <name>'
"""

from aocd.models import Puzzle
from typing import NamedTuple, List, Dict
from collections import Counter, defaultdict, deque
import heapq
import math

# Enter year and day
puzzle = Puzzle(2021, 15)

data = puzzle.input_data
# data = """1163751742
# 1381373672
# 2136511328
# 3694931569
# 7463417111
# 1319128137
# 1359912421
# 3125421639
# 1293138521
# 2311944581"""
numbers = [[int(d) for d in l] for l in data.split('\n')]

C = defaultdict(int)
for y, row in enumerate(numbers):
    for x, d in enumerate(row):
        C[(x, y)] = d

######################################################################
#   Part 1
######################################################################


def print_grid(G: dict):
    for y in range(max(G.keys())[1]+1):
        print("".join([str(G[(x, y)]) for x in range(max(G.keys())[0]+1)]))
    print()


def get_min_cost_map(C: dict, start: tuple):
    P = defaultdict(lambda: math.inf)
    P[start] = 0
    Q = []
    heapq.heappush(Q, (0, start))
    while Q:
        _, curr_pos = heapq.heappop(Q)

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            next_pos = (curr_pos[0] + dx, curr_pos[1] + dy)
            if next_pos in C.keys() and P[next_pos] > (P[curr_pos] + C[next_pos]):
                P[next_pos] = P[curr_pos] + C[next_pos]
                heapq.heappush(Q, (P[next_pos], next_pos))
    return P

start = (min(C.keys()))
end = (max(C.keys()))
Cmin = get_min_cost_map(C, start)
print(Cmin[end])
# puzzle.answer_a = Cmin[end]


######################################################################
#   Part 2
######################################################################

def get_big_cost_map(C: dict):
    end = (max(C.keys()))
    width = end[0] + 1
    height = end[1] + 1

    Cbig = defaultdict(int)
    for i in range(5):
        for j in range(5):
            for x, y in C.keys():
                xx = j * width + x
                yy = i * height + y
                val = C[(x, y)] + i + j
                val = val if val < 10 else val - (val//9 * 9)
                Cbig[(xx, yy)] = val

    return Cbig


Cbig = get_big_cost_map(C)

start2 = (min(Cbig.keys()))
end2 = (max(Cbig.keys()))
Cmin2 = get_min_cost_map(Cbig, start2)
print(Cmin2[end2])
# puzzle.answer_b = Cmin2[end2]
