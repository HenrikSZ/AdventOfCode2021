###############################################################################
# Day x, Task y                                                               #
###############################################################################

import aoc_util


day = 6
data_str = """3,4,3,1,2"""


def task(data_set: list[str]) -> int:
    fish = [int(x) for x in data_set[0].split(",")]

    for _ in range(80):
        for f in range(len(fish)):
            val = fish[f] - 1

            if val == -1:
                fish[f] = 6
                fish.append(8)
            else:
                fish[f] = val

    return len(fish)


aoc_util.run_with_data_str(task, data_str)
aoc_util.run_with_data_set(task, day)
