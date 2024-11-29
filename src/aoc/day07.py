import re

from src.aoc.day00 import Day00


class Day07(Day00):
    def compute_part_one_solution(self, version_identifier: str) -> str:
        rules = self.parse_rules(self.part_one_identifier, version_identifier)
        return str(sum(self.can_bag_contain_shiny_gold(bag, rules) for bag in rules))

    def can_bag_contain_shiny_gold(self, bag: str, rules: dict) -> bool:
        if 'shiny gold' in rules[bag].keys():
            return True

        return any(self.can_bag_contain_shiny_gold(bag, rules) for bag in rules[bag])

    def compute_part_two_solution(self, version_identifier: str) -> str:
        rules = self.parse_rules(self.part_two_identifier, version_identifier)
        return str(self.count_bags_inside_shiny_gold(rules))

    def count_bags_inside_shiny_gold(self, rules: dict) -> int:
        return self.count_bags_inside('shiny gold', rules)

    def count_bags_inside(self, bag: str, rules: dict) -> int:
        return sum(count * (1 + self.count_bags_inside(bag, rules)) for bag, count in rules[bag].items())

    def parse_rules(self, part_identifier: str, version_identifier: str) -> dict:
        rules = {}

        for line in self.lines_input_data(part_identifier, version_identifier):
            bag, contents = line.split(' bags contain ')
            rules[bag] = {}

            if contents == 'no other bags.':
                continue

            for content in contents.split(', '):
                matches = re.search(r'(\d+) (.*) bags?', content)
                rules[bag][matches.group(2)] = int(matches.group(1))

        return rules
