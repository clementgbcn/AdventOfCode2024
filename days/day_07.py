from functools import reduce
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
    def compute_calibration(input_value: List[str]) -> int:
        total = 0
        for line in input_value:
            v = extract_int(line)
            if reduce(lambda x, y: x + y if min(x, y) == 1 else x * y, v[1:]) < v[0]:
                continue
            for comb in range(0, 2 ** (len(v) - 2)):
                calibration = v[1]
                for i in range(0, len(v) - 2):
                    calibration = (
                        calibration + v[i + 2]
                        if comb & (1 << i)
                        else calibration * v[i + 2]
                    )
                    if calibration > v[0]:
                        break
                if calibration == v[0]:
                    total += v[0]
                    break
        return total

    @staticmethod
    def compute_calibration_fast(input_value: List[str]) -> int:
        total = 0
        for line in input_value:
            v = extract_int(line)
            print(v)
            if Day07.compute_recursive(v[0], v[1:], False):
                total += v[0]
        return total

    @staticmethod
    def compute_recursive(target: int, v, support_pipe=False) -> bool:
        if len(v) == 1:
            return v[0] == target
        if target > v[-1] and Day07.compute_recursive(
            target - v[-1], v[:-1], support_pipe
        ):
            return True
        if target % v[-1] == 0 and Day07.compute_recursive(
            target // v[-1], v[:-1], support_pipe
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
    def compute_calibration_2(input_value: List[str]) -> int:
        total = 0
        for line in input_value:
            v = extract_int(line)
            calibration = v[1]
            for i in range(0, len(v) - 2):
                calibration = int(str(calibration) + str(v[i + 2]))
            if calibration < v[0]:
                continue
            for comb in range(0, 3 ** (len(v) - 2)):
                calibration = v[1]
                product = comb
                for i in range(0, len(v) - 2):
                    if product % 3 == 0:
                        calibration *= v[i + 2]
                    elif product % 3 == 1:
                        calibration += v[i + 2]
                    else:
                        calibration = int(str(calibration) + str(v[i + 2]))
                    if calibration > v[0]:
                        break
                    product = product // 3
                if calibration == v[0]:
                    total += v[0]
                    break
        return total

    @staticmethod
    def compute_calibration_2_fast(input_value: List[str]) -> int:
        total = 0
        for line in input_value:
            v = extract_int(line)
            if Day07.compute_recursive(v[0], v[1:], True):
                total += v[0]
        return total

    def solution_first_star(self, input_value: List[str], input_type: TestEnum) -> int:
        return self.compute_calibration(input_value)

    def solution_second_star(self, input_value: List[str], input_type: TestEnum) -> int:
        return self.compute_calibration_2(input_value)
