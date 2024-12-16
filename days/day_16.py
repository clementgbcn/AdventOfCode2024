import logging
import sys

from day_factory.day import Day
from day_factory.day_utils import TestEnum
from utils.input_parser import InputParser

logger = logging.getLogger(__name__)

DISPLAY_BOT = False


class Day16(Day):
    FIRST_STAR_TEST_RESULT = 11048
    SECOND_STAR_TEST_RESULT = 64

    def __init__(self):
        super().__init__(self)

    @staticmethod
    def build_graph(input_value: InputParser):
        maze = {}
        i, j = 0, 0
        for j, line in enumerate(input_value.get_iterator()):
            for i, c in enumerate(line):
                maze[i + j * 1j] = c
        start = 1 + (j - 1) * 1j
        end = i - 1 + 1j
        visited = set()
        stack = [start]
        graph = {}
        while len(stack) > 0:
            p = stack.pop(0)
            if p in visited or maze[p] == "#":
                continue
            visited.add(p)
            if p != start and p != end:
                if maze[p + 1] == "#" and maze[p - 1] == "#":
                    # Not the nodes
                    stack.append(p + 1j)
                    stack.append(p - 1j)
                    continue
                if maze[p + 1j] == "#" and maze[p - 1j] == "#":
                    stack.append(p + 1)
                    stack.append(p - 1)
                    continue
            for e in [1, -1, 1j, -1j]:
                if maze[p - e] == "#" and not (p == start and e == 1):
                    continue
                for d in [1, -1, 1j, -1j]:
                    if e == -d or maze[p + d] == "#":
                        continue
                    graph[(p, e)] = graph.get((p, e), {})
                    graph[(p, e)][d] = None
                    stack.append(p + d)
        for n, k in graph.items():
            key_to_delete = []
            for d in k.keys():
                c = 1
                while maze[n[0] + c * d] != "#" and (n[0] + c * d, d) not in graph:
                    c += 1
                if maze[n[0] + c * d] == "#":
                    # Deadend
                    key_to_delete.append(d)
                else:
                    graph[n][d] = (
                        (n[0] + c * d, c) if n[1] == d else (n[0] + c * d, c + 1000)
                    )
            for key in key_to_delete:
                del graph[n][key]
        return graph, start, end

    @staticmethod
    def dijkstra_algorithm(graph, start_node):
        unvisited_nodes = list(graph.keys())
        shortest_path = {}
        previous_nodes = {}
        max_value = sys.maxsize
        for node in unvisited_nodes:
            shortest_path[node] = max_value
        shortest_path[start_node] = 0

        while unvisited_nodes:
            current_min_node = None
            for node in unvisited_nodes:  # Iterate over the nodes
                if current_min_node is None:
                    current_min_node = node
                elif shortest_path[node] < shortest_path[current_min_node]:
                    current_min_node = node

            neighbors = graph[current_min_node]
            for d, neighbor in neighbors.items():
                tentative_value = shortest_path[current_min_node] + neighbor[1]
                if tentative_value <= shortest_path[(neighbor[0], d)]:
                    shortest_path[(neighbor[0], d)] = tentative_value
                    previous_nodes[(neighbor[0], d)] = previous_nodes.get(
                        (neighbor[0], d), []
                    ) + [current_min_node]

            unvisited_nodes.remove(current_min_node)

        return previous_nodes, shortest_path

    @staticmethod
    def compute_robots(input_value: InputParser) -> int:
        graph, start, end = Day16.build_graph(input_value)
        _, dist = Day16.dijkstra_algorithm(graph, (start, 1))
        return min(dist[(end, 1)], dist[(end, -1j)])

    @staticmethod
    def compute_robots_2(input_value: InputParser) -> int:
        graph, start, end = Day16.build_graph(input_value)
        path, dist = Day16.dijkstra_algorithm(graph, (start, 1))
        node_to_visit = []
        best_places = {start}
        visited = {(start, 1)}
        if dist[(end, 1)] <= dist[(end, -1j)]:
            node_to_visit.append((end, 1))
        if dist[(end, 1)] >= dist[(end, -1j)]:
            node_to_visit.append((end, -1j))
        while len(node_to_visit) > 0:
            n = node_to_visit.pop(0)
            if n in visited:
                continue
            best_places.add(n[0])
            visited.add(n)
            for previous in path[n]:
                dist = previous[0] - n[0]
                ite = int(abs(dist))
                d = dist / abs(dist)
                for c in range(1, ite):
                    best_places.add(n[0] + c * d)
                node_to_visit.append(previous)
        return len(best_places)

    def solution_first_star(
        self, input_value: InputParser, input_type: TestEnum
    ) -> int:
        return self.compute_robots(input_value)

    def solution_second_star(
        self, input_value: InputParser, input_type: TestEnum
    ) -> int:
        return self.compute_robots_2(input_value)
