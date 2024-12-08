from day import Day
from day_factory.day_utils import TestEnum
from utils.input_parser import InputParser


class DayTemplate(Day):
    def __init__(self):
        super().__init__(self)

    @staticmethod
    def solve(input_value: InputParser) -> int:
        return len(input_value.get_table())

    @staticmethod
    def solve_2(input_value: InputParser) -> int:
        return len(input_value.get_table())

    def solution_first_star(
        self, input_value: InputParser, input_type: TestEnum
    ) -> int:
        return self.solve(input_value)

    def solution_second_star(
        self, input_value: InputParser, input_type: TestEnum
    ) -> int:
        return self.solve_2(input_value)
