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

with open("data_day3.txt") as f:
    lines1 = f.readlines()
    lines2 = lines1.copy()

    current_position = 0
    while len(lines1) > 1:
        count1 = 0
        for i in lines1:
            if i[current_position] == "1":
                count1 += 1

        if count1 >= len(lines1) / 2:
            destroy = "0"
        else:
            destroy = "1"

        i = 0
        while i < len(lines1):
            if lines1[i][current_position] == destroy:
                lines1.remove(lines1[i])
                i -= 1

            i += 1

        current_position += 1

    current_position = 0
    while len(lines2) > 1:
        count1 = 0
        for i in lines2:
            if i[current_position] == "1":
                count1 += 1

        if count1 >= len(lines2) / 2:
            destroy = "1"
        else:
            destroy = "0"

        i = 0
        while i < len(lines2):
            if lines2[i][current_position] == destroy:
                lines2.remove(lines2[i])
                i -= 1

            i += 1
 
        current_position += 1


    print(int(lines1[0], 2) * int(lines2[0], 2))

