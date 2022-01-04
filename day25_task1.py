###############################################################################
# Day x, Task y                                                               #
###############################################################################

import aoc_util


day = 25
data_str_easy = """...>...
.......
......>
v.....>
......>
.......
..vvv.."""
data_str = """v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>"""


def task(data_set: list[str]) -> int:
    r_grid = []
    d_grid = []

    for l in data_set:
        row = [c for c in l]
        r_grid.append(row)
        d_grid.append(row.copy())

    steps = 0

    moved = True
    while moved:
        moved = False
        for row in range(len(r_grid)):
            for col in range(len(r_grid[0])):
                if r_grid[row][col] == "." and r_grid[row][col - 1] == ">":
                    d_grid[row][col] = ">"
                    d_grid[row][col - 1] = "."
                    moved = True
                else:
                    d_grid[row][col] = r_grid[row][col]

        d_grid[2][-1] = "."

        for row in range(len(r_grid)):
            for col in range(len(r_grid[0])):
                if d_grid[row][col] == "." and d_grid[row - 1][col] == "v":
                    r_grid[row][col] = "v"
                    r_grid[row - 1][col] = "."
                    moved = True
                else:
                    r_grid[row][col] = d_grid[row][col]

        steps += 1

    return steps


aoc_util.run_with_data_str(task, data_str_easy)
aoc_util.run_with_data_str(task, data_str)
aoc_util.run_with_data_set(task, day)
