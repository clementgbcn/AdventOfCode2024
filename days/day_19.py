import logging

from day_factory.day import Day
from day_factory.day_utils import TestEnum
from utils.input_parser import InputParser

logger = logging.getLogger(__name__)

DISPLAY_BOT = False


class Day19(Day):
    FIRST_STAR_TEST_RESULT = 6
    SECOND_STAR_TEST_RESULT = 16

    def __init__(self):
        super().__init__(self)
        self.towels = set()

    @staticmethod
    def extract_input(input_value: InputParser):
        table = input_value.get_table()
        return set(table[0].split(", ")), table[2:]

    def is_valid(self, design, d):
        if design in d:
            return d[design]
        is_valid = False
        for towel in self.towels:
            if len(towel) > len(design) or design[: len(towel)] != towel:
                continue
            is_valid = is_valid or self.is_valid(design[len(towel) :], d)
            if is_valid:
                break
        d[design] = is_valid
        return is_valid

    def get_combinations(self, design, d):
        if design in d:
            return d[design]
        combinations = 0
        for towel in self.towels:
            if len(towel) > len(design) or design[: len(towel)] != towel:
                continue
            combinations += self.get_combinations(design[len(towel) :], d)
        d[design] = combinations
        return combinations

    def get_valid_towels(self, input_value: InputParser) -> int:
        self.towels, designs = Day19.extract_input(input_value)
        return sum(map(lambda design: self.is_valid(design, {"": True}), designs))

    def get_towels_arrangement(self, input_value: InputParser) -> int:
        table = input_value.get_table()
        self.towels = set(table[0].split(", "))
        return sum(
            map(lambda design: self.get_combinations(design, {"": 1}), table[2:])
        )

    def solution_first_star(
        self, input_value: InputParser, input_type: TestEnum
    ) -> int:
        return self.get_valid_towels(input_value)

    def solution_second_star(
        self, input_value: InputParser, input_type: TestEnum
    ) -> int:
        return self.get_towels_arrangement(input_value)
