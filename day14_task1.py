###############################################################################
# Day x, Task y                                                               #
###############################################################################

import aoc_util


day = 14
data_str = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""


def task(data_set: list[str]) -> int:
    struct = [x for x in data_set[0]]
    mapping = {}
    for e in data_set[2:]:
        [from_e, to_e] = e.split(" -> ")

        mapping[(from_e[0], from_e[1])] = to_e
    for _ in range(10):
        i = 1
        while i < len(struct):
            element = mapping.get((struct[i - 1], struct[i]))
            if element is not None:
                struct.insert(i, element)
                i += 1

            i += 1

    element_to_count = {}
    for i in struct:
        element_to_count[i] = element_to_count.setdefault(i, 0) + 1

    least = 10000000000
    most = 0
    for v in element_to_count.values():
        if v > most:
            most = v
        if v < least:
            least = v
    
    return most - least


aoc_util.run_with_data_str(task, data_str)
aoc_util.run_with_data_set(task, day)
