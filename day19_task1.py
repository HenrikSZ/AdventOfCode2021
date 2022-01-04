###############################################################################
# Day x, Task y                                                               #
###############################################################################

import aoc_util


day = 19
data_str = """"""


class Scanner:
    def __init__(self, data_set):
        [data, index] = data_set
        self.beacons = set()

        while index < len(data) and data[index] != "":
            self.beacons.add(tuple([int(x) for x in data[index].split(",")]))
            index += 1

        data_set[1] = index + 2


    def connect_to_scanner(self, other):
        pass


def task(data_set: list[str]) -> int:
    data_set = [data_set, 2]
    scanners = []

    while data_set[1] < len(data_set[0]):
        scanners.append(Scanner(data_set))


aoc_util.run_with_data_str(task, data_str)
aoc_util.run_with_data_set(task, day)
