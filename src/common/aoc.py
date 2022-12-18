import os.path
import time
from typing import Optional


class Task:
    def solve(self):
        try:
            self.check_solution(1, self.compute_part_one, self.part_one_expected_test_value)
            self.check_solution(2, self.compute_part_two, self.part_two_expected_test_value)

            self.solve_solution(1, self.compute_part_one)
            self.solve_solution(2, self.compute_part_two)
        except AssertionError as e:
            print(e)

    def load(self, version: str) -> list:
        file = '{path}_{version}.txt'.format(
            path=os.path.realpath(
                os.path.join(
                    os.path.dirname(os.path.realpath(__file__)),
                    '..',
                    '..',
                    'var',
                    'input',
                    self.__module__.split('.')[-1]
                )
            ),
            version=version
        )

        with open(file) as f:
            data = f.read().splitlines()

        return data

    def compute_part_one(self, version: str) -> str:
        raise NotImplementedError

    def compute_part_two(self, version: str) -> str:
        raise NotImplementedError

    @property
    def part_one_expected_test_value(self) -> Optional[str]:
        return None

    @property
    def part_two_expected_test_value(self) -> Optional[str]:
        return None

    @staticmethod
    def check_solution(part: int, func: callable, expected: str):
        result = func(version='test')
        assert result == expected, f'Test#{part} FAIL: Got {result} instead {expected}'

    @staticmethod
    def solve_solution(part: int, func: callable):
        start = time.perf_counter()
        result = func(version='live')
        timestamp = time.perf_counter() - start
        print(f'Part#{part} result: {result} computed in {timestamp:.8f}s')
