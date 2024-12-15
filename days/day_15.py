import logging

from day_factory.day import Day
from day_factory.day_utils import TestEnum
from utils.input_parser import InputParser

logger = logging.getLogger(__name__)


class Day15(Day):
    FIRST_STAR_TEST_RESULT = 10092
    SECOND_STAR_TEST_RESULT = 9021

    DIRECTION = {"<": -1, ">": 1, "^": -1j, "v": 1j}

    def __init__(self):
        super().__init__(self)

    @staticmethod
    def compute_robots(input_value: InputParser) -> int:
        warehouse = {}
        moves = []
        iterator = input_value.get_iterator()
        robot = None
        i, j = None, None
        for j, line in enumerate(iterator):
            if line == "":
                break
            for i, c in enumerate(line):
                warehouse[i + j * 1j] = c
                if c == "@":
                    robot = i + j * 1j
        max_i = i + 1
        max_j = j
        for line in iterator:
            moves += list(line)
        for m in moves:
            d = Day15.DIRECTION[m]
            boxes = []
            can_move = True
            while True:
                p = robot + d * (len(boxes) + 1)
                if warehouse[robot + d * (len(boxes) + 1)] == "O":
                    boxes.append(p)
                    continue
                elif warehouse[robot + d * (len(boxes) + 1)] == "#":
                    can_move = False
                break
            if can_move:
                for b in boxes[::-1]:
                    warehouse[b + d] = "O"
                warehouse[robot] = "."
                robot = robot + d
                warehouse[robot] = "@"
        count = 0
        for j in range(max_j):
            for i in range(max_i):
                if warehouse[i + j * 1j] == "O":
                    count += j * 100 + i
        return count

    @staticmethod
    def compute_robots_2(input_value: InputParser) -> int:
        warehouse = {}
        moves = []
        iterator = input_value.get_iterator()
        robot = None
        i, j = None, None
        for j, line in enumerate(iterator):
            if line == "":
                break
            for i, c in enumerate(line):
                if c == "#" or c == ".":
                    warehouse[2 * i + j * 1j] = c
                    warehouse[2 * i + 1 + j * 1j] = c
                elif c == "O":
                    warehouse[2 * i + j * 1j] = "["
                    warehouse[2 * i + 1 + j * 1j] = "]"
                elif c == "@":
                    warehouse[2 * i + j * 1j] = "@"
                    warehouse[2 * i + 1 + j * 1j] = "."
                    robot = 2 * i + j * 1j
        max_i = 2 * (i + 1)
        max_j = j
        for line in iterator:
            moves += list(line)
        for m in moves:
            d = Day15.DIRECTION[m]
            boxes = set()
            visited = set()
            bfs = [robot]
            can_move = True
            while len(bfs):
                p = bfs.pop(0) + d
                if p in visited:
                    continue
                visited.add(p)
                if warehouse[p] == "[":
                    boxes.add(p)
                    bfs.append(p)
                    bfs.append(p + 1)
                    continue
                elif warehouse[p] == "]":
                    boxes.add(p - 1)
                    bfs.append(p - 1)
                    bfs.append(p)
                    continue
                elif warehouse[p] == "#":
                    can_move = False
                    break
            if can_move:
                updated = set()
                for b in boxes:
                    warehouse[b + d] = "["
                    warehouse[b + 1 + d] = "]"
                    updated.add(b + d)
                    updated.add(b + 1 + d)
                for b in boxes:
                    if b not in updated:
                        warehouse[b] = "."
                    if b + 1 not in updated:
                        warehouse[b + 1] = "."
                warehouse[robot] = "."
                robot = robot + d
                warehouse[robot] = "@"
        count = 0
        for j in range(max_j):
            for i in range(max_i):
                if warehouse[i + j * 1j] == "[":
                    count += j * 100 + i
        return count

    def solution_first_star(
        self, input_value: InputParser, input_type: TestEnum
    ) -> int:
        return self.compute_robots(input_value)

    def solution_second_star(
        self, input_value: InputParser, input_type: TestEnum
    ) -> int:
        return self.compute_robots_2(input_value)
