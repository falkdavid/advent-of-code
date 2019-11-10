#!/usr/bin/env python3
"""
    - Run the script in an ipython session using '%run <name>'
    - Make sure to 'export AOC_SESSION=<your_aoc_token>'
"""

from aocd.models import Puzzle
from typing import List, NamedTuple
from collections import Counter
import re

# https://adventofcode.com/2016/day/3
puzzle = Puzzle(2016, 4)

data = puzzle.input_data
room_data = data.split('\n')
######################################################################
#   Part 1
######################################################################

class Room(NamedTuple):
    string: str
    letters: str
    room_id: int
    checksum: str

    def real(self):
        c = Counter(self.letters)
        s = sorted(c.most_common(), key=lambda x: (-x[1], x[0]))[:5]
        return "".join([x[0] for x in s]) == self.checksum

def get_rooms(room_list: List[str]) -> List[Room]:
    rooms = []
    for r in room_list:
        parts = r.split('-')
        string = " ".join(parts[:-1])
        room_id, checksum = re.match(r"([0-9]+)\[(.*)\]", parts[-1]).groups()
        letters = "".join(parts[:-1])
        rooms.append(Room(string, letters, int(room_id), checksum))

    return rooms

def get_real_rooms(rooms: List[Room]) -> List[Room]:
    return [r for r in rooms if r.real()] 

def get_sector_sum(rooms: List[Room]) -> int:
    return sum([r.room_id for r in rooms])


test_rooms = get_rooms(["aaaaa-bbb-z-y-x-123[abxyz]",
                        "a-b-c-d-e-f-g-h-987[abcde]",
                        "not-a-real-room-404[oarel]",
                        "totally-real-room-200[decoy]"])

assert test_rooms[0].real()
assert get_sector_sum(get_real_rooms(test_rooms)) == 1514

rooms = get_rooms(room_data)
print(get_sector_sum(get_real_rooms(rooms)))

# puzzle.answer_a = get_sector_sum(get_real_rooms(rooms))


######################################################################
#   Part 2
######################################################################


def decrypt(cipher: str, shift: int) -> str:
    words = cipher.split(' ')
    decrypted_words = []
    for w in words:
        w = "".join([chr((((ord(c) - ord('a')) + shift) % 26) + ord('a'))
                     for c in w])
        decrypted_words.append(w)
    return " ".join(decrypted_words)

def get_north_pole_room_id(rooms: List[Room]) -> int:
    decrypted_rooms = [(decrypt(r.string, r.room_id), r.room_id) 
                        for r in rooms]
    for ws, id in decrypted_rooms:
        if 'north' in ws or 'pole' in ws:
            return id

assert decrypt("qzmt zixmtkozy ivhz", 343) == "very encrypted name"

print(get_north_pole_room_id(rooms))
# puzzle.answer_b = get_north_pole_room_id(rooms)