#!/usr/bin/env python3
"""
    - Run the script in an ipython session using '%run <name>'
    - Make sure to 'export AOC_SESSION=<your_aoc_token>'
"""

from aocd.models import Puzzle
from typing import NamedTuple, List
import re

# https://adventofcode.com/2016/day/7
puzzle = Puzzle(2016, 7)

data = puzzle.input_data
lines = data.split('\n')
######################################################################
#   Part 1
######################################################################

class IP(NamedTuple):
    supernet: List[str]
    hypernets: List[str]

    def supports_tls(self) -> bool:
        if any([find_abba(st) for st in self.supernet]) and \
            not any([find_abba(st) for st in self.hypernets]):
            return True
        return False

    def supports_ssl(self) -> bool:
        super_aba = [get_all_aba(st) for st in self.supernet]
        super_aba = [x for sa in super_aba for x in sa if x]
        hyper_aba = [get_all_aba(hy) for hy in self.hypernets]
        hyper_aba = [aba_to_bab(x) for ha in hyper_aba for x in ha if x]
        if any([aba in hyper_aba for aba in super_aba]):
            return True
        return False

def find_abba(inp: str) -> bool:
    if len(inp) < 4:
        return False
    for i in range(0, len(inp)-3):
        check = inp[i:i+4]
        if str(check) == str(check[::-1]) \
            and check[0] != check[1]:
            return True
    return False

def get_all_ips(lines: List[str]) -> List[IP]:
    ips = []
    for l in lines:
        hypernets = re.findall(r'\[([a-z]*)\]', l)
        supernet = re.sub(r'\[([a-z]*)\]', ",", l).split(',')
        ips.append(IP(supernet, hypernets))
    return ips

def get_ips_tls(ips: List[IP]) -> List[IP]:
    return [ip for ip in ips if ip.supports_tls()]

assert find_abba("a") == False
assert find_abba("aaaa") == False
assert find_abba("abba") == True
assert find_abba("klojjo") == True

test_lines = """abba[mnop]qrst
abcd[bddb]xyyx
aaaa[qwer]tyui
ioxxoj[asdfgh]zxcvbn""".split('\n')

test_ips = get_all_ips(test_lines)

assert test_ips[0].supports_tls() == True
assert test_ips[1].supports_tls() == False
assert test_ips[2].supports_tls() == False
assert test_ips[3].supports_tls() == True

ips = get_all_ips(lines)

print(len(get_ips_tls(ips)))

# puzzle.answer_a = len(get_ips_tls(ips))


######################################################################
#   Part 2
######################################################################

def aba_to_bab(inp: str) -> str:
    if len(inp) < 3:
        return None
    return inp[1] + inp[0] + inp[1]

def get_all_aba(inp: str) -> List[str]:
    if len(inp) < 3:
        return []
    abas = []
    for i in range(0, len(inp)-2):
        check = inp[i:i+3]
        if str(check) == str(check[::-1]) \
            and check[0] != check[1]:
            abas.append(check)
    return abas

def get_ips_ssl(ips: List[IP]) -> List[IP]:
    return [ip for ip in ips if ip.supports_ssl()]

test_lines = """aba[bab]xyz
xyx[xyx]xyx
aaa[kek]eke
zazbz[bzb]cdb""".split('\n')

test_ips = get_all_ips(test_lines)

assert test_ips[0].supports_ssl() == True
assert test_ips[1].supports_ssl() == False
assert test_ips[2].supports_ssl() == True
assert test_ips[3].supports_ssl() == True

ips = get_all_ips(lines)

print(len(get_ips_ssl(ips)))

# puzzle.answer_b = len(get_ips_ssl(ips))