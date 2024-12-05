from src.aoc.day00 import Day00


class Day15(Day00):
    def compute_part_one_solution(self, version_identifier: str) -> str:
        return self.__compute_solution_with_rounds(version_identifier, 2020)

    def compute_part_two_solution(self, version_identifier: str) -> str:
        return self.__compute_solution_with_rounds(version_identifier, 30000000)

    def __compute_solution_with_rounds(
        self, version_identifier: str, rounds: int
    ) -> str:
        game_numbers = self.starting_numbers(version_identifier)
        used_numbers = {number: turn + 1 for turn, number in enumerate(game_numbers)}
        last_number = game_numbers[-1]

        for turn in range(len(game_numbers), rounds):
            used_numbers[last_number], last_number = turn, (
                0
                if last_number not in used_numbers
                else turn - used_numbers[last_number]
            )

        return str(last_number)

    def starting_numbers(self, version_identifier: str) -> list[int]:
        return [
            int(x)
            for x in self.input_data_as_lines(
                self.part_one_identifier, version_identifier
            )[0].split(",")
        ]
