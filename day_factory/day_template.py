from typing import List

from day import Day
from day_factory.day_utils import TestEnum


class DayTemplate(Day):
    def __init__(self):
        super().__init__(self)

    @staticmethod
    def solve(input_value: List[str]) -> int:
        return len(input_value)

    @staticmethod
    def solve_2(input_value: List[str]) -> int:
        return len(input_value)

    def solution_first_star(self, input_value: List[str], input_type: TestEnum) -> int:
        return self.solve(input_value)

    def solution_second_star(self, input_value: List[str], input_type: TestEnum) -> int:
        return self.solve_2(input_value)
