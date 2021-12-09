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


def task(data_set: list[str]) -> int:
    height_map = []
    for i in data_set:
        height_map.append([int(x) for x in i.replace("\n", "")])

    risk = 0
    for row in range(len(height_map)):
        for col in range(len(height_map[0])):
            val = height_map[row][col]
            if (row == 0 or height_map[row - 1][col] > val) \
                and (row == len(height_map) - 1 or height_map[row + 1][col] > val) \
                and (col == 0 or height_map[row][col - 1] > val) \
                and (col == len(height_map[0]) - 1 or height_map[row][col + 1] > val):
                risk += val + 1         

    return risk


aoc_util.run_with_data_str(task, data_str)
aoc_util.run_with_data_set(task, day)
