###############################################################################
# Day x, Task y                                                               #
###############################################################################

import aoc_util


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


def calculate_risk(risk_map, row, col):
    if row > 0:
        from_top = risk_map[row - 1][col] + risk_map[row][col]
    if col > 0:
        from_left = risk_map[row][col - 1] + risk_map[row][col]

    if row > 0 and col > 0:
        risk_map[row][col] = min(from_top, from_left)
    elif row > 0:
        risk_map[row][col] = from_top
    elif col > 0:
        risk_map[row][col] = from_left


def task(data_set: list[str]) -> int:
    risk_map = []
    for i in data_set:
        row = [int(x) for x in i]
        extension = row
        for _ in range(4):
            extension = [x + 1 if x < 9 else 1 for x in extension]
            row.extend(extension)

        risk_map.append(row)

    for row in range(0, 4 * len(data_set)):
        new_row = [x + 1 if x < 9 else 1 for x in risk_map[row]]
        risk_map.append(new_row)
        

    for row in range(len(risk_map)):
        for col in range(len(risk_map[0])):
            calculate_risk(risk_map, row, col)

    return risk_map[len(risk_map[0]) - 1][len(risk_map) - 1] - risk_map[0][0]



aoc_util.run_with_data_str(task, data_str)
aoc_util.run_with_data_set(task, day)
