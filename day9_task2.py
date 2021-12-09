###############################################################################
# Day 9, Task 1                                                               #
###############################################################################

import aoc_util


day = 9
data_str = """2199943210
3987894921
9856789892
8767896789
9899965678"""


def basin_find(height_map, row, col):
    size = 1
    height_map[row][col] = -1
    if row > 0 and height_map[row - 1][col] != 9 and height_map[row - 1][col] != -1:
        size += basin_find(height_map, row - 1, col)
    if row < len(height_map) - 1 and height_map[row + 1][col] != 9 and height_map[row + 1][col] != -1:
        size += basin_find(height_map, row + 1, col)
    if col > 0 and height_map[row][col - 1] != 9 and height_map[row][col - 1] != -1:
        size += basin_find(height_map, row, col - 1)
    if col < len(height_map[0]) - 1 and height_map[row][col + 1] != 9 and height_map[row][col + 1] != -1:
        size += basin_find(height_map, row, col + 1)

    return size


def task(data_set: list[str]) -> int:
    height_map = []
    for i in data_set:
        height_map.append([int(x) for x in i.replace("\n", "")])
    
    sizes = []
    for row in range(len(height_map)):
        for col in range(len(height_map[0])):
            if height_map[row][col] != 9 and height_map[row][col] != -1:
                sizes.append(basin_find(height_map, row, col))

    sizes.sort()
    sizes = sizes[-3:]
    return sizes[0] * sizes[1] * sizes[2]


aoc_util.run_with_data_str(task, data_str)
aoc_util.run_with_data_set(task, day)
