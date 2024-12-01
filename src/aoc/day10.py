from src.aoc.day00 import Day00


class Day10(Day00):
    def compute_part_one_solution(self, version_identifier: str) -> str:
        current_joltage = 0
        one_jolt_differences = 0
        three_jolt_differences = 1  # The device's built-in adapter is always 3 jolts higher than the highest adapter

        adapters = self.input_data_as_lines_of_ints(self.part_one_identifier, version_identifier)

        for adapter in sorted(adapters):
            match adapter - current_joltage:
                case 1:
                    one_jolt_differences += 1
                case 3:
                    three_jolt_differences += 1
                case _:
                    pass

            current_joltage = adapter

        return str(one_jolt_differences * three_jolt_differences)

    def compute_part_two_solution(self, version_identifier: str) -> str:
        adapters = self.input_data_as_lines_of_ints(self.part_one_identifier, version_identifier)
        current_joltage = 0
        collections = []
        current_set = [0]

        for adapter in sorted(adapters):
            match adapter - current_joltage:
                case 3:
                    collections.append(current_set)
                    current_set = [adapter]
                case _:
                    current_set.append(adapter)

            current_joltage = adapter
        collections.extend([current_set, [current_joltage + 3]])

        combinations = 1
        for collection in collections:
            combinations *= self.compute_collections_combinations(collection)

        return str(combinations)

    def compute_collections_combinations(self, collection: list[int]) -> int:
        collection_length = len(collection)
        if collection_length < 3:
            return 1

        match collection_length:
            case 3:
                return 2
            case 4:
                return 4
            case 5:
                return 7
            case _:
                return 1
