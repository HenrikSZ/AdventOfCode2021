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

        mapping[(from_e[0], from_e[1])] = ((from_e[0], to_e), (to_e, from_e[1]))

    pairs = {}
    for i in range(1, len(struct)):
        pair = (struct[i - 1], struct[i])
        pairs[pair] = pairs.setdefault(pair, 0) + 1

    element_to_count = {}
    for e in pairs.keys():
        element_to_count[e[1]] = element_to_count.setdefault(e[1], 0) + pairs[e]

    element_to_count[struct[0]] = element_to_count.setdefault(struct[0], 0) + 1

    for _ in range(40):
        new_pairs = {}
        for k in pairs.keys():
            value = pairs[k]
            
            maps_to = mapping[k]
            new_pairs[maps_to[0]] = new_pairs.setdefault(maps_to[0], 0) + value
            new_pairs[maps_to[1]] = new_pairs.setdefault(maps_to[1], 0) + value

            element_to_count[maps_to[0][1]] = element_to_count.setdefault(maps_to[0][1], 0) + value


        pairs = new_pairs

    occurence_counts = list(element_to_count.values())
    least = occurence_counts[0]
    most = occurence_counts[0]
    for v in occurence_counts[1:]:
        if v > most:
            most = v
        if v < least:
            least = v
    
    return most - least


aoc_util.run_with_data_str(task, data_str)
aoc_util.run_with_data_set(task, day)
