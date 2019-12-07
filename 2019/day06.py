#!/usr/bin/env python3
"""
    - Make sure to 'export AOC_SESSION=<your_aoc_token>'
    - Run the script in an ipython session using '%run <name>'
"""

from aocd.models import Puzzle
from typing import NamedTuple, List, Dict
from collections import Counter, defaultdict
from queue import Queue

# Enter year and day
puzzle = Puzzle(2019, 6)

data = puzzle.input_data
lines = data.split('\n')
######################################################################
#   Part 1
######################################################################

class Body(object):
    def __init__(self, name, parent, children):
        self.name = name
        self.parent = parent
        self.children = children

    def __repr__(self):
        return f"Body({self.name}, {self.parent}, {self.children})"

def parse(lines):
    pairs = [tuple(l.split(')')) for l in lines]
    return pairs

def build_tree(pairs):
    body_names = set([p[i] for i in range(2) for p in pairs])
    bodys = {}
    for bn in body_names:
        parent = [p for p,c in pairs if c == bn]
        if len(parent) > 0:
            parent = parent[0]
        else:
            parent = None
        children = [c for p,c in pairs if p == bn]
        bodys[bn] = Body(bn, parent, children)

    root = bodys['COM']
    stack = [root]
    while stack:
        current = stack.pop()
        current.children = [bodys[c] for c in current.children]
        stack.extend(current.children)

    return root, bodys

def num_total_orbits(body, depth):
    if body:
        res = 0
        for c in body.children:
            res += num_total_orbits(c, depth + 1)
        return res + depth
    return depth

test_inp = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L""".split('\n')

test_root, test_idx = build_tree(parse(test_inp))
assert num_total_orbits(test_root, 0) == 42

pairs = parse(lines)
root, tree_idx = build_tree(pairs)

print(num_total_orbits(root, 0))
# puzzle.answer_a = num_total_orbits(root, 0)


######################################################################
#   Part 2
######################################################################

def get_path_to_root(node, tree_idx):
    path = []
    while node.parent:
        path.append(node.parent)
        node = tree_idx[node.parent]
    return path

def get_len_shortest_path(n1, n2, tree_idx):
    p1 = set(get_path_to_root(n1, tree_idx))
    p2 = set(get_path_to_root(n2, tree_idx))

    return len(p1 ^ p2)

test_inp = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN""".split('\n')
test_root, test_idx = build_tree(parse(test_inp))
assert get_len_shortest_path(test_idx['YOU'], test_idx['SAN'], test_idx) == 4

print(get_len_shortest_path(tree_idx['YOU'], tree_idx['SAN'], tree_idx))
# puzzle.answer_b = get_len_shortest_path(tree_idx['YOU'], tree_idx['SAN'], tree_idx)