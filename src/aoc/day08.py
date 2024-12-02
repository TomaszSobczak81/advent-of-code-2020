import copy

from src.aoc.day00 import Day00


class Day08(Day00):
    def __init__(self, part_one_expected_result: str, part_two_expected_result: str):
        super(Day08, self).__init__(part_one_expected_result, part_two_expected_result)
        self.executed_lines_of_code: list[int] = []
        self.is_infinite_loop: bool = False

    def compute_part_one_solution(self, version_identifier: str) -> str:
        code = self.parse_code(self.part_one_identifier, version_identifier)

        self.executed_lines_of_code = []
        self.is_infinite_loop = False

        return str(self.execute_code(code))

    def parse_code(self, part_identifier: str, version_identifier: str) -> list:
        code = []

        for line in self.input_data_as_lines(part_identifier, version_identifier):
            operation, argument = line.split(" ")
            code.append({"operation": operation, "argument": int(argument)})

        return code

    def execute_code(self, code: list, line: int = 0, acc: int = 0) -> int:
        if line >= len(code):
            return acc

        if line in self.executed_lines_of_code:
            self.is_infinite_loop = True
            return acc

        self.executed_lines_of_code.append(line)
        match code[line]["operation"]:
            case "acc":
                return self.execute_code(code, line + 1, acc + code[line]["argument"])
            case "jmp":
                return self.execute_code(code, line + code[line]["argument"], acc)
            case "nop":
                return self.execute_code(code, line + 1, acc)

        return acc

    def compute_part_two_solution(self, version_identifier: str) -> str:
        code = self.parse_code(self.part_one_identifier, version_identifier)

        for idx, line in enumerate(code):
            if line["operation"] == "acc":
                continue

            __code = copy.deepcopy(code)
            __code[idx]["operation"] = "jmp" if line["operation"] == "nop" else "nop"

            self.executed_lines_of_code = []
            self.is_infinite_loop = False

            acc = self.execute_code(__code)

            if not self.is_infinite_loop:
                return str(acc)

        raise Exception("No solution found")
