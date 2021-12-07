###############################################################################
# Day 7, Task 1                                                               #
###############################################################################

import aoc_util


day = 7
data_str = """16,1,2,0,4,2,7,1,2,14"""


def task(data_set: list[str]) -> int:
    distances = [int(x) for x in data_set[0].split(",")]
    maximum = max(distances)
    minimum = min(distances)

    minimum_distance = 0
    for x in distances:
        minimum_distance += abs(minimum - x)

    for i in range(minimum + 1, maximum + 1):
        distance = 0
        for x in distances:
            distance += abs(i - x)

        if distance < minimum_distance:
            minimum_distance = distance

    return minimum_distance
   


aoc_util.run_with_data_str(task, data_str)
aoc_util.run_with_data_set(task, day)
