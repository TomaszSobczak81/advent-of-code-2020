from itertools import product

from src.aoc.day00 import Day00


class Day01(Day00):
    def compute_part_one_solution(self, version_identifier: str) -> str:
        couples = self.__input_data(self.part_one_identifier, version_identifier, 2)

        for a, b in couples:
            if 2020 == (int(a) + int(b)):
                return str(int(a) * int(b))

    def compute_part_two_solution(self, version_identifier: str) -> str:
        triplets = self.__input_data(self.part_one_identifier, version_identifier, 3)

        for a, b, c in triplets:
            if 2020 == (int(a) + int(b) + int(c)):
                return str(int(a) * int(b) * int(c))

    def __input_data(
        self, part_identifier: str, version_identifier: str, repeatitions: int
    ) -> list:
        data = self.input_data_as_lines(part_identifier, version_identifier)
        return list(product(*([data] * repeatitions)))
