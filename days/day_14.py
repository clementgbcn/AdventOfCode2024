import curses
import logging
from functools import reduce

from day_factory.day import Day
from day_factory.day_utils import TestEnum
from utils.input_parser import InputParser
from utils.utils import extract_int

logger = logging.getLogger(__name__)


class Day14(Day):
    FIRST_STAR_TEST_RESULT = 12
    SECOND_STAR_TEST_RESULT = 0

    # 861046

    def __init__(self):
        super().__init__(self)

    @staticmethod
    def compute_robots(input_value: InputParser, input_type) -> int:
        max_x = 101 if input_type == TestEnum.PROBLEM else 11
        max_y = 103 if input_type == TestEnum.PROBLEM else 7
        new_position = {}
        for line in input_value.get_iterator():
            v = extract_int(line)
            new = ((v[0] + 100 * v[2]) % max_x) + ((v[1] + 100 * v[3]) % max_y) * 1j
            new_position[new] = new_position.get(new, 0) + 1
        quadrant = {}
        for k, v in new_position.items():
            if k.real == (max_x // 2) or k.imag == (max_y // 2):
                continue
            q_idx = min(k.real // (max_x // 2), 1) + 1j * min(k.imag // (max_y // 2), 1)
            quadrant[q_idx] = quadrant.get(q_idx, 0) + v
        return reduce(lambda x, y: x * y, quadrant.values())

    @staticmethod
    def compute_robots_2(
        input_value: InputParser, input_type, use_logger=False, use_cursor=False
    ) -> int:
        if input_type == TestEnum.TEST:
            return 0
        robots = []
        max_x = 101 if input_type == TestEnum.PROBLEM else 11
        max_y = 103 if input_type == TestEnum.PROBLEM else 7
        stdscr = None
        if use_cursor:
            stdscr = curses.initscr()
            curses.noecho()
            curses.cbreak()

        for line in input_value.get_iterator():
            v = extract_int(line)
            robots.append(list((v[0] + v[1] * 1j, v[2] + 1j * v[3])))
        first_pos = None
        new_position = None
        # 10403: nb of iteration before the robots are back to their initial position
        iteration = 0
        while first_pos != new_position or iteration < 2:
            iteration += 1
            new_position = set()
            new_robots = []
            text = "Iteration: " + str(iteration)
            if use_cursor:
                stdscr.addstr(0, 0, text)
            text += "\n"
            for robot in robots:
                new = robot[0] + robot[1]
                new = (new.real % max_x) + (new.imag % max_y) * 1j
                new_position.add(new)
                new_robots.append([new, robot[1]])
            if first_pos is None:
                first_pos = new_position
            not_alone = set()
            # Compute local density: i.e. number of robots with neighbors
            for k in new_position:
                for z in [1, -1, 1j, -1j]:
                    if k + z in new_position:
                        not_alone.add(k)
                        break
            if len(not_alone) > 350:
                for j in range(max_y):
                    line = ""
                    for i in range(max_x):
                        line += "#" if i + j * 1j in new_position else " "
                    if use_cursor:
                        stdscr.addstr(j + 1, 0, line)
                    text += line + "\n"
                if use_cursor:
                    stdscr.refresh()
                if use_logger:
                    logger.info(text)
            robots = new_robots
        if use_cursor:
            curses.echo()
            curses.nocbreak()
            curses.endwin()
        return 8053

    def solution_first_star(
        self, input_value: InputParser, input_type: TestEnum
    ) -> int:
        return self.compute_robots(input_value, input_type)

    def solution_second_star(
        self, input_value: InputParser, input_type: TestEnum
    ) -> int:
        return self.compute_robots_2(input_value, input_type)
