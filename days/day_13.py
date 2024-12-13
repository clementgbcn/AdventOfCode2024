from day_factory.day import Day
from day_factory.day_utils import TestEnum
from utils.input_parser import InputParser
from utils.utils import extract_int


class Day13(Day):
    FIRST_STAR_TEST_RESULT = 480
    SECOND_STAR_TEST_RESULT = 875318608908
    # 861046

    def __init__(self):
        super().__init__(self)

    @staticmethod
    def compute_stones(input_value: InputParser, offset=0) -> int:
        ite = input_value.get_iterator()
        tokens = 0
        while token_a_str := next(ite, None):
            token_a = extract_int(token_a_str)
            token_b = extract_int(next(ite))
            prize = list(map(lambda x: x + offset, extract_int(next(ite))))
            if (prize[1] * token_a[0] - prize[0] * token_a[1]) % (
                token_a[0] * token_b[1] - token_a[1] * token_b[0]
            ) == 0:
                b = (prize[1] * token_a[0] - prize[0] * token_a[1]) // (
                    token_a[0] * token_b[1] - token_a[1] * token_b[0]
                )
                if (prize[0] - b * token_b[0]) % token_a[0] == 0:
                    a = (prize[0] - b * token_b[0]) // token_a[0]
                    tokens += a * 3 + b
            next(ite, None)
        return tokens

    def solution_first_star(
        self, input_value: InputParser, input_type: TestEnum
    ) -> int:
        return self.compute_stones(
            input_value,
        )

    def solution_second_star(
        self, input_value: InputParser, input_type: TestEnum
    ) -> int:
        return self.compute_stones(input_value, 10000000000000)
