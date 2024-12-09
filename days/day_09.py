from day_factory.day import Day
from day_factory.day_utils import TestEnum
from utils.input_parser import InputParser


class Day09(Day):
    FIRST_STAR_TEST_RESULT = 1928
    SECOND_STAR_TEST_RESULT = 2858

    def __init__(self):
        super().__init__(self)

    @staticmethod
    def compute_calibration(input_value: InputParser) -> int:
        disk_map_input = map(lambda x: int(x), input_value.get_table()[0])
        disk_map = []
        current_id = 0
        free_space = False
        for i, c in enumerate(disk_map_input):
            if free_space:
                disk_map += [None] * c
            else:
                disk_map += [current_id] * c
                current_id += 1
            free_space = not free_space
        print(disk_map)
        i = 0
        j = len(disk_map) - 1
        while i < j:
            if disk_map[i] is None and disk_map[j] is None:
                j -= 1
            elif disk_map[i] is not None and disk_map[j] is None:
                i += 1
                j -= 1
            elif disk_map[i] is not None and disk_map[j] is not None:
                i += 1
            else:
                disk_map[i], disk_map[j] = disk_map[j], disk_map[i]
                i += 1
                j -= 1
        total = 0
        for i, c in enumerate(disk_map):
            if c is None:
                break
            total += i * c
        return total

    @staticmethod
    def compute_calibration_2(input_value: InputParser) -> int:
        disk_map_input = map(lambda x: int(x), input_value.get_table()[0])
        disk_map = []
        current_id = 0
        free_space = False
        id_map = {}
        idx = 0
        for i, c in enumerate(disk_map_input):
            if free_space:
                disk_map += [None] * c
            else:
                disk_map += [current_id] * c
                id_map[current_id] = (idx, c)
                current_id += 1
            idx += c
            free_space = not free_space
        j_id = current_id - 1
        while 0 < j_id:
            j = id_map[j_id][0]
            i = 0
            while i < j:
                if disk_map[i] is not None:
                    i += 1
                else:
                    if all(map(lambda x: x is None, disk_map[i : i + id_map[j_id][1]])):
                        disk_map[i : i + id_map[j_id][1]] = disk_map[
                            j : j + id_map[j_id][1]
                        ]
                        disk_map[j : j + id_map[j_id][1]] = [None] * id_map[j_id][1]
                        break
                    else:
                        i += 1
            j_id -= 1
        total = 0
        for i, c in enumerate(disk_map):
            if c is None:
                continue
            total += i * c
        return total

    def solution_first_star(
        self, input_value: InputParser, input_type: TestEnum
    ) -> int:
        return self.compute_calibration(input_value)

    def solution_second_star(
        self, input_value: InputParser, input_type: TestEnum
    ) -> int:
        return self.compute_calibration_2(input_value)
