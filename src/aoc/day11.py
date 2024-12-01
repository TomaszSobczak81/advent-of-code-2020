import copy
from itertools import product

from src.aoc.day00 import Day00


class Day11(Day00):
    def compute_part_one_solution(self, version_identifier: str) -> str:
        seats = self.input_data_as_grid(self.part_one_identifier, version_identifier)
        return str(self.simulate_seats_behaviour(seats, long_range_adjacent_search=False, maximum_occupied_seats=4))

    def compute_part_two_solution(self, version_identifier: str) -> str:
        seats = self.input_data_as_grid(self.part_one_identifier, version_identifier)
        return str(self.simulate_seats_behaviour(seats, long_range_adjacent_search=True, maximum_occupied_seats=5))

    def simulate_seats_behaviour(self, seats: list[list[str]], long_range_adjacent_search: bool,
                                 maximum_occupied_seats: int) -> int:
        seats_occupied = sum([row.count("#") for row in seats])

        while True:
            seats = self.process_seats_with_rules(seats, long_range_adjacent_search, maximum_occupied_seats)
            seats_occupied_new = sum([row.count("#") for row in seats])

            if seats_occupied == seats_occupied_new:
                break

            seats_occupied = seats_occupied_new

        return seats_occupied

    def process_seats_with_rules(self, seats: list[list[str]], long_range_adjacent_search: bool,
                                 maximum_occupied_seats: int) -> list[list[str]]:
        seats_copy = copy.deepcopy(seats)

        for (x, y) in product(range(0, len(seats[0])), range(0, len(seats))):
            # Floor (.) never changes
            if seats[y][x] == ".":
                continue

            match long_range_adjacent_search:
                case True:
                    adjacent_seats = self.long_range_adjacent_seats(seats, x, y)
                case _:
                    adjacent_seats =  self.immediately_adjacent_seats(seats, x, y)

            # If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied
            if seats[y][x] == "L" and "#" not in adjacent_seats:
                seats_copy[y][x] = "#"

            # If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty
            elif seats[y][x] == "#" and adjacent_seats.count("#") >= maximum_occupied_seats:
                seats_copy[y][x] = "L"

        return seats_copy

    @staticmethod
    def immediately_adjacent_seats(grid: list, x: int, y: int) -> list[str]:
        grid_cells = []
        grid_width = len(grid[0])
        grid_height = len(grid)

        for (i, j) in product([-1, 0, 1], repeat=2):
            if i == 0 and j == 0:
                continue

            if 0 <= (x + i) < grid_width and 0 <= (y + j) < grid_height:
                grid_cells.append(grid[y + j][x + i])

        return grid_cells

    @staticmethod
    def long_range_adjacent_seats(grid: list, x: int, y: int) -> list[str]:
        grid_cells = []
        grid_width = len(grid[0])
        grid_height = len(grid)

        for (i, j) in product([-1, 0, 1], repeat=2):
            if i == 0 and j == 0:
                continue

            for distance in range(1, max(grid_width, grid_height)):
                x_offset = x + (i * distance)
                y_offset = y + (j * distance)

                if 0 <= x_offset < grid_width and 0 <= y_offset < grid_height:
                    if grid[y_offset][x_offset] != ".":
                        grid_cells.append(grid[y_offset][x_offset])
                        break

        return grid_cells
