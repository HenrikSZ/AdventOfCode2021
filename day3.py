###############################################################################
# Day 3, Task 1                                                               #
###############################################################################

with open("data_day3.txt") as f:
    init = [0] * 12
    for l in f:
        for i in range(12):
            if l[i] == "1":
                init[i] += 1

    low = 0
    high = 0
    for i in range(12):
        if init[i] > 500:
            high += 2 ** (11 - i)
        else:
            low += 2 ** (11 - i)

    print(low * high)    



###############################################################################
# Day 3, Task 2                                                               #
###############################################################################

def find_rating(lines: list[str], keep_on_more_1: str, keep_on_less_1: str) -> int:
    lines = lines.copy()

    current_position = 0
    while len(lines) > 1:
        count1 = 0
        for i in lines:
            if i[current_position] == "1":
                count1 += 1

        keep = ""
        if count1 >= len(lines) / 2:
            keep = keep_on_more_1
        else:
            keep = keep_on_less_1

        lines = [i for i in lines if i[current_position] == keep]

        current_position += 1

    return int(lines[0], 2)


with open("data_day3.txt") as f:
    lines = f.readlines()

    val1 = find_rating(lines, "1", "0")
    val2 = find_rating(lines, "0", "1")

    print(val1 * val2)

