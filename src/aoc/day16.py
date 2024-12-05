import itertools

from src.aoc.day00 import Day00


class Day16(Day00):
    def compute_part_one_solution(self, version_identifier: str) -> str:
        rules, ticket, tickets_nearby = self.__parse_notes(version_identifier)

        def __is_ticket_valid(_ticket: list[int]) -> int:
            _rules = list(itertools.chain(*rules.values()))
            for field_value in _ticket:
                checks = list(map(lambda r: r[0] <= field_value <= r[1], _rules))
                if not any(checks):
                    return field_value

            return 0

        return str(sum(list(map(__is_ticket_valid, tickets_nearby))))

    def compute_part_two_solution(self, version_identifier: str) -> str:
        rules, ticket, tickets_nearby = self.__parse_notes(version_identifier)

        def __is_ticket_valid(_ticket: list[int]) -> int:
            _rules = list(itertools.chain(*rules.values()))
            for field_value in _ticket:
                checks = list(map(lambda r: r[0] <= field_value <= r[1], _rules))
                if not any(checks):
                    return False

            return True

        def __guess_field_options(value: int) -> list[int]:
            options = []
            for field, ranges in rules.items():
                if any(list(map(lambda r: r[0] <= value <= r[1], ranges))):
                    options.append(field)

            return options

        valid_tickets = list(filter(__is_ticket_valid, tickets_nearby))
        guessed_fields = {}
        correct_fields = {}

        for position, values in enumerate(self.transpose_grid(valid_tickets)):
            guessed_fields[position] = __guess_field_options(values[0])

        def __remove_field_proposals(fields_proposals: dict[int, list[str]],  proposal: str) -> dict[int, list[str]]:
            for fp in fields_proposals.values():
                if proposal in fp:
                    fp.remove(proposal)

            return fields_proposals

        for position, fields in guessed_fields.items():
            if len(fields) == 1:
                print(position, fields)

        # while guessed_fields:
        #     for position, fields in list(guessed_fields.items()):
        #         if len(fields) == 1:
        #             field = fields[0]
        #             guessed_fields.pop(position)
        #             correct_fields[field] = position
        #
        #             for tmp in guessed_fields.values():
        #                 if field in tmp:
        #                     tmp.remove(field)
        #             # guessed_fields = __remove_field_proposals(guessed_fields, field)


        print(correct_fields)

        return str(0)

    def __parse_notes(self, version_identifier: str):
        notes = self.input_data_as_lines(self.part_one_identifier, version_identifier)
        rules = {}
        ticket = []
        tickets_nearby = []

        for idx, line in enumerate(notes):
            if line == "your ticket:":
                ticket = list(map(int, notes[idx + 1].split(",")))
                continue

            if line == "nearby tickets:":
                tickets_nearby = list(
                    map(lambda x: list(map(int, x.split(","))), notes[idx + 1 :])
                )
                continue

            if ":" in line:
                field, ranges = line.split(": ")
                rules[field] = list(
                    map(
                        lambda x: list(map(int, tuple(x.split("-")))),
                        ranges.split(" or "),
                    )
                )

        return rules, ticket, tickets_nearby
