###############################################################################
# Day x, Task y                                                               #
###############################################################################

import aoc_util
from collections import deque


day = 6
data_str = """3,4,3,1,2"""


def fix_to_states(fish):
    ret = [0] * 9
    for i in fish:
        ret[i] += 1

    return ret


def task(data_set: list[str]) -> int:
    fish = [int(x) for x in data_set[0].split(",")]
    states = fix_to_states(fish)

    for _ in range(256):
        val = states[0]
        for i in range(8):
            states[i] = states[i + 1]
        states[6] += val
        states[8] = val            


    return sum(states)


aoc_util.run_with_data_str(task, data_str)
aoc_util.run_with_data_set(task, day)
