#!/usr/bin/env python3
"""
    - Make sure to 'export AOC_SESSION=<your_aoc_token>'
    - Run the script in an ipython session using '%run <name>'
"""

from aocd.models import Puzzle
from typing import NamedTuple, List, Dict
from collections import Counter, defaultdict
import re
# Enter year and day
puzzle = Puzzle(2020, 19)

data = puzzle.input_data
# data = """0: 4 1 5
# 1: 2 3 | 3 2
# 2: 4 4 | 5 5
# 3: 4 5 | 5 4
# 4: "a"
# 5: "b"

# ababbb
# bababa
# abbbab
# aaabbb
# aaaabbb"""
# data = """42: 9 14 | 10 1
# 9: 14 27 | 1 26
# 10: 23 14 | 28 1
# 1: "a"
# 11: 42 31
# 5: 1 14 | 15 1
# 19: 14 1 | 14 14
# 12: 24 14 | 19 1
# 16: 15 1 | 14 14
# 31: 14 17 | 1 13
# 6: 14 14 | 1 14
# 2: 1 24 | 14 4
# 0: 8 11
# 13: 14 3 | 1 12
# 15: 1 | 14
# 17: 14 2 | 1 7
# 23: 25 1 | 22 14
# 28: 16 1
# 4: 1 1
# 20: 14 14 | 1 15
# 3: 5 14 | 16 1
# 27: 1 6 | 14 18
# 14: "b"
# 21: 14 1 | 1 14
# 25: 1 1 | 1 14
# 22: 14 14
# 8: 42
# 26: 14 22 | 1 20
# 18: 15 15
# 7: 14 5 | 1 21
# 24: 14 1

# abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
# bbabbbbaabaabba
# babbbbaabbbbbabbbbbbaabaaabaaa
# aaabbbbbbaaaabaababaabababbabaaabbababababaaa
# bbbbbbbaaaabbbbaaabbabaaa
# bbbababbbbaaaaaaaabbababaaababaabab
# ababaaaaaabaaab
# ababaaaaabbbaba
# baabbaaaabbaaaababbaababb
# abbbbabbbbaaaababbbbbbaaaababb
# aaaaabbaabaaaaababaa
# aaaabbaaaabbaaa
# aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
# babaaabbbaaabaababbaabababaaab
# aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba"""
rules, lines = data.split('\n\n')
lines = lines.split('\n')
rules = {int(r.split(': ')[0]):r.split(': ')[1] for r in rules.split('\n')}
######################################################################
#   Part 1
######################################################################
def get_patterns(k):
  if type(k) is int and k in rules:
    r = rules[k]
    if r.startswith('"'):
      return r[1:-1]

    if r.find('|') == -1:
      keys = [int(x) for x in r.split()]
      return "".join([get_patterns(k) for k in keys])
    else:
      l,r = [[int(x) for x in s.split()] for s in r.split(' | ')]
      l_str = "".join([get_patterns(x) for x in l])
      r_str = "".join([get_patterns(x) for x in r])
      return f"({l_str}|{r_str})"

pattern = f"^{get_patterns(0)}$"
res = 0
for l in lines:
  if re.match(pattern, l):
    res += 1

print(res)
# puzzle.answer_a = 


######################################################################
#   Part 2
######################################################################

def get_patterns2(k):
  if type(k) is int and k in rules:
    r = rules[k]
    # print(k,r)
    if r.startswith('"'):
      return r[1:-1]

    if k == 8:
      keys = [int(x) for x in r.split()]
      return "".join([f"({get_patterns2(k)})+" for k in keys])
    if k == 11:
      k1,k2 = [int(x) for x in r.split()]
      s = "|".join([get_patterns2(k1)*i + get_patterns2(k2)*i for i in range(1,11)])
      return f"({s})"

    if r.find('|') == -1:
      keys = [int(x) for x in r.split()]
      return "".join([get_patterns2(k) for k in keys])
    else:
      l,r = [[int(x) for x in s.split()] for s in r.split(' | ')]
      l_str = "".join([get_patterns2(x) for x in l])
      r_str = "".join([get_patterns2(x) for x in r])
      return f"({l_str}|{r_str})"

pattern = f"^{get_patterns2(0)}$"
# print(pattern)
res = 0
for l in lines:
  if re.match(pattern, l):
    res += 1

print(res)
# puzzle.answer_b = 