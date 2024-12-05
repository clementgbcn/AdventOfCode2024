from typing import List

from day_factory.day import Day
from day_factory.day_utils import TestEnum


class Day04(Day):
    FIRST_STAR_TEST_RESULT = 18
    SECOND_STAR_TEST_RESULT = 9

    WORD = "XMAS"
    WORD_EDGE_LETTERS = {"M", "S"}

    def __init__(self):
        super().__init__(self)

    @staticmethod
    def search_word(table: List[str], i: int, j: int) -> int:
        if table[i][j] != Day04.WORD[0]:
            return 0
        total = 0
        for x in range(-1, 2):
            for y in range(-1, 2):
                if (x == 0 and y == 0) or not (
                    0 <= i + (len(Day04.WORD) - 1) * x < len(table)
                    and 0 <= j + (len(Day04.WORD) - 1) * y < len(table[0])
                ):
                    continue
                for z in range(1, len(Day04.WORD)):
                    if (
                        0 <= i + (x * z) < len(table)
                        and 0 <= j + (y * z) < len(table[0])
                        and table[i + (x * z)][j + (y * z)] == Day04.WORD[z]
                    ):
                        continue
                    break
                else:
                    total += 1
        return total

    @staticmethod
    def compute_program(input_value: List[str]) -> int:
        table = [line for line in input_value]
        total = 0
        for i in range(len(table)):
            for j in range(len(table[0])):
                total += Day04.search_word(table, i, j)
        return total

    @staticmethod
    def compute_program_2(input_value: List[str]) -> int:
        table = [line for line in input_value]
        total = 0
        for i in range(1, len(table) - 1):
            for j in range(1, len(table[0]) - 1):
                if table[i][j] != "A":
                    continue
                if {
                    table[i - 1][j - 1],
                    table[i + 1][j + 1],
                } == Day04.WORD_EDGE_LETTERS and {
                    table[i + 1][j - 1],
                    table[i - 1][j + 1],
                } == Day04.WORD_EDGE_LETTERS:
                    total += 1
        return total

    def solution_first_star(self, input_value: List[str], input_type: TestEnum) -> int:
        return self.compute_program(input_value)

    def solution_second_star(self, input_value: List[str], input_type: TestEnum) -> int:
        return self.compute_program_2(input_value)
