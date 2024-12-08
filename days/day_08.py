from typing import List, Dict, Tuple

from day_factory.day import Day
from day_factory.day_utils import TestEnum
from utils.input_parser import InputParser


class Day08(Day):
    FIRST_STAR_TEST_RESULT = 14
    SECOND_STAR_TEST_RESULT = 34

    def __init__(self):
        super().__init__(self)

    @staticmethod
    def parse_antennas(
        input_value: InputParser,
    ) -> Tuple[int, int, Dict[str, List[complex]]]:
        antennas = {}
        x, y = 0, 0
        for x, line in enumerate(input_value.get_iterator()):
            for y, c in enumerate(line):
                if c != ".":
                    antennas[c] = antennas.get(c, []) + [x + y * 1j]
        return x, y, antennas

    @staticmethod
    def compute_calibration(input_value: InputParser) -> int:
        max_x, max_y, antennas = Day08.parse_antennas(input_value)
        antinodes = set()
        for antenna, pos in antennas.items():
            for a in range(len(pos) - 1):
                for b in range(a + 1, len(pos)):
                    x1 = 2 * pos[a] - pos[b]
                    if 0 <= x1.real <= max_x and 0 <= x1.imag <= max_y:
                        antinodes.add(x1)
                    x2 = 2 * pos[b] - pos[a]
                    if 0 <= x2.real <= max_x and 0 <= x2.imag <= max_y:
                        antinodes.add(x2)
        return len(antinodes)

    @staticmethod
    def add_antinodes(
        start: complex, v: complex, max_x: int, max_y: int, antinodes: set
    ) -> None:
        x = start
        while 0 <= x.real <= max_x and 0 <= x.imag <= max_y:
            antinodes.add(x)
            x += v

    @staticmethod
    def compute_calibration_2(input_value: InputParser) -> int:
        max_x, max_y, antennas = Day08.parse_antennas(input_value)
        antinodes = set()
        for antenna, pos in antennas.items():
            for a in range(len(pos) - 1):
                for b in range(a + 1, len(pos)):
                    v = pos[a] - pos[b]
                    Day08.add_antinodes(pos[a], v, max_x, max_y, antinodes)
                    Day08.add_antinodes(pos[b], -v, max_x, max_y, antinodes)
        return len(antinodes)

    def solution_first_star(
        self, input_value: InputParser, input_type: TestEnum
    ) -> int:
        return self.compute_calibration(input_value)

    def solution_second_star(
        self, input_value: InputParser, input_type: TestEnum
    ) -> int:
        return self.compute_calibration_2(input_value)
