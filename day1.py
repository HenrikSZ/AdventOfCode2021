###############################################################################
# Day 1, Task 1                                                               #
###############################################################################

count_increased = 0

with open("data_day1.txt") as f:
    last_depth = int(f.readline())
    for l in f:
        new_depth = int(l)
        if new_depth > last_depth:
            count_increased += 1

        last_depth = new_depth

print(count_increased)


###############################################################################
# Day 1, Task 2                                                               #
###############################################################################

count_increased = 0

with open("data_day1.txt") as f:
    current_window = 0
    lines = f.readlines()
    last_depth = 0
    for i, n in enumerate(lines):
        last_depth = current_window
        current_window += int(lines[i])

        if i >= 3:
            current_window -= int(lines[i - 3])
            if current_window > last_depth:
                count_increased += 1


print(count_increased)
