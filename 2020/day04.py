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
puzzle = Puzzle(2020, 4)


data = puzzle.input_data
# data = """pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
# hcl:#623a2f

# eyr:2029 ecl:blu cid:129 byr:1989
# iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

# hcl:#888785
# hgt:164cm byr:2001 iyr:2015 cid:88
# pid:545766238 ecl:hzl
# eyr:2022

# iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"""
passports = data.split('\n\n')

######################################################################
#   Part 1
######################################################################


class Passport(NamedTuple):
    byr: int
    iyr: int
    eyr: int
    hgt: str
    hcl: str
    ecl: str
    pid: str
    cid: str

    def is_valid(self):
        r = sum([1 for x in self if x is not None])
        return r == 8 or r == 7 and self.cid is None

    def is_valid2(self):
        if self.byr is None or self.byr < 1920 or self.byr > 2002:
            return False

        if self.iyr is None or self.iyr < 2010 or self.iyr > 2020:
            return False

        if self.eyr is None or self.eyr < 2020 or self.eyr > 2030:
            return False

        if self.hgt is None or not self.hgt.endswith(('cm', 'in')):
            return False
        if self.hgt.endswith('cm'):
            cm = int(self.hgt[:-2])
            if cm < 150 or cm > 193:
                return False
        if self.hgt.endswith('in'):
            inch = int(self.hgt[:-2])
            if inch < 59 or inch > 76:
                return False

        if self.hcl is not None:
            m = re.match(r'^#[0-9a-f]{6}$', self.hcl)
            if m is None:
                return False
        else:
            return False

        if self.ecl is None or self.ecl not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            return False

        if self.pid is not None:
            pm = re.match(r'^[0-9]{9}$', self.pid)
            if not pm:
                return False
        else:
            return False
        return True

    @staticmethod
    def from_string(inp: str):
        data = re.split(r' |\n', inp)
        byr = iyr = eyr = hgt = hcl = ecl = pid = cid = None
        for e in data:
            k, v = e.split(':')
            if k == "byr":
                byr = int(v)
            elif k == "iyr":
                iyr = int(v)
            elif k == "eyr":
                eyr = int(v)
            elif k == "hgt":
                hgt = v
            elif k == "hcl":
                hcl = v
            elif k == "ecl":
                ecl = v
            elif k == "pid":
                pid = v
            elif k == "cid":
                cid = v

        return Passport(byr, iyr, eyr, hgt, hcl, ecl, pid, cid)


P = []
for p in passports:
    P.append(Passport.from_string(p))

res1 = sum([p.is_valid() for p in P])
print(res1)

# puzzle.answer_a = res1


######################################################################
#   Part 2
######################################################################

res2 = sum([p.is_valid2() for p in P])
print(res2)

# puzzle.answer_b = res2
