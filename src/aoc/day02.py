import re

from src.aoc.day00 import Day00


class Day02(Day00):
    def compute_part_one_solution(self, version_identifier: str) -> str:
        def validate_password(s: str):
            m = re.match("^([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)", s)

            return True if (int(m.group(1)) <= m.group(4).count(m.group(3)) <= int(m.group(2))) else False

        data = self.input_data_as_lines(self.part_one_identifier, version_identifier)
        return str(len([p for p in data if validate_password(p)]))

    def compute_part_two_solution(self, version_identifier: str) -> str:
        def validate_password(s: str):
            m = re.match("^([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)", s)
            a = bool(m.group(4)[int(m.group(1)) - 1] == m.group(3))
            b = bool(m.group(4)[int(m.group(2)) - 1] == m.group(3))

            return a != b

        data = self.input_data_as_lines(self.part_one_identifier, version_identifier)
        return str(len([p for p in data if validate_password(p)]))
