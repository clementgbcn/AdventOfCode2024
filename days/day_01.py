from day_factory.day import Day


class Day01(Day):
    FIRST_STAR_TEST_RESULT = 0
    SECOND_STAR_TEST_RESULT = 0

    def __init__(self):
        super().__init__(self)

    @staticmethod
    def count_increment(input_value):
        print(input_value)
        return 0

    @staticmethod
    def count_increment_2(input_value):
        print(input_value)
        return 0

    def solution_first_star(self, input_value, input_type):
        return self.count_increment(input_value)

    def solution_second_star(self, input_value, input_type):
        return self.count_increment_2(input_value)
