#!/usr/bin/env python3
"""
    - Make sure to 'export AOC_SESSION=<your_aoc_token>'
    - Run the script in an ipython session using '%run <name>'
"""

from aocd.models import Puzzle
from typing import NamedTuple, List, Dict
from collections import Counter, defaultdict

# Enter year and day
puzzle = Puzzle(2021, 12)

data = puzzle.input_data
# data = """dc-end
# HN-start
# start-kj
# dc-start
# dc-HN
# LN-dc
# HN-end
# kj-sa
# kj-HN
# kj-dc"""
# data = """fs-end
# he-DX
# fs-he
# start-DX
# pj-DX
# end-zg
# zg-sl
# zg-pj
# pj-he
# RW-he
# fs-DX
# pj-RW
# zg-RW
# start-pj
# he-WI
# zg-he
# pj-fs
# start-RW"""

edges = [e.split('-') for e in data.split('\n')]
G = defaultdict(set)
for e in edges:
    G[e[0]].add(e[1])
    G[e[1]].add(e[0])

######################################################################
#   Part 1
######################################################################


def backtrack(node: str, path: list):
    if node == 'end':
        return 1
    if node.islower() and node in path[:-1]:
        return 0

    r = 0
    for n in G[node]:
        r += backtrack(n, path+[n])

    return r


answer = backtrack('start', ['start'])
print(answer)
# puzzle.answer_a = answer


######################################################################
#   Part 2
######################################################################


def backtrack2(node: str, path: list, twice: str):
    if len(path) > 1 and node == 'start':
        return 0
    if node == 'end':
        return 1

    # If the node is lowercase, check if there is a node twice.
    #   If there is one, and this node appears at least once before, stop the path
    if node.islower() and (twice is not None) and (node in path[:-1]):
        return 0
    
    # If there is no node twice, allow this node to be used twice
    if node.islower() and (twice is None) and (node in path[:-1]):
        twice = node

    r = 0
    for n in G[node]:
        r += backtrack2(n, path+[n], twice)

    return r


answer = backtrack2('start', ['start'], None)
print(answer)
# puzzle.answer_b = answer
