import re
from typing import Optional

from common.aoc import Task


class Day2(Task):
    def compute_part_one(self, version: str) -> str:
        def validate_password(s: str):
            m = re.match("^([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)", s)

            return True if (int(m.group(1)) <= m.group(4).count(m.group(3)) <= int(m.group(2))) else False

        return str(len([p for p in self.load(version) if validate_password(p)]))

    def compute_part_two(self, version: str) -> str:
        def validate_password(s: str):
            m = re.match("^([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)", s)
            a = bool(m.group(4)[int(m.group(1)) - 1] == m.group(3))
            b = bool(m.group(4)[int(m.group(2)) - 1] == m.group(3))

            return a != b

        return str(len([p for p in self.load(version) if validate_password(p)]))

    @property
    def part_one_expected_test_value(self) -> Optional[str]:
        return '2'

    @property
    def part_two_expected_test_value(self) -> Optional[str]:
        return '1'
