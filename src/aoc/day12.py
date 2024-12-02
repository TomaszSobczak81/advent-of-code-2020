from src.aoc.day00 import Day00


class Day12(Day00):
    def compute_part_one_solution(self, version_identifier: str) -> str:
        def __move_ship_towards(
            location: dict[str, int], direction: str, distance: int
        ) -> dict[str, int]:
            match direction:
                case "N":
                    location["y"] += distance
                case "S":
                    location["y"] -= distance
                case "E":
                    location["x"] += distance
                case "W":
                    location["x"] -= distance

            return location

        def __rotate_ship(direction: str, rotation: str, degrees: int) -> str:
            return {
                "NL": {90: "W", 180: "S", 270: "E"},
                "NR": {90: "E", 180: "S", 270: "W"},
                "EL": {90: "N", 180: "W", 270: "S"},
                "ER": {90: "S", 180: "W", 270: "N"},
                "SL": {90: "E", 180: "N", 270: "W"},
                "SR": {90: "W", 180: "N", 270: "E"},
                "WL": {90: "S", 180: "E", 270: "N"},
                "WR": {90: "N", 180: "E", 270: "S"},
            }[direction + rotation][degrees]

        ship_direction = "E"
        ship_location = {"x": 0, "y": 0}

        for command, value in self.load_ship_instructions(version_identifier):
            match command:
                case "L" | "R":
                    ship_direction = __rotate_ship(ship_direction, command, value)
                case "F":
                    ship_location = __move_ship_towards(
                        ship_location, ship_direction, value
                    )
                case _:
                    ship_location = __move_ship_towards(ship_location, command, value)

        return str(sum(map(lambda x: abs(x), ship_location.values())))

    def compute_part_two_solution(self, version_identifier: str) -> str:
        def __move_waypoint(
            waypoint: dict[str, int], direction: str, distance: int
        ) -> dict[str, int]:
            match direction:
                case "N":
                    waypoint["y"] += distance
                case "S":
                    waypoint["y"] -= distance
                case "E":
                    waypoint["x"] += distance
                case "W":
                    waypoint["x"] -= distance

            return waypoint

        def __rotate_ship_waypoint(
            waypoint: dict[str, int], rotation: str, degrees: int
        ) -> dict[str, int]:
            degrees = 360 - degrees if rotation == "L" else degrees

            for _ in range(degrees // 90):
                waypoint = {"x": waypoint["y"], "y": -waypoint["x"]}

            return waypoint

        def __move_ship_towards_waypoint(
            location: dict[str, int], waypoint: dict[str, int], distance: int
        ) -> dict[str, int]:
            return {
                "x": location["x"] + waypoint["x"] * distance,
                "y": location["y"] + waypoint["y"] * distance,
            }

        ship_location = {"x": 0, "y": 0}
        ship_waypoint = {"x": 10, "y": 1}

        for command, value in self.load_ship_instructions(version_identifier):
            match command:
                case "L" | "R":
                    ship_waypoint = __rotate_ship_waypoint(
                        ship_waypoint, command, value
                    )
                case "F":
                    ship_location = __move_ship_towards_waypoint(
                        ship_location, ship_waypoint, value
                    )
                case _:
                    ship_waypoint = __move_waypoint(ship_waypoint, command, value)

        return str(sum(map(lambda x: abs(x), ship_location.values())))

    def load_ship_instructions(self, version_identifier: str) -> list[tuple[str, int]]:
        return list(
            map(
                lambda line: (line[0], int(line[1:])),
                self.input_data_as_lines(self.part_one_identifier, version_identifier),
            )
        )
