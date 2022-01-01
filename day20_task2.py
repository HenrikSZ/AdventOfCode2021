###############################################################################
# Day x, Task y                                                               #
###############################################################################

import aoc_util


day = 20
data_str = """..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###"""


def set_lit(mapping, old, new, row, col, step):
    count = 0
    is_outside = step % 2 == 1 and mapping[0] == "#"

    if row > 0:
        if col > 0 and old[row - 1][col - 1] == "#":
            count |= 0b100000000
        if old[row - 1][col] == "#":
            count |= 0b010000000
        if col < len(old[0]) - 1 and old[row - 1][col + 1] == "#":
            count |= 0b001000000
    elif is_outside:
        count |= 0b111000000

    if col > 0:
        if old[row][col - 1] == "#":
            count |= 0b000100000
    elif is_outside:
        count |= 0b100100100

    if old[row][col] == "#":
        count |= 0b000010000

    if col < len(old[0]) - 1:
        if old[row][col + 1] == "#":
            count |= 0b000001000
    elif is_outside:
        count |= 0b001001001

    if row < len(old) - 1:
        if col > 0 and old[row + 1][col - 1] == "#":
            count |= 0b000000100
        if old[row + 1][col] == "#":
            count |= 0b000000010
        if col < len(old[0]) - 1 and old[row + 1][col + 1] == "#":
            count |= 0b000000001
    elif is_outside:
        count |= 0b000000111

    new[row][col] = mapping[count]


def get_num_lit_pixels(grid):
    num_lit = 0

    for row in grid:
        for v in row:
            if v == "#":
                num_lit += 1

    return num_lit


def task(data_set: list[str]) -> int:
    replacement = data_set[0]
    num_steps = 50

    old_grid = []
    new_grid = []

    for _ in range(num_steps):
        old_grid.append(["."] * (len(data_set[2]) + 2 * num_steps))
        new_grid.append(["."] * (len(data_set[2]) + 2 * num_steps))

    for i in range(2, len(data_set)):
        row = ["."] * num_steps
        row += data_set[i]
        row += ["."] * num_steps

        old_grid.append(row)
        new_grid.append(row.copy())

    for _ in range(num_steps):
        old_grid.append(["."] * (len(data_set[2]) + 2 * num_steps))
        new_grid.append(["."] * (len(data_set[2]) + 2 * num_steps))


    for i in range(num_steps):
        for row in range(0, len(old_grid)):
            for col in range(0, len(old_grid[0])):
                set_lit(replacement, old_grid, new_grid, row, col, i)

        tmp = old_grid
        old_grid = new_grid
        new_grid = tmp


    return get_num_lit_pixels(old_grid)


aoc_util.run_with_data_str(task, data_str)
aoc_util.run_with_data_set(task, day)
