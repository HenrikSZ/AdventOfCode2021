###############################################################################
# Day x, Task y                                                               #
###############################################################################

import aoc_util


day = 21
data_str = """Player 1 starting position: 4
Player 2 starting position: 8"""


def get_next_three_numbers(n):
    ret = 0
    
    for _ in range(3):
        ret += n
        n += 1
        if n == 101:
            n = 1

    return ret, n


def task(data_set: list[str]) -> int:
    pos_1 = int(data_set[0][-1]) - 1
    pos_2 = int(data_set[1][-1]) - 1

    score_1 = 0
    score_2 = 0

    n = 1

    dice_rolls = 0

    while 1:
        throw, n = get_next_three_numbers(n)
        dice_rolls += 3
        pos_1 += throw
        pos_1 %= 10
        score_1 += (pos_1 + 1)

        if score_1 >= 1000:
            return score_2 * dice_rolls

        throw, n = get_next_three_numbers(n)
        dice_rolls += 3
        pos_2 += throw
        pos_2 %= 10
        score_2 += (pos_2 + 1)

        if score_2 >= 1000:
            return score_1 * dice_rolls


aoc_util.run_with_data_str(task, data_str)
aoc_util.run_with_data_set(task, day)
