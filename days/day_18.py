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
    def bfs(corrupted, size):
        start = 0
        q = [(start, None)]
        prev_mapping = {}
        while len(q) > 0:
            p, prev = q.pop(0)
            if p in prev_mapping:
                continue
            prev_mapping[p] = prev
            if p == size + size * 1j:
                break
            for d in [1, -1, 1j, -1j]:
                nxt = p + d
                if (
                    (0 <= nxt.real <= size and 0 <= nxt.imag <= size)
                    and nxt not in prev_mapping
                    and nxt not in corrupted
                ):
                    q.append((nxt, p))
        if prev_mapping.get(size + size * 1j, None) is None:
            return None
        current = size + size * 1j
        path = [current]
        while prev_mapping[current] != 0:
            current = prev_mapping[current]
            path += [current]
        return path

    @staticmethod
    def compute_robots(input_value: InputParser, input_type) -> int:
        coord = Day18.extract_input(input_value)
        size = 70 if input_type == TestEnum.PROBLEM else 6
        nb = 1024 if input_type == TestEnum.PROBLEM else 12
        return len(Day18.bfs(set(coord[:nb]), size))

    @staticmethod
    def compute_robots_inc(input_value: InputParser, input_type) -> int:
        coord = Day18.extract_input(input_value)
        size = 70 if input_type == TestEnum.PROBLEM else 6
        # We know it works for part 1
        cutoff = 1024 if input_type == TestEnum.PROBLEM else 12
        path = Day18.bfs(set(coord[:cutoff]), size)
        while path is not None:
            while coord[cutoff] not in set(path):
                cutoff += 1
            path = Day18.bfs(set(coord[: cutoff + 1]), size)
        print(coord[cutoff])
        return cutoff

    @staticmethod
    def compute_robots_dichotomy(input_value: InputParser, input_type) -> int:
        coord = Day18.extract_input(input_value)
        size = 70 if input_type == TestEnum.PROBLEM else 6
        low = 0
        high = len(coord)
        while low + 1 < high:
            mid = (low + high) // 2
            path = Day18.bfs(set(coord[:mid]), size)
            if path is None:
                high = mid
            else:
                low = mid
        if Day18.bfs(set(coord[: high + 1]), size) is not None:
            return high + 1
        if Day18.bfs(set(coord[:high]), size) is not None:
            return high
        return high - 1

    def solution_first_star(
        self, input_value: InputParser, input_type: TestEnum
    ) -> int:
        return self.compute_robots(input_value, input_type)

    def solution_second_star(
        self, input_value: InputParser, input_type: TestEnum
    ) -> int:
        return self.compute_robots_dichotomy(input_value, input_type)
