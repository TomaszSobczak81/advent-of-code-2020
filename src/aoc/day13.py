from math import prod

from src.aoc.day00 import Day00


class Day13(Day00):
    def compute_part_one_solution(self, version_identifier: str) -> str:
        planned_departure, schedule = self.__load_bus_schedule(version_identifier)
        schedule_buses = list(schedule.values())
        waiting_times = [bus - (planned_departure % bus) for bus in schedule_buses]

        return str(
            min(waiting_times) * schedule_buses[waiting_times.index(min(waiting_times))]
        )

    def compute_part_two_solution(self, version_identifier: str) -> str:
        _, schedule = self.__load_bus_schedule(version_identifier)
        return str(self.__chineese_remainder_theorem(schedule))

    def __chineese_remainder_theorem(self, schedule: dict[int, int]) -> int:
        m = prod(schedule.values())
        return (
            sum(
                -idx * (m // bus) * pow(m // bus, -1, bus)
                for idx, bus in schedule.items()
            )
            % m
        )

    def __load_bus_schedule(
        self, version_identifier: str
    ) -> tuple[int, dict[int, int]]:
        lines = self.input_data_as_lines(self.part_one_identifier, version_identifier)
        return int(lines[0]), {
            index: int(bus)
            for index, bus in enumerate(lines[1].split(","))
            if bus != "x"
        }
