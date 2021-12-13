###############################################################################
# Day x, Task y                                                               #
###############################################################################

import aoc_util


day = 13
data_str = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""


def fold(dots, instr):
    [axis, val] = instr.replace("fold along ", "").split("=")

    val = int(val)

    new_dots = set([])
    if axis == "x":
        for i in dots:
            if i[0] < val:
                new_dots.add(i)
            else:
                new_dots.add((val - (i[0] - val), i[1]))
    elif axis == "y":
        for i in dots:
            if i[1] < val:
                new_dots.add(i)
            else:
                new_dots.add((i[0], val - (i[1] - val)))
    
    return new_dots


def task(data_set: list[str]) -> int:
    dots = set([])
    i = 0
    while data_set[i] != "":
        [x, y] = data_set[i].split(",")
        dots.add((int(x), int(y)))
        i += 1

    i += 1
    dots = fold(dots, data_set[i])

    return len(dots)


aoc_util.run_with_data_str(task, data_str)
aoc_util.run_with_data_set(task, day)
