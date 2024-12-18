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
    def compute_robots(input_value: InputParser, input_type) -> int:
        coord = Day18.extract_input(input_value)
        size = 70 if input_type == TestEnum.PROBLEM else 6
        nb = 1024 if input_type == TestEnum.PROBLEM else 12
        grid = set(coord[:nb])
        start = 0
        visited = set()
        q = [(start, 0)]
        while len(q) > 0:
            p, nb = q.pop(0)
            if p == size + size * 1j:
                return nb
            if p in visited:
                continue
            visited.add(p)
            for d in [1, -1, 1j, -1j]:
                nxt = p + d
                if (
                    not (0 <= nxt.real <= size and 0 <= nxt.imag <= size)
                    or nxt in visited
                    or nxt in grid
                ):
                    continue
                q.append((nxt, nb + 1))

    @staticmethod
    def compute_robots_2(input_value: InputParser, input_type) -> int:
        coord = Day18.extract_input(input_value)
        size = 70 if input_type == TestEnum.PROBLEM else 6
        nb = 1024 if input_type == TestEnum.PROBLEM else 12
        grid = set(coord[:nb])
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
                    or nxt in grid
                ):
                    continue
                q.append((nxt, prev + [nxt]))
        flip = nb
        print(path)
        while path is not None:
            while coord[flip] not in set(path):
                flip += 1
            grid = set(coord[: flip + 1])
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
                        or nxt in grid
                    ):
                        continue
                    q.append((nxt, prev + [nxt]))
        print(coord[flip])
        return flip

    def solution_first_star(
        self, input_value: InputParser, input_type: TestEnum
    ) -> int:
        return self.compute_robots(input_value, input_type)

    def solution_second_star(
        self, input_value: InputParser, input_type: TestEnum
    ) -> int:
        return self.compute_robots_2(input_value, input_type)
