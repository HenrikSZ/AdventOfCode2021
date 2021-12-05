###############################################################################
# Day x, Task y                                                               #
###############################################################################

import aoc_util


day = 5
data_str = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""


def task(data_set: list[str]) -> int:
    num = 0
    vents_map = {}
    for line in data_set:
        coords = line.split(" -> ")
        [x1, y1] = [int(x) for x in coords[0].split(",")]
        [x2, y2] = [int(x) for x in coords[1].split(",")]

        if x1 == x2:
            begin = min(y1, y2)
            end = max(y1, y2) + 1
            for i in range(begin, end):
                val = vents_map.setdefault((x1, i), 0) + 1
                if val == 2:
                    num += 1

                vents_map[(x1, i)] = val
                
        
        if y1 == y2:
            begin = min(x1, x2)
            end = max(x1, x2) + 1
            for i in range(begin, end):
                val = vents_map.setdefault((i, y1), 0) + 1
                if val == 2:
                    num += 1

                vents_map[(i, y1)] = val

    return num




aoc_util.run_with_data_str(task, data_str)
aoc_util.run_with_data_set(task, day)
