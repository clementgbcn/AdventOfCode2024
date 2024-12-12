from day_factory.day import Day
from day_factory.day_utils import TestEnum
from utils.input_parser import InputParser


class Day12(Day):
    FIRST_STAR_TEST_RESULT = 1930
    SECOND_STAR_TEST_RESULT = 1206
    # 861046

    def __init__(self):
        super().__init__(self)

    @staticmethod
    def get_region(garden, i, j, visited):
        current_region = set()
        stack = [i + j * 1j]
        plant = garden[i][j]
        while len(stack) > 0:
            current = stack.pop(0)
            if current in current_region or current in visited:
                continue
            visited.add(current)
            current_region.add(current)
            for direction in [1, -1, 1j, -1j]:
                new_pos = current + direction
                if (
                    0 <= new_pos.real < len(garden)
                    and 0 <= new_pos.imag < len(garden[0])
                    and new_pos not in visited
                    and garden[int(new_pos.real)][int(new_pos.imag)] == plant
                ):
                    stack.append(new_pos)
        edges_map = {}
        for p in current_region:
            for t in [(0, 1j), (0, 1), (1, 1 + 1j), (1j, 1 + 1j)]:
                edges_map[(p + t[0], p + t[1])] = edges_map.get(
                    (p + t[0], p + t[1]), set()
                )
                edges_map[(p + t[0], p + t[1])].add(p)
        side_edges_map = {k: list(v)[0] for k, v in edges_map.items() if len(v) == 1}
        return current_region, side_edges_map

    @staticmethod
    def get_edges(side_edges_map, i, j):
        edge = 0
        visited_edges = set()
        while len(visited_edges) != len(side_edges_map):
            if len(visited_edges) > 0:
                edge_to_visit = (
                    set(side_edges_map.keys()).difference(visited_edges).pop()
                )
                start, nxt = edge_to_visit
            else:
                start, nxt = i + j * 1j, i + (j + 1) * 1j
            first_one = start
            start_direction = nxt - start
            d = start_direction
            visited_edges.add((start, nxt))
            while nxt != first_one:
                ps = []
                for direction in [1, -1, 1j, -1j]:
                    new_pos = nxt + direction
                    if (
                        (nxt, new_pos) not in side_edges_map
                        and (new_pos, nxt) not in side_edges_map
                    ) or new_pos == start:
                        continue
                    ps.append((nxt, new_pos, direction, 0 if direction == d else 1))
                for p in ps:
                    current_tile = side_edges_map.get(
                        (start, nxt), side_edges_map.get((nxt, start))
                    )
                    tile = side_edges_map.get(
                        (p[0], p[1]), side_edges_map.get((p[1], p[0]))
                    )
                    if len(ps) == 1 or current_tile == tile:
                        start, nxt = p[0], p[1]
                        if (start, nxt) in side_edges_map:
                            visited_edges.add((start, nxt))
                        else:
                            visited_edges.add((nxt, start))
                        edge += p[3]
                        d = p[2]
            if start_direction != d:
                edge += 1
        return edge

    @staticmethod
    def compute_stones(input_value: InputParser, perimeter) -> int:
        garden = input_value.get_table()
        regions = []
        visited = set()
        for i in range(len(garden)):
            for j in range(len(garden[0])):
                if i + j * 1j in visited:
                    continue
                current_region, edges_side_map = Day12.get_region(garden, i, j, visited)
                if perimeter:
                    regions.append((current_region, len(edges_side_map)))
                else:
                    regions.append(
                        (current_region, Day12.get_edges(edges_side_map, i, j))
                    )
        return sum(map(lambda x: len(x[0]) * x[1], regions))

    def solution_first_star(
        self, input_value: InputParser, input_type: TestEnum
    ) -> int:
        return self.compute_stones(input_value, True)

    def solution_second_star(
        self, input_value: InputParser, input_type: TestEnum
    ) -> int:
        return self.compute_stones(input_value, False)
