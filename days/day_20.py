import logging

from day_factory.day import Day
from day_factory.day_utils import TestEnum
from utils.input_parser import InputParser

logger = logging.getLogger(__name__)

DISPLAY_BOT = False


class Day20(Day):
    FIRST_STAR_TEST_RESULT = 44
    SECOND_STAR_TEST_RESULT = 285

    def __init__(self):
        super().__init__(self)
        self.towels = set()

    @staticmethod
    def extract_input(input_value: InputParser):
        walls = set()
        start, end = 0, 0
        i, j = 0, 0
        for j, line in enumerate(input_value.get_iterator()):
            for i, c in enumerate(line):
                if c == "#":
                    walls.add(i + j * 1j)
                if c == "S":
                    start = i + j * 1j
                if c == "E":
                    end = i + j * 1j

        return start, end, i, j, walls

    @staticmethod
    def get_distances(start, end, walls):
        distance = {}
        queue = [(end, 0)]
        while len(queue) > 0:
            c = queue.pop(0)
            if c[0] in distance or c[0] in walls:
                continue
            distance[c[0]] = c[1]
            if c[0] == start:
                continue
            for d in [1, -1, 1j, -1j]:
                nxt = c[0] + d
                if nxt in distance or nxt in walls:
                    continue
                queue.append((c[0] + d, c[1] + 1))
        return distance

    @staticmethod
    def get_shortcut(
        input_value: InputParser, input_type, cheat_time, test_upper_bound
    ) -> int:
        start, end, max_i, max_j, walls = Day20.extract_input(input_value)
        distance = Day20.get_distances(start, end, walls)
        queue = [(start, 0, None)]
        res = {}
        time_saved = test_upper_bound if input_type == TestEnum.TEST else 100
        upper_bound = distance[start] - time_saved + 1
        while len(queue) > 0:
            c = queue.pop(0)
            dist = c[0] - end
            if c[1] + abs(dist.real) + abs(dist.imag) >= upper_bound:
                # Remaining distance too big
                continue
            if c[0] == end:
                if c[1] < upper_bound:
                    res[distance[start] - c[1]] = res.get(distance[start] - c[1], 0) + 1
                continue
            for y in range(-cheat_time, cheat_time + 1):
                for x in range(-cheat_time + abs(y), cheat_time + 1 - abs(y)):
                    if x == 0 and y == 0:
                        continue
                    nxt = c[0] + x + y * 1j
                    if nxt in walls or not (
                        0 <= nxt.real <= max_i and 0 <= nxt.imag <= max_j
                    ):
                        continue
                    dist = c[1] + abs(y) + abs(x) + distance[nxt]
                    if dist < upper_bound:
                        res[distance[start] - dist] = (
                            res.get(distance[start] - dist, 0) + 1
                        )
            for d in [1, -1, 1j, -1j]:
                nxt = c[0] + d
                if nxt == c[2]:
                    continue
                if nxt in walls or not (
                    0 <= nxt.real <= max_i and 0 <= nxt.imag <= max_j
                ):
                    continue
                queue.append((nxt, c[1] + 1, c[0]))
        return sum(res.values())

    def solution_first_star(
        self, input_value: InputParser, input_type: TestEnum
    ) -> int:
        return self.get_shortcut(input_value, input_type, 2, 1)

    def solution_second_star(
        self, input_value: InputParser, input_type: TestEnum
    ) -> int:
        return self.get_shortcut(input_value, input_type, 20, 50)
