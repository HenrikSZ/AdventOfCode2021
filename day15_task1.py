###############################################################################
# Day x, Task y                                                               #
###############################################################################

import aoc_util, sys


day = 15
data_str = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""


class Dijkstra():
    def __init__(self, matrix):
        self.matrix = matrix
        self.vertices = []
        self.dists = {(0, 0): 0}
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                vertex = (row, col)
                self.vertices.append(vertex)
                self.dists[vertex] = sys.maxsize

        self.dists[(0, 0)] = 0

    def find_min_distance_vertex(self):
        min_dist_vertex = (0, 0)
        distance = sys.maxsize
        for k in self.vertices:
            if self.dists[k] < distance:
                distance = self.dists[k]
                min_dist_vertex = k

        return distance, min_dist_vertex


    def get_neighbours(self, vertex):
        neighbours = []
        if (vertex[0] - 1, vertex[1]) in self.vertices:
            neighbours.append((vertex[0] - 1, vertex[1]))
        if (vertex[0], vertex[1] - 1) in self.vertices:
            neighbours.append((vertex[0], vertex[1] - 1))
        if (vertex[0], vertex[1] + 1) in self.vertices:
            neighbours.append((vertex[0], vertex[1] + 1))
        if (vertex[0] + 1, vertex[1]) in self.vertices:
            neighbours.append((vertex[0] + 1, vertex[1]))

        return neighbours


    def solve(self):
        while len(self.vertices) > 0:
            distance, min_distance_vertex = self.find_min_distance_vertex()
            self.vertices.remove(min_distance_vertex)

            neighbours = self.get_neighbours(min_distance_vertex)
            for n in neighbours:
                alt = distance + self.matrix[n[0]][n[1]]

                if alt < self.dists[n]:
                    self.dists[n] = alt

        return self.dists[(len(self.matrix) - 1, len(self.matrix[0]) - 1)]


def task(data_set: list[str]) -> int:
    risk_map = []
    for i in data_set:
        row = [int(x) for x in i]
        risk_map.append(row)

    dijkstra = Dijkstra(risk_map)

    return dijkstra.solve()



aoc_util.run_with_data_str(task, data_str)
aoc_util.run_with_data_set(task, day)
