from itertools import product
from typing import Optional

from common.aoc import Task


class Day1(Task):
    def compute_part_one(self, version: str) -> str:
        couples = self.load(version, 2)

        for a, b in couples:
            if 2020 == (int(a) + int(b)):
                return str(int(a) * int(b))

    def compute_part_two(self, version: str) -> str:
        triplets = self.load(version, 3)

        for a, b, c in triplets:
            if 2020 == (int(a) + int(b) + int(c)):
                return str(int(a) * int(b) * int(c))

    @property
    def part_one_expected_test_value(self) -> Optional[str]:
        return '514579'

    @property
    def part_two_expected_test_value(self) -> Optional[str]:
        return '241861950'

    def load(self, version: str, times: int) -> list:
        data = super().load(version)
        return list(product(*([data] * times)))
