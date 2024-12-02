from itertools import product

from src.aoc.day00 import Day00


class Day09(Day00):
    def compute_part_one_solution(self, version_identifier: str) -> str:
        transmission = self.input_data_as_lines_of_ints(
            self.part_one_identifier, version_identifier
        )
        preamble_len = 25 if version_identifier == self.live_version_identifier else 5

        for i in range(preamble_len, len(transmission)):
            if not self.is_valid_number(
                transmission[i], transmission[i - preamble_len : i]
            ):
                return str(transmission[i])

        raise Exception("No solution found")

    def is_valid_number(self, number: int, preamble: list[int]) -> bool:
        return number in [sum(pair) for pair in product(preamble, repeat=2)]

    def compute_part_two_solution(self, version_identifier: str) -> str:
        invalid_number = int(self.compute_part_one_solution(version_identifier))
        transmission = self.input_data_as_lines_of_ints(
            self.part_one_identifier, version_identifier
        )

        for i in range(len(transmission)):
            for j in range(i + 1, len(transmission)):
                contiguous_range = transmission[i:j]
                contiguous_range_sum = sum(contiguous_range)

                if contiguous_range_sum == invalid_number:
                    return str(min(contiguous_range) + max(contiguous_range))
                elif contiguous_range_sum > invalid_number:
                    break

        raise Exception("No solution found")
