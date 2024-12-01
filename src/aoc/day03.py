import math

from src.aoc.day00 import Day00


class Day03(Day00):
    def compute_part_one_solution(self, version_identifier: str, right: int = 3, down: int = 1) -> str:
        grid = list(map(lambda s: list(s), self.input_data_as_lines(self.part_one_identifier, version_identifier)))
        height = len(grid)
        width = len(grid[0])
        trees = 0

        for i in range(1, height):
            if ((down * i) < height) and ('#' == grid[(down * i)][(right * i) % width]):
                trees = trees + 1

        return str(trees)

    def compute_part_two_solution(self, version_identifier: str) -> str:
        data = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
        runs = list(map(lambda a: int(self.compute_part_one_solution(version_identifier, a[0], a[1])), data))

        return str(math.prod(runs))
