from bisect import insort, bisect

from day_factory.day import Day
from day_factory.day_utils import TestEnum
from utils.input_parser import InputParser


class Guard:
    def __init__(self, i, j, di, dj):
        self.i = i
        self.j = j
        self.di = di
        self.dj = dj

    @property
    def ij(self):
        return self.i, self.j

    @property
    def didj(self):
        return self.di, self.dj

    @property
    def ijd(self):
        return self.i, self.j, self.di, self.dj

    def get_next(self):
        return Guard(self.i + self.di, self.j + self.dj, self.di, self.dj)

    def rotate(self):
        return Guard(self.i, self.j, self.dj, -self.di)

    def is_next_valid(self, obstructions):
        return 0 <= self.i + self.di < len(
            obstructions
        ) and 0 <= self.j + self.dj < len(obstructions[0])


class Day06(Day):
    FIRST_STAR_TEST_RESULT = 41
    SECOND_STAR_TEST_RESULT = 6

    def __init__(self):
        super().__init__(self)

    @staticmethod
    def extract_data(input_value: InputParser):
        obstructions = []
        guard = None
        for i, line in enumerate(input_value.get_iterator()):
            current_line = []
            for j, c in enumerate(line[::]):
                if c == "^":
                    guard = Guard(i, j, -1, 0)
                    current_line.append(".")
                else:
                    current_line.append(c)
            obstructions.append(current_line)
        return obstructions, guard

    @staticmethod
    def compute_visited(obstructions, guard: Guard):
        visited = {guard.ij: set()}
        while guard.is_next_valid(obstructions) and guard.didj not in visited[guard.ij]:
            visited[guard.ij].add(guard.didj)
            next_guard = guard.get_next()
            if obstructions[next_guard.i][next_guard.j] == "#":
                guard = guard.rotate()
            else:
                guard = next_guard
                if guard.ij not in visited:
                    visited[guard.ij] = set()
        return guard.didj in visited.get(guard.ij, set()), visited

    @staticmethod
    def compute_program(input_value: InputParser) -> int:
        obstructions, guard = Day06.extract_data(input_value)
        _, visited = Day06.compute_visited(obstructions, guard)
        return len(visited)

    @staticmethod
    def compute_program_2(input_value: InputParser) -> int:
        obstructions, guard = Day06.extract_data(input_value)
        visited = Day06.compute_visited(obstructions, guard)[1]
        del visited[guard.ij]
        total = 0
        for v in visited.keys():
            obstructions[v[0]][v[1]] = "#"
            if Day06.compute_visited(obstructions, guard)[0]:
                total += 1
            obstructions[v[0]][v[1]] = "."
        print(total)
        return total

    @staticmethod
    def extract_advanced_data(input_line: InputParser):
        obstructions_rows = {}
        obstructions_columns = {}
        max_i = 0
        max_j = 0
        guard = None
        for i, line in enumerate(input_line.get_iterator()):
            max_i = i
            for j, c in enumerate(line[::]):
                if c == "#":
                    obstructions_rows[i] = obstructions_rows.get(i, list())
                    insort(obstructions_rows[i], j)
                    obstructions_columns[j] = obstructions_columns.get(j, list())
                    insort(obstructions_columns[j], i)
                elif c == "^":
                    guard = (i, j, -1, 0)
                max_j = j
        return obstructions_rows, obstructions_columns, max_i, max_j, guard

    @staticmethod
    def optimal_visit(obstructions_columns, obstructions_rows, guard, max_i, max_j):
        visited = {(guard[0], guard[1])}
        while True:
            i, j, di, dj = guard
            if dj == 0:
                col = obstructions_columns.get(j, list())
                idx = bisect(col, i)
                if (
                    len(col) == 0
                    or (di == 1 and idx == len(col))
                    or (di == -1 and idx == 0)
                ):
                    x, y = (i, max_i + 1) if di == 1 else (0, i)
                    for k in range(x, y):
                        visited.add((k, j))
                    return visited
                next_i = col[idx] - 1 if di == 1 else col[idx - 1] + 1
                x, y = (i + 1, next_i + 1) if di == 1 else (next_i, i)
                for k in range(x, y):
                    visited.add((k, j))
                guard = (next_i, j, 0, -di)
            else:
                row = obstructions_rows.get(i, list())
                idx = bisect(row, j)
                if (
                    len(row) == 0
                    or (dj == 1 and idx == len(row))
                    or (dj == -1 and idx == 0)
                ):
                    x, y = (j, max_j + 1) if dj == 1 else (0, j)
                    for k in range(x, y):
                        visited.add((i, k))
                    return visited
                next_j = row[idx] - 1 if dj == 1 else row[idx - 1] + 1
                x, y = (j + 1, next_j + 1) if dj == 1 else (next_j, j)
                for k in range(x, y):
                    visited.add((i, k))
                guard = (i, next_j, dj, 0)

    @staticmethod
    def compute_program_fast(input_value: InputParser) -> int:
        obstructions_rows, obstructions_columns, max_i, max_j, guard = (
            Day06.extract_advanced_data(input_value)
        )
        return len(
            Day06.optimal_visit(
                obstructions_columns, obstructions_rows, guard, max_i, max_j
            )
        )

    @staticmethod
    def is_looping(obstructions_rows, obstructions_columns, start):
        visited_oriented = set()
        guard = (start[0], start[1], -1, 0)
        while guard not in visited_oriented:
            visited_oriented.add(guard)
            i, j, di, dj = guard
            if dj == 0:
                col = obstructions_columns.get(j, list())
                idx = bisect(col, i)
                if (
                    len(col) == 0
                    or (di == 1 and idx == len(col))
                    or (di == -1 and idx == 0)
                ):
                    return False
                next_i = col[idx] - 1 if di == 1 else col[idx - 1] + 1
                guard = (next_i, j, 0, -di)
            else:
                row = obstructions_rows.get(i, list())
                idx = bisect(row, j)
                if (
                    len(row) == 0
                    or (dj == 1 and idx == len(row))
                    or (dj == -1 and idx == 0)
                ):
                    return False
                next_j = row[idx] - 1 if dj == 1 else row[idx - 1] + 1
                guard = (i, next_j, dj, 0)
        return True

    @staticmethod
    def compute_program_2_fast(input_value: InputParser) -> int:
        obstructions_rows, obstructions_columns, max_i, max_j, guard = (
            Day06.extract_advanced_data(input_value)
        )
        start = (guard[0], guard[1])
        visited = Day06.optimal_visit(
            obstructions_columns, obstructions_rows, guard, max_i, max_j
        )
        visited.remove(start)
        total = 0
        for v in visited:
            obstructions_rows[v[0]] = obstructions_rows.get(v[0], list())
            row_idx = bisect(obstructions_rows[v[0]], v[1])
            obstructions_rows[v[0]] = (
                obstructions_rows[v[0]][:row_idx]
                + [v[1]]
                + obstructions_rows[v[0]][row_idx:]
            )
            obstructions_columns[v[1]] = obstructions_columns.get(v[1], list())
            col_idx = bisect(obstructions_columns[v[1]], v[0])
            obstructions_columns[v[1]] = (
                obstructions_columns[v[1]][:col_idx]
                + [v[0]]
                + obstructions_columns[v[1]][col_idx:]
            )
            if Day06.is_looping(obstructions_rows, obstructions_columns, start):
                total += 1
            del obstructions_rows[v[0]][row_idx]
            del obstructions_columns[v[1]][col_idx]
            if len(obstructions_rows[v[0]]) == 0:
                del obstructions_rows[v[0]]
            if len(obstructions_columns[v[1]]) == 0:
                del obstructions_columns[v[1]]
        return total

    def solution_first_star(
        self, input_value: InputParser, input_type: TestEnum
    ) -> int:
        return self.compute_program_fast(input_value)

    def solution_second_star(
        self, input_value: InputParser, input_type: TestEnum
    ) -> int:
        return self.compute_program_2_fast(input_value)
