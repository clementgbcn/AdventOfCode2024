from bisect import insort
from itertools import starmap

from day_factory.day import Day
from utils.utils import extract_int


class Day01(Day):
    FIRST_STAR_TEST_RESULT = 11
    SECOND_STAR_TEST_RESULT = 31

    def __init__(self):
        super().__init__(self)

    @staticmethod
    def count_id(input_value):
        left_list = []
        right_list = []
        for line in input_value:
            values = extract_int(line)
            insort(left_list, values[0])
            insort(right_list, values[-1])
        return sum(starmap(lambda a, b: abs(a-b), zip(left_list, right_list)))


    @staticmethod
    def count_id_2(input_value):
        left_dict = {}
        right_dict = {}
        for line in input_value:
            values = extract_int(line)
            left_dict[values[0]] = left_dict.get(values[0], 0) + 1
            right_dict[values[-1]] = right_dict.get(values[-1], 0) + 1
        return sum(map(lambda x: x*left_dict.get(x, 0)*right_dict.get(x, 0), left_dict.keys()))

    def solution_first_star(self, input_value, input_type):
        return self.count_id(input_value)

    def solution_second_star(self, input_value, input_type):
        return self.count_id_2(input_value)
