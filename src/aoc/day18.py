from src.aoc.day00 import Day00


class Day18(Day00):
    def compute_part_one_solution(self, version_identifier: str) -> str:
        expressions = self.input_data_as_lines(
            self.part_one_identifier, version_identifier
        )
        return str(
            sum(
                [
                    self.__evaluate_expression(
                        expression, {"(": 0, "+": 1, "*": 1, ")": 1}
                    )
                    for expression in expressions
                ]
            )
        )

    def compute_part_two_solution(self, version_identifier: str) -> str:
        expressions = self.input_data_as_lines(
            self.part_one_identifier, version_identifier
        )
        return str(
            sum(
                [
                    self.__evaluate_expression(
                        expression, {"(": 0, "+": 2, "*": 1, ")": 1}
                    )
                    for expression in expressions
                ]
            )
        )

    def __evaluate_expression(self, expression: str, wages: dict[str, int]) -> int:
        stack = []

        for x in self.__convert_to_rpn(expression, wages):
            if x.isdigit():
                stack.append(int(x))
            elif x == "+":
                stack.append(stack.pop() + stack.pop())
            elif x == "*":
                stack.append(stack.pop() * stack.pop())

        return stack.pop()

    @staticmethod
    def __convert_to_rpn(expression: str, wages: dict[str, int]) -> list[str]:
        items = []
        stack = []

        for c in expression.replace(" ", ""):
            if c.isdigit():
                items.append(c)
            elif c == "(":
                stack.append(c)
            elif c == ")":
                while stack[-1] != "(":
                    items.append(stack.pop())
                stack.pop()
            else:
                while len(stack) and wages.get(stack[-1], 9) >= wages.get(c):
                    items.append(stack.pop())
                stack.append(c)

        while stack:
            items.append(stack.pop())

        return items
