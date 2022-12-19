import re
from typing import Optional

from common.aoc import Task


class Day4(Task):
    def __init__(self):
        self.passports = None

    def compute_part_one(self, version: str) -> str:
        def validate_passport(d: dict) -> int:
            if 8 == len(d) or (7 == len(d) and 'cid' not in d):
                return 1
            return 0

        self.passports = self.load_passports_data(version)
        validated = [validate_passport(p) for p in self.passports]

        return str(sum(validated))

    def compute_part_two(self, version: str) -> str:
        def validate_passport(d: dict) -> int:
            valid = 8 == len(d) or (7 == len(d) and 'cid' not in d)
            valid = valid and bool(re.match(r"^\d{4}$", d['byr'])) and (1920 <= int(d['byr']) <= 2002)
            valid = valid and bool(re.match(r"^\d{4}$", d['iyr'])) and (2010 <= int(d['iyr']) <= 2020)
            valid = valid and bool(re.match(r"^\d{4}$", d['eyr'])) and (2020 <= int(d['eyr']) <= 2030)

            hgt = re.match(r"^(\d+)(cm|in)$", d['hgt']) if valid else False

            if valid and bool(hgt):
                hgt_min = 150 if 'cm' == hgt.group(2) else 59
                hgt_max = 193 if 'cm' == hgt.group(2) else 76
                valid = valid and bool(hgt) and (hgt_min <= int(hgt.group(1)) <= hgt_max)

            valid = valid and bool(hgt)
            valid = valid and bool(re.match(r"^#[\da-f]{6}$", d['hcl']))
            valid = valid and bool(re.match(r"^amb|blu|brn|gry|grn|hzl|oth$", d['ecl']))
            valid = valid and bool(re.match(r"^\d{9}$", d['pid']))

            return 1 if valid else 0

        validated = [validate_passport(p) for p in self.passports]

        return str(sum(validated))

    @property
    def part_one_expected_test_value(self) -> Optional[str]:
        return '2'

    @property
    def part_two_expected_test_value(self) -> Optional[str]:
        return '2'

    def load_passports_data(self, version) -> list:
        current = []
        rawdata = []
        outdata = []

        for line in self.load(version):
            if 0 == len(line):
                rawdata.append(re.split(r"\s+", ' '.join(current)))
                current = []
                continue

            current.append(line)
        rawdata.append(re.split(r"\s+", ' '.join(current)))

        for d in rawdata:
            outdata.append({s.split(':')[0]: s.split(':')[1] for s in d})

        return outdata
