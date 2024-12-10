from day_factory.day import Day
from day_factory.day_utils import TestEnum
from utils.input_parser import InputParser


class Day10(Day):
    FIRST_STAR_TEST_RESULT = 36
    SECOND_STAR_TEST_RESULT = 81

    def __init__(self):
        super().__init__(self)

    @staticmethod
    def compute_calibration(input_value: InputParser, rating=False) -> int:
        trails = {}
        starts = set()
        i, j = 0, 0
        for i, line in enumerate(input_value.get_iterator()):
            for j, c in enumerate(line):
                if c == ".":
                    continue
                trails[i + j * 1j] = int(c)
                if c == "0":
                    starts.add(i + j * 1j)
        max_i, max_j = i, j
        score = 0
        trailheads = set()
        for start in starts:
            paths = [[start]]
            visited_paths = [set(starts)]
            if not rating:
                trailheads = set()
            while len(paths) > 0:
                current_path = paths.pop(0)
                current_path_set = visited_paths.pop(0)
                last_pos = current_path[-1]
                for direction in [1, -1, 1j, -1j]:
                    next_pos = last_pos + direction
                    if not (
                        0 <= next_pos.real <= max_i
                        and 0 <= next_pos.imag <= max_j
                        and next_pos not in current_path_set
                        and next_pos in trails
                        and trails[next_pos] == trails[last_pos] + 1
                    ):
                        continue
                    if trails[next_pos] == 9:
                        if not rating:
                            trailheads.add(next_pos)
                        else:
                            trailheads.add(tuple(current_path + [next_pos]))
                        continue
                    paths.append(current_path + [next_pos])
                    current_path_set = current_path_set.copy()
                    current_path_set.add(next_pos)
                    visited_paths.append(current_path_set)
            if not rating:
                score += len(trailheads)
        return score if not rating else len(trailheads)

    def solution_first_star(
        self, input_value: InputParser, input_type: TestEnum
    ) -> int:
        return self.compute_calibration(input_value, False)

    def solution_second_star(
        self, input_value: InputParser, input_type: TestEnum
    ) -> int:
        return self.compute_calibration(input_value, True)
