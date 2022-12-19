import math
from typing import Optional

from common.aoc import Task


class Day3(Task):
    def compute_part_one(self, version: str, right: int = 3, down: int = 1) -> str:
        grid = list(map(lambda s: list(s), self.load(version)))
        height = len(grid)
        width = len(grid[0])
        trees = 0

        for i in range(1, height):
            if ((down * i) < height) and ('#' == grid[(down * i)][(right * i) % width]):
                trees = trees + 1

        return str(trees)

    def compute_part_two(self, version: str) -> str:
        data = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
        runs = list(map(lambda a: int(self.compute_part_one(version, a[0], a[1])), data))

        return str(math.prod(runs))

    @property
    def part_one_expected_test_value(self) -> Optional[str]:
        return '7'

    @property
    def part_two_expected_test_value(self) -> Optional[str]:
        return '336'
