import re
from functools import reduce
from typing import List

from day_factory.day import Day
from day_factory.day_utils import TestEnum
from utils.utils import extract_int


class Day03(Day):
    FIRST_STAR_TEST_RESULT = 161
    SECOND_STAR_TEST_RESULT = 48

    MUL_INSTRUCTION = re.compile(r"mul\(-?\d+,-?\d+\)")
    DO_INSTRUCTION = "do()"
    DONT_INSTRUCTION = "don't()"

    def __init__(self):
        super().__init__(self)

    @staticmethod
    def compute_program(input_value: List[str]) -> int:
        total = 0
        for program_line in input_value:
            for op in re.compile(Day03.MUL_INSTRUCTION).findall(program_line):
                total += reduce(lambda x, y: x * y, extract_int(op))
        return total

    @staticmethod
    def compute_program_2(input_value: List[str]) -> int:
        total = 0
        for split_op in "".join(input_value).split(Day03.DO_INSTRUCTION):
            for op in re.compile(Day03.MUL_INSTRUCTION).findall(
                split_op.split(Day03.DONT_INSTRUCTION)[0]
            ):
                total += reduce(lambda x, y: x * y, extract_int(op))
        return total

    def solution_first_star(self, input_value: List[str], input_type: TestEnum) -> int:
        return self.compute_program(input_value)

    def solution_second_star(self, input_value: List[str], input_type: TestEnum) -> int:
        return self.compute_program_2(input_value)
