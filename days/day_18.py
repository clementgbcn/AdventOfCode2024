import logging

from day_factory.day import Day
from day_factory.day_utils import TestEnum
from utils.input_parser import InputParser
from utils.utils import extract_int

logger = logging.getLogger(__name__)

DISPLAY_BOT = False


class Day18(Day):
    FIRST_STAR_TEST_RESULT = 22
    SECOND_STAR_TEST_RESULT = 20

    def __init__(self):
        super().__init__(self)

    @staticmethod
    def extract_input(input_value: InputParser):
        coord = []
        for line in input_value.get_iterator():
            c = extract_int(line)
            coord.append(c[0] + c[1] * 1j)
        return coord

    @staticmethod
    def dfs(corrupted, size):
        start = 0
        visited = set()
        q = [(start, [start])]
        path = None
        while len(q) > 0:
            p, prev = q.pop(0)
            if p == size + size * 1j:
                path = prev
                break
            if p in visited:
                continue
            visited.add(p)
            for d in [1, -1, 1j, -1j]:
                nxt = p + d
                if (
                    not (0 <= nxt.real <= size and 0 <= nxt.imag <= size)
                    or nxt in visited
                    or nxt in corrupted
                ):
                    continue
                q.append((nxt, prev + [nxt]))
        return path

    @staticmethod
    def compute_robots(input_value: InputParser, input_type) -> int:
        coord = Day18.extract_input(input_value)
        size = 70 if input_type == TestEnum.PROBLEM else 6
        nb = 1024 if input_type == TestEnum.PROBLEM else 12
        return len(Day18.dfs(set(coord[:nb]), size)) - 1

    @staticmethod
    def compute_robots_2(input_value: InputParser, input_type) -> int:
        coord = Day18.extract_input(input_value)
        size = 70 if input_type == TestEnum.PROBLEM else 6
        # We know it works for part 1
        cutoff = 1024 if input_type == TestEnum.PROBLEM else 12
        path = Day18.dfs(set(coord[:cutoff]), size)
        while path is not None:
            while coord[cutoff] not in set(path):
                cutoff += 1
            path = Day18.dfs(set(coord[: cutoff + 1]), size)
        print(coord[cutoff])
        return cutoff

    def solution_first_star(
        self, input_value: InputParser, input_type: TestEnum
    ) -> int:
        return self.compute_robots(input_value, input_type)

    def solution_second_star(
        self, input_value: InputParser, input_type: TestEnum
    ) -> int:
        return self.compute_robots_2(input_value, input_type)
