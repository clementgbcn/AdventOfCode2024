from typing import List, Dict, Set, Iterable

from day_factory.day import Day
from day_factory.day_utils import TestEnum
from utils.input_parser import InputParser
from utils.utils import extract_int


class Day05(Day):
    FIRST_STAR_TEST_RESULT = 143
    SECOND_STAR_TEST_RESULT = 123

    def __init__(self):
        super().__init__(self)

    @staticmethod
    def compute_program(input_value: InputParser) -> int:
        values = input_value.get_iterator()
        rules = Day05.extract_rules(values)
        total = 0
        for line in values:
            updates = extract_int(line)
            if not Day05.is_invalid(updates, rules):
                total += updates[len(updates) // 2]
        return total

    @staticmethod
    def compute_program_2(input_value: InputParser) -> int:
        values = input_value.get_iterator()
        rules = Day05.extract_rules(values)
        total = 0
        for line in values:
            updates = extract_int(line)
            if not Day05.is_invalid(updates, rules):
                continue
            for idx, update in enumerate(updates):
                constraint = rules.get(update, set())
                subset = set(updates[:idx] + updates[idx + 1 :])
                if len(constraint.intersection(subset)) == len(updates) // 2:
                    total += update
                    break
        return total

    @staticmethod
    def extract_rules(input_value: Iterable[str]) -> Dict[int, Set[int]]:
        rules = {}
        for line in input_value:
            if line == "":
                break
            values = extract_int(line)
            new_set = rules.get(values[0], set())
            new_set.add(values[1])
            rules[values[0]] = new_set
        return rules

    @staticmethod
    def is_invalid(updates: List[int], rules: Dict[int, Set[int]]):
        encountered_updates = set()
        for update in updates:
            encountered_updates.add(update)
            for constraint in rules.get(update, set()):
                if constraint in encountered_updates:
                    break
            else:
                continue
            return True
        return False

    def solution_first_star(
        self, input_value: InputParser, input_type: TestEnum
    ) -> int:
        return self.compute_program(input_value)

    def solution_second_star(
        self, input_value: InputParser, input_type: TestEnum
    ) -> int:
        return self.compute_program_2(input_value)
