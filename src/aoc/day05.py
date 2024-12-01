from typing import Optional

from src.aoc.day00 import Day00


class Day05(Day00):
    def __init__(self, part_one_expected_result: str, part_two_expected_result: str):
        super(Day05, self).__init__(part_one_expected_result, part_two_expected_result)
        self.seat_ids = {
            self.live_version_identifier: [],
            self.test_version_identifier: []
        }

    def compute_part_one_solution(self, version_identifier: str) -> str:
        def calculate_seat_id(b: str) -> int:
            enc = list(b)
            row = list(range(128))
            col = list(range(8))

            for op in enc:
                match op:
                    case 'F':
                        row = row[:(len(row) // 2)]
                    case 'B':
                        row = row[(len(row) // 2):]
                    case 'L':
                        col = col[:(len(col) // 2)]
                    case 'R':
                        col = col[(len(col) // 2):]

            return int(row[0]) * 8 + int(col[0])

        seat_ids = [calculate_seat_id(b) for b in self.input_data_as_lines(self.part_one_identifier, version_identifier)]
        self.seat_ids[version_identifier] = seat_ids

        return str(max(seat_ids))

    def compute_part_two_solution(self, version_identifier: str) -> Optional[str]:
        seat_ids = self.seat_ids[version_identifier]
        seat_ids.sort()

        for seat_id in seat_ids:
            if seat_id + 1 not in seat_ids:
                return str(seat_id + 1)

        return None
