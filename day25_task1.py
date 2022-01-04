###############################################################################
# Day x, Task y                                                               #
###############################################################################

import aoc_util


day = 25
data_steasy = """...>...
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
    grid = []

    for l in data_set:
        row = [c for c in l]
        grid.append(row)

    steps = 0

    moved = True
    while moved:
        moved = False
        for row in range(len(grid)):
            last_was_occupied = False
            col = 0
            while col < len(grid[0]):
                if grid[row][col] == "." and grid[row][col - 1] == ">" \
                    and (col != len(grid[0]) - 1 or not last_was_occupied):
                    if col == 0:
                        last_was_occupied = True
                    grid[row][col] = ">"
                    grid[row][col - 1] = "."
                    moved = True
                    col += 1
                col += 1
                

        for col in range(len(grid[0])):
            last_was_occupied = False
            row = 0
            while row < len(grid):
                if grid[row][col] == "." and grid[row - 1][col] == "v" \
                    and (row != len(grid) - 1 or not last_was_occupied):
                    if row == 0:
                        last_was_occupied = True
                    grid[row][col] = "v"
                    grid[row - 1][col] = "."
                    moved = True
                    row += 1
                row += 1
        steps += 1

    return steps


#aoc_util.run_with_data_str(task, data_steasy)
aoc_util.run_with_data_str(task, data_str)
aoc_util.run_with_data_set(task, day)
