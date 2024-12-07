from typing import List

from day_factory.day import Day
from day_factory.day_utils import TestEnum
from utils.utils import extract_int


class Day07(Day):
    FIRST_STAR_TEST_RESULT = 3749
    SECOND_STAR_TEST_RESULT = 11387

    def __init__(self):
        super().__init__(self)

    @staticmethod
    def compute_recursive(target: int, v, support_pipe=False) -> bool:
        if len(v) == 1:
            return v[0] == target
        if (
            target > v[-1]
            and Day07.compute_recursive(target - v[-1], v[:-1], support_pipe)
        ) or (
            target % v[-1] == 0
            and Day07.compute_recursive(target // v[-1], v[:-1], support_pipe)
        ):
            return True
        if support_pipe:
            t_str = str(target)
            len_v = len(str(v[-1]))
            if (
                len(t_str) > len_v
                and int(t_str[-len_v:]) == v[-1]
                and Day07.compute_recursive(int(t_str[0:-len_v]), v[:-1], support_pipe)
            ):
                return True
        return False

    @staticmethod
    def compute_calibration(input_value: List[str], support_pipe=False) -> int:
        total = 0
        for line in input_value:
            v = extract_int(line)
            if Day07.compute_recursive(v[0], v[1:], support_pipe):
                total += v[0]
        return total

    def solution_first_star(self, input_value: List[str], input_type: TestEnum) -> int:
        return self.compute_calibration(input_value, False)

    def solution_second_star(self, input_value: List[str], input_type: TestEnum) -> int:
        return self.compute_calibration(input_value, True)
