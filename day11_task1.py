###############################################################################
# Day 11, Task 1                                                              #
###############################################################################

import aoc_util


day = 11
data_str = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""


def flash_octi(octi, row, col):
    flashes = 0
    octi[row][col] += 1
    if octi[row][col] == 10:
        flashes += 1
        if row > 0:
            flashes += flash_octi(octi, row - 1, col)
            if col > 0:
                flashes += flash_octi(octi, row - 1, col - 1)
            if col < len(octi[0]) - 1:
                flashes += flash_octi(octi, row - 1, col + 1)
        if col > 0:
            flashes += flash_octi(octi, row, col - 1)
        if col < len(octi[0]) - 1:
            flashes += flash_octi(octi, row, col + 1)
        if row < len(octi) - 1:
            flashes += flash_octi(octi, row + 1, col)
            if col > 0:
                flashes += flash_octi(octi, row + 1, col - 1)
            if col < len(octi[0]) - 1:
                flashes += flash_octi(octi, row + 1, col + 1)

    return flashes


def task(data_set: list[str]) -> int:
    octi = []
    for i in data_set:
        row = []
        for o in i:
            row.append(int(o))
        octi.append(row)

    flashes = 0
    for i in range(100):
        for row in range(len(octi)):
            for col in range(len(octi[0])):
                flashes += flash_octi(octi, row, col)

        for i in range(len(octi)):
            for j in range(len(octi[0])):
                if octi[i][j] > 9:
                    octi[i][j] = 0
                

    return flashes


aoc_util.run_with_data_str(task, data_str)
aoc_util.run_with_data_set(task, day)
