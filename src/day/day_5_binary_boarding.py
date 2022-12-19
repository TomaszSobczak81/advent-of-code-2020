from typing import Optional

from common.aoc import Task


class Day5(Task):
    def __init__(self):
        self.seat_ids = None

    def compute_part_one(self, version: str) -> str:
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

        self.seat_ids = [calculate_seat_id(b) for b in self.load(version)]

        return str(max(self.seat_ids))

    def compute_part_two(self, version: str) -> Optional[str]:
        self.seat_ids.sort()

        for seat_id in self.seat_ids:
            if seat_id + 1 not in self.seat_ids:
                return str(seat_id + 1)

        return None

    @property
    def part_one_expected_test_value(self) -> Optional[str]:
        return '357'

    @property
    def part_two_expected_test_value(self) -> Optional[str]:
        return '358'
