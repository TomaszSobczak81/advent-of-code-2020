import os
import time


class Day00(object):
    __part_one_identifier = "one"
    __part_two_identifier = "two"

    __live_version_identifier = "live"
    __test_version_identifier = "test"

    def __init__(self, part_one_expected_result: str, part_two_expected_result: str):
        self.__part_one_expected_result = part_one_expected_result
        self.__part_two_expected_result = part_two_expected_result

    @property
    def part_one_identifier(self) -> str:
        return self.__part_one_identifier

    @property
    def part_two_identifier(self) -> str:
        return self.__part_two_identifier

    @property
    def live_version_identifier(self) -> str:
        return self.__live_version_identifier

    @property
    def test_version_identifier(self) -> str:
        return self.__test_version_identifier

    def solve(self):
        self.__solve_solution(self.part_one_identifier, self.__part_one_expected_result)
        self.__solve_solution(self.part_two_identifier, self.__part_two_expected_result)

    def __solve_solution(self, part_identifier: str, expected_result: str):
        self.__process_test_solution(part_identifier, expected_result)
        self.__process_live_solution(part_identifier)

    def __process_test_solution(self, part_identifier: str, expected_result: str):
        actual_result = self.__compute_solution(part_identifier, self.test_version_identifier)

        try:
            assert actual_result == expected_result
            print(f"Test passed for part {part_identifier}. Got {actual_result} as expected.")
        except AssertionError:
            print(f"Test failed for part {part_identifier}. Got {actual_result} instead of {expected_result}.")
            exit(0)

    def __process_live_solution(self, part_identifier: str):
        start = time.perf_counter()
        result = self.__compute_solution(part_identifier, self.live_version_identifier)
        timestamp = time.perf_counter() - start
        print(f"Solution for part {part_identifier}: {result} took {timestamp:.8f}s.")

    def __compute_solution(self, part_identifier: str, version_identifier: str) -> str:
        match part_identifier:
            case self.part_one_identifier:
                return self.compute_part_one_solution(version_identifier)
            case self.part_two_identifier:
                return self.compute_part_two_solution(version_identifier)
            case _:
                raise ValueError(f"Unknown part identifier {part_identifier}.")

    def compute_part_one_solution(self, version_identifier: str) -> str:
        return self.raw_input_data(self.part_one_identifier, version_identifier)

    def compute_part_two_solution(self, version_identifier: str) -> str:
        return self.raw_input_data(self.part_one_identifier, version_identifier)[::-1]

    def raw_input_data(self, part_identifier: str, version_identifier: str) -> str:
        file = '{path}/part_{part_identifier}.txt'.format(
            path=os.path.realpath(
                os.path.join(
                    os.path.dirname(os.path.realpath(__file__)),
                    '..',
                    '..',
                    'var',
                    'input',
                    version_identifier,
                    self.__module__.split('.')[-1]
                )
            ),
            part_identifier=part_identifier,
        )

        with open(file) as f:
            data = f.read()

        return data

    def lines_input_data(self, part_identifier: str, version_identifier: str) -> list:
        return self.raw_input_data(part_identifier, version_identifier).splitlines()

    def list_of_ints_input_data(self, part_identifier: str, version_identifier: str) -> list[int]:
        return [int(line) for line in self.lines_input_data(part_identifier, version_identifier)]
