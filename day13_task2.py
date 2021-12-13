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

    while i < len(data_set):
        dots = fold(dots, data_set[i])
        i += 1

    min_x = 100000000000000
    max_x = 0
    min_y = 100000000000000
    max_y = 0
    for i in dots:
        if i[0] < min_x:
            min_x = i[0]
        elif i[0] > max_x:
            max_x = i[0]
        
        if i[1] < min_y:
            min_y = i[1]
        elif i[1] > max_y:
            max_y = i[1]

    result = [[" "] * (max_x - min_x + 1) for _ in range(max_y - min_y + 1)]

    for i in dots:
        result[i[1] - min_y][i[0] - min_x] = "X"

    for row in result:
        for col in row:
            print(col, end="")

        print()
    return 0


aoc_util.run_with_data_str(task, data_str)
aoc_util.run_with_data_set(task, day)
