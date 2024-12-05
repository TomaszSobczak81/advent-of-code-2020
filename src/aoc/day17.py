from itertools import product

from src.aoc.day00 import Day00


class Day17(Day00):
    ACTIVE = "#"
    INACTIVE = "."

    def compute_part_one_solution(self, version_identifier: str) -> str:
        space = self.__load_initial_space(version_identifier)
        state = self.__simulate_energy_source(space, 6)

        return str(sum([x.count(self.ACTIVE) for y in state for x in y]))

    def compute_part_two_solution(self, version_identifier: str) -> str:
        space = self.__load_hyper_space(version_identifier)
        state = self.__simulate_energy_source_in_hyper_space(space, 6)

        return str(sum([x.count(self.ACTIVE) for z in state for y in z for x in y]))

    def __load_initial_space(self, version_identifier: str) -> list[list[list[str]]]:
        return [self.input_data_as_grid(self.part_one_identifier, version_identifier)]

    def __simulate_energy_source(
        self, space: list[list[list[str]]], cycles: int
    ) -> list[list[list[str]]]:
        for _ in range(cycles):
            space = self.__simulate_cycle(space)
        return space

    def __simulate_cycle(self, space: list[list[list[str]]]) -> list[list[list[str]]]:
        return [
            [
                [
                    self.__simulate_cube(space, x - 1, y - 1, z - 1)
                    for x in range(len(space[0][0]) + 2)  # x
                ]
                for y in range(len(space[0]) + 2)  # y
            ]
            for z in range(len(space) + 2)  # z
        ]

    def __simulate_cube(
        self, space: list[list[list[str]]], x: int, y: int, z: int
    ) -> str:
        active_neighbors = 0

        for a, b, c in product([x - 1, x, x + 1], [y - 1, y, y + 1], [z - 1, z, z + 1]):
            if a == x and b == y and c == z:
                continue
            active_neighbors += self.__is_active(space, a, b, c)

        if self.__is_active(space, x, y, z):
            return self.ACTIVE if active_neighbors in [2, 3] else self.INACTIVE

        return self.ACTIVE if active_neighbors == 3 else self.INACTIVE

    def __is_active(self, space: list[list[list[str]]], x: int, y: int, z: int) -> bool:
        return (
            False
            if any(
                [
                    x < 0,
                    y < 0,
                    z < 0,
                    x >= len(space[0][0]),
                    y >= len(space[0]),
                    z >= len(space),
                ]
            )
            else space[z][y][x] == self.ACTIVE
        )

    def __load_hyper_space(
        self, version_identifier: str
    ) -> list[list[list[list[str]]]]:
        return [self.__load_initial_space(version_identifier)]

    def __simulate_energy_source_in_hyper_space(
        self, space: list[list[list[list[str]]]], cycles: int
    ) -> list[list[list[list[str]]]]:
        for _ in range(cycles):
            space = self.__simulate_hyper_cycle(space)
        return space

    def __simulate_hyper_cycle(
        self, space: list[list[list[list[str]]]]
    ) -> list[list[list[list[str]]]]:
        return [
            [
                [
                    [
                        self.__simulate_hyper_cube(space, x - 1, y - 1, z - 1, w - 1)
                        for x in range(len(space[0][0][0]) + 2)  # x
                    ]
                    for y in range(len(space[0][0]) + 2)  # y
                ]
                for z in range(len(space[0]) + 2)  # z
            ]
            for w in range(len(space) + 2)  # w
        ]

    def __simulate_hyper_cube(
        self, space: list[list[list[list[str]]]], x: int, y: int, z: int, w: int
    ) -> str:
        active_neighbors = 0

        for a, b, c, d in product(
            [x - 1, x, x + 1], [y - 1, y, y + 1], [z - 1, z, z + 1], [w - 1, w, w + 1]
        ):
            if a == x and b == y and c == z and d == w:
                continue
            active_neighbors += self.__is_hyper_active(space, a, b, c, d)

        if self.__is_hyper_active(space, x, y, z, w):
            return self.ACTIVE if active_neighbors in [2, 3] else self.INACTIVE

        return self.ACTIVE if active_neighbors == 3 else self.INACTIVE

    def __is_hyper_active(
        self, space: list[list[list[list[str]]]], x: int, y: int, z: int, w: int
    ) -> bool:
        return (
            False
            if any(
                [
                    x < 0,
                    y < 0,
                    z < 0,
                    w < 0,
                    x >= len(space[0][0][0]),
                    y >= len(space[0][0]),
                    z >= len(space[0]),
                    w >= len(space),
                ]
            )
            else space[w][z][y][x] == self.ACTIVE
        )
