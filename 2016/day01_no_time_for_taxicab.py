#!/usr/bin/env python3
"""
    - Run the script in an ipython session using '%run <name>'
    - Make sure to 'export AOC_SESSION=<your_aoc_token>'
"""

from aocd.models import Puzzle
from typing import List

# https://adventofcode.com/2016/day/1
puzzle = Puzzle(2016, 1)

data = puzzle.input_data
directions = data.split(", ")

######################################################################
#   Part 1
######################################################################

class Coord(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f"Coord({self.x}, {self.y})"

# State machine to keep track of direction to save a bunch of ifs
alph = "RL"
fsm = {'N':"EW", 'E':"SN", 'S':"WE", 'W':"NS"}
axis = {'x':{'E':1,'W':-1}, 'y':{'N':1,'S':-1}}


def follow_directions(directions: List[str], start_facing: str = 'N') -> Coord:
    pos = Coord(0, 0)
    facing = start_facing

    for d in directions:
        turn = alph.index(d[0])
        amount = int(d[1:])

        # turn around
        facing = fsm[facing][turn]
        # move
        if facing in axis['x']:
            pos.x += axis['x'][facing] * amount
        else:
            pos.y += axis['y'][facing] * amount
        
    return pos

def get_distance(directions: List[str]) -> int:
    end = follow_directions(directions)
    return abs(end.x) + abs(end.y)

assert get_distance(["R2", "L3"]) == 5
assert get_distance(["R2", "R2", "R2"]) == 2
assert get_distance(["R5", "L5", "R5", "R3"]) == 12

print(get_distance(directions))

# puzzle.awnser_a = get_distance(directions)


######################################################################
#   Part 2
######################################################################

def visit_twice(directions: List[str], start_facing: str = 'N') -> Coord:
    current_pos = Coord(0, 0)
    facing = start_facing

    seen_pos = {(0,0)}

    for d in directions:
        turn = alph.index(d[0])
        amount = int(d[1:])

        facing = fsm[facing][turn]
        if facing in axis['x']:
            new_pos = [(current_pos.x + axis['x'][facing]*a, current_pos.y)
                        for a in range(1, amount + 1)]
            
            if seen_pos.intersection(set(new_pos)):
                seen_twice = list(seen_pos.intersection(new_pos))[0]
                return Coord(seen_twice[0], seen_twice[1])

            seen_pos.update(new_pos)
            current_pos.x += axis['x'][facing] * amount
        else:
            new_pos = [(current_pos.x, current_pos.y + axis['y'][facing]*a)
                        for a in range(1, amount + 1)]

            if seen_pos.intersection(set(new_pos)):
                seen_twice = list(seen_pos.intersection(new_pos))[0]
                return Coord(seen_twice[0], seen_twice[1])

            seen_pos.update(new_pos)
            current_pos.y += axis['y'][facing] * amount

def get_distance_seen_twice(directions: List[str]) -> int:
    end = visit_twice(directions)
    assert end is not None
    return abs(end.x) + abs(end.y)

assert get_distance_seen_twice(["R8", "R4", "R4", "R8"]) == 4

print(get_distance_seen_twice(directions))

# puzzle.answer_b = get_distance_seen_twice(directions)