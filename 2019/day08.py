#!/usr/bin/env python3
"""
    - Make sure to 'export AOC_SESSION=<your_aoc_token>'
    - Run the script in an ipython session using '%run <name>'
"""

from aocd.models import Puzzle
from typing import NamedTuple, List, Dict
from collections import Counter, defaultdict
import numpy as np

# Enter year and day
puzzle = Puzzle(2019, 8)

data = puzzle.input_data
width = 25
height = 6
num_layers = 100
######################################################################
#   Part 1
######################################################################

def get_layers(data, width, height, num_layers):
    i = 0
    while data[i:i+width*height] != '':
        yield data[i:i+width*height]
        i += width * height

def get_checksum(data, width, height, num_layers):
    best_c = 100
    best_l = ""
    for l in get_layers(data, width, height, num_layers):
        assert l != ""
        if l.count('0') < best_c:
            best_c = l.count('0')
            best_l = l

    return best_l.count('1') * best_l.count('2')

print(get_checksum(data, width, height, num_layers))
# puzzle.answer_a = get_checksum(data, width, height, num_layers)


######################################################################
#   Part 2
######################################################################

def decode(data, width, height, num_layers):
    image = get_layers(data, width, height, num_layers)
    image = [[l[r*width:(r+1)*width] for r in range(height)] for l in image]
    
    res = []
    r = 0
    c = 0
    for r in range(height):
        s = ""
        for c in range(width):
            color = None
            for layer in image:
                if layer[r][c] == '2':
                    continue
                else:
                    color = layer[r][c]
                    break

            s += color
            
        res.append(s)

    return res

def print_image(image):
    for r in image:
        print(r.replace('0', ' ').replace('1', '#'))

#test_image = decode('0222112222120000', 2, 2, 2)
#print_image(test_image)
image = decode(data, width, height, num_layers)
print_image(image)
# puzzle.answer_b = "LJECH"