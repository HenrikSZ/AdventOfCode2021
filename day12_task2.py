###############################################################################
# Day 12, Task 1                                                              #
###############################################################################

import aoc_util


day = 12
#data_str = """fs-end
"""he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""
data_str = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""


def options_from(paths, visited, double, curr_node):
    option_count = 0
    visited = visited.copy()

    if curr_node.islower():
        visited.append(curr_node)

    if curr_node == "end":
        option_count = 1
    else:
        next_nodes = paths[curr_node]
        for i in next_nodes:
            if i not in visited:
                option_count += options_from(paths, visited, double, i)
            elif not double and i != "start" and i != "end":
                option_count += options_from(paths, visited, i, i)
    
    return option_count


def task(data_set: list[str]) -> int:
    paths = {}
    for i in data_set:
        [start, end] = i.split("-")
        paths.setdefault(start, []).append(end)
        paths.setdefault(end, []).append(start)


    return options_from(paths, [], None, "start")


aoc_util.run_with_data_str(task, data_str)
aoc_util.run_with_data_set(task, day)
