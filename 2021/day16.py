#!/usr/bin/env python3
"""
    - Make sure to 'export AOC_SESSION=<your_aoc_token>'
    - Run the script in an ipython session using '%run <name>'
"""

from functools import reduce
from aocd.models import Puzzle
from typing import NamedTuple, List, Dict
from collections import Counter, defaultdict

# Enter year and day
puzzle = Puzzle(2021, 16)

data = puzzle.input_data
# data = """D2FE28"""
# data = """38006F45291200"""
# data = """EE00D40C823060"""
# data = """A0016C880162017C3686B18A3D4780"""
# data = """04005AC33890"""
######################################################################
#   Part 1
######################################################################


class Literal(NamedTuple):
    version: int
    type_id: int
    length: int
    data: int


class Operator(NamedTuple):
    version: int
    type_id: int
    length: int
    data: list


def hex2bin(s: str):
    r = ["{0:04b}".format(int(c, 16)) for c in s]
    return "".join(r)


def decode_packet(packet: str, hex: bool = True):
    if hex:
        packet = hex2bin(packet)

    header = packet[:6]
    data = packet[6:]
    version = int(header[:3], 2)
    type_id = int(header[3:], 2)
    # print(version, type_id, len(packet))

    num_bits = 6
    # Literal value
    if type_id == 4:
        literal = ""
        for i in range(0, len(data), 5):
            sl = data[i:i+5]
            literal += sl[1:]
            num_bits += 5
            if sl.startswith('0'):
                break

        return Literal(version, type_id, num_bits, int(literal, 2))
    # Operator type
    else:
        length_id = int(data[0], 2)
        if length_id == 0:
            total_bits = int(data[1:16], 2)
            packet_data = data[16:16+total_bits]
            num_bits += 16 + total_bits

            i = 0
            d = []
            while i < total_bits:
                p = decode_packet(packet_data, hex=False)
                d.append(p)
                i += p.length
                packet_data = packet_data[p.length:]

            return Operator(version, type_id, num_bits, d)
        else:
            number_packets = int(data[1:12], 2)
            packet_data = data[12:]
            num_bits += 12

            d = []
            for i in range(number_packets):
                p = decode_packet(packet_data, hex=False)
                d.append(p)
                packet_data = packet_data[p.length:]
                num_bits += p.length

            return Operator(version, type_id, num_bits, d)


def get_sum_version(packet):
    if type(packet) is Literal:
        return packet.version
    elif type(packet) is Operator:
        return packet.version + sum([get_sum_version(p) for p in packet.data])


P = decode_packet(data)
awnser = get_sum_version(P)
print(awnser)
# puzzle.answer_a = awnser

######################################################################
#   Part 2
######################################################################

def execute_packet(packet):
    if type(packet) is Literal:
        return packet.data
    elif type(packet) is Operator:
        if packet.type_id == 0:
            return sum([execute_packet(p) for p in packet.data])
        elif packet.type_id == 1:
            return reduce(lambda a, b: a*b, [execute_packet(p) for p in packet.data])
        elif packet.type_id == 2:
            return min([execute_packet(p) for p in packet.data])
        elif packet.type_id == 3:
            return max([execute_packet(p) for p in packet.data])
        elif packet.type_id == 5:
            return execute_packet(packet.data[0]) > execute_packet(packet.data[1])
        elif packet.type_id == 6:
            return execute_packet(packet.data[0]) < execute_packet(packet.data[1])
        elif packet.type_id == 7:
            return execute_packet(packet.data[0]) == execute_packet(packet.data[1])

awnser = execute_packet(P)
print(awnser)
# puzzle.answer_b =
