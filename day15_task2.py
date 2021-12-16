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
        self.source_list = self.matrix[0].copy()
        for i in range(1, len(self.matrix)):
            self.source_list.extend(self.matrix[i])
        self.vertices = list(range(len(matrix) * len(matrix[0])))
        self.dists = [sys.maxsize] * (len(matrix) * len(matrix[0]))
        self.is_visited_matrix = [False] * (len(matrix) * len(matrix[0]))

        self.dists[0] = 0


    def find_min_distance_vertex(self):
        min_dist_vertex = 0
        distance = sys.maxsize
        index = 0
        for i, k in enumerate(self.vertices):
            if self.dists[k] < distance:
                distance = self.dists[k]
                min_dist_vertex = k
                index = i

        return distance, index, min_dist_vertex


    def act_on_neighbour(self, n, distance):
        alt = distance + self.source_list[n]
        if alt < self.dists[n]:
            self.dists[n] = alt


    def update_neighbours(self, vertex, distance):
        col = vertex % len(self.matrix[0])
        row = vertex // len(self.matrix[0])
        if row > 0 and not self.is_visited_matrix[vertex - len(self.matrix[0])]:
            self.act_on_neighbour(vertex - len(self.matrix[0]), distance)
        if col > 0 and not self.is_visited_matrix[vertex - 1]:
            self.act_on_neighbour(vertex - 1, distance)
        if col < len(self.matrix[0]) - 1 and not self.is_visited_matrix[vertex + 1]:
            self.act_on_neighbour(vertex + 1, distance)
        if row < len(self.matrix) - 1 and not self.is_visited_matrix[vertex + len(self.matrix[0])]:
            self.act_on_neighbour(vertex + len(self.matrix[0]), distance)


    def solve(self):
        while 1:
            if len(self.vertices) % 1000 == 0:
                print(len(self.vertices))
                
            distance, index, min_distance_vertex = self.find_min_distance_vertex()
            del self.vertices[index]
            self.is_visited_matrix[min_distance_vertex] = True

            self.update_neighbours(min_distance_vertex, distance)

            if min_distance_vertex == len(self.matrix) * len(self.matrix[0]) - 1:
                return self.dists[min_distance_vertex]


def task(data_set: list[str]) -> int:
    risk_map = []
    for i in data_set:
        row = [int(x) for x in i]
        extension = row
        for _ in range(4):
            extension = [x + 1 if x < 9 else 1 for x in extension]
            row.extend(extension)

        risk_map.append(row)

    for row in range(4 * len(data_set)):
        new_row = [x + 1 if x < 9 else 1 for x in risk_map[row]]
        risk_map.append(new_row)
        
    dijkstra = Dijkstra(risk_map)

    return dijkstra.solve()



aoc_util.run_with_data_str(task, data_str)
aoc_util.run_with_data_set(task, day)
