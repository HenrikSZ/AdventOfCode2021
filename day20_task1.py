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


def task(data_set: list[str]) -> int:
    lit_pixels = set()
    min_row = 0
    max_row = len(data_set) - 1
    min_col = 0
    max_col = len(data_set[2]) - 1

    replacement = data_set[0]

    for row in range(2, len(data_set)):
        for col in range(len(data_set[row])):
            if data_set[row][col] == "#":
                lit_pixels.add((row - 2, col))

    for i in range(2):
        new_lit_pixels = set()
        for row in range(min_row - 1, max_row + 2):
            for col in range(min_col - 1, max_col + 2):
                count = 0
                shift = 8
                for y in range(-1, 2):
                    for x in range(-1, 2):
                        if (row + y, col + x) in lit_pixels:
                            count |= (0b1 << shift)
                        elif data_set[0][0] == "#" and i % 2 == 1 \
                            and (row + y < min_row or row + y > max_row \
                            or col + x < min_col or col + x > max_col):
                            count |= (0b1 << shift)
                            new_lit_pixels.add((row + y, col + x))
                        shift -= 1

                if replacement[count] == "#":
                    new_lit_pixels.add((row, col))
                    min_row = min(min_row, row)
                    max_row = max(max_row, row)
                    min_col = min(min_col, col)
                    max_col = max(max_col, col)

        lit_pixels = new_lit_pixels

    return len(lit_pixels)


aoc_util.run_with_data_str(task, data_str)
aoc_util.run_with_data_set(task, day)
