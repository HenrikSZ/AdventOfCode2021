###############################################################################
# Day x, Task y                                                               #
###############################################################################

import aoc_util


day = 21
data_str = """Player 1 starting position: 4
Player 2 starting position: 8"""


dice_roll_to_n = {
    3: 1,
    4: 3,
    5: 6,
    6: 7,
    7: 6,
    8: 3,
    9: 1
}


def play(n, pos_1, pos_2, score_1, score_2):
    if score_2 >= 21:
        return 0, n
    
    player_1_wins = 0
    player_2_wins = 0

    for p in range(3, 10):
        new_pos_1 = (pos_1 + p) % 10
        new_score_1 = score_1 + new_pos_1 + 1

        player_2_wins_tmp, player_1_wins_tmp = play(
            n * dice_roll_to_n[p],
            pos_2,
            new_pos_1,
            score_2,
            new_score_1
        )

        player_1_wins += player_1_wins_tmp
        player_2_wins += player_2_wins_tmp

    return player_1_wins, player_2_wins


def task(data_set: list[str]) -> int:
    pos_1 = int(data_set[0][-1]) - 1
    pos_2 = int(data_set[1][-1]) - 1

    player_1_wins, player_2_wins = play(1, pos_1, pos_2, 0, 0)

    return max(player_1_wins, player_2_wins)


aoc_util.run_with_data_str(task, data_str)
aoc_util.run_with_data_set(task, day)
