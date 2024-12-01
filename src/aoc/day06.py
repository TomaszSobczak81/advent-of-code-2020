from src.aoc.day00 import Day00


class Day06(Day00):
    def compute_part_one_solution(self, version_identifier: str) -> str:
        forms = []
        yeses = 0

        for line in self.input_data_as_lines(self.part_one_identifier, version_identifier):
            if not line:
                yeses += len(set(forms))
                forms = []
                continue

            forms += list(line)

        if forms:
            yeses += len(set(forms))

        return str(yeses)

    def compute_part_two_solution(self, version_identifier: str) -> str:
        forms = []
        yeses = 0

        for line in self.input_data_as_lines(self.part_one_identifier, version_identifier):
            if not line:
                yeses += len(set.intersection(*forms))
                forms = []
                continue

            forms.append(set(line))

        if forms:
            yeses += len(set.intersection(*forms))

        return str(yeses)
