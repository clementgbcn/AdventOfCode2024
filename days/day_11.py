from functools import lru_cache

from day_factory.day import Day
from day_factory.day_utils import TestEnum
from utils.input_parser import InputParser
from utils.utils import extract_int


class Day11(Day):
    FIRST_STAR_TEST_RESULT = 55312
    SECOND_STAR_TEST_RESULT = 65601038650482

    def __init__(self):
        super().__init__(self)

    @staticmethod
    @lru_cache(maxsize=None)
    def compute(value, stone) -> int:
        if stone == 0:
            return 1
        if value == 0:
            return Day11.compute(1, stone - 1)
        s = str(value)
        if len(s) % 2 == 0:
            ls = len(s) // 2
            return Day11.compute(int(s[0:ls]), stone - 1) + Day11.compute(
                int(s[ls:]), stone - 1
            )
        return Day11.compute(value * 2024, stone - 1)

    @staticmethod
    def compute_stones(input_value: InputParser, iteration) -> int:
        return sum(
            map(
                lambda s: Day11.compute(s, iteration),
                extract_int(next(input_value.get_iterator())),
            )
        )

    def solution_first_star(
        self, input_value: InputParser, input_type: TestEnum
    ) -> int:
        return self.compute_stones(input_value, iteration=25)

    def solution_second_star(
        self, input_value: InputParser, input_type: TestEnum
    ) -> int:
        return self.compute_stones(input_value, iteration=75)
