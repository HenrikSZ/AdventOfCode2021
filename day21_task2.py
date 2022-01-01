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


def play(steps_to_universes, n, pos, score, step_count):
    step_count += 1
    for p in range(3, 10):
        new_pos = (pos + p) % 10
        new_score = score + new_pos + 1

        if new_score >= 21:
            steps_to_universes[step_count] = steps_to_universes.get(step_count, 0) + n
        else:
            play(steps_to_universes,
                n * dice_roll_to_n[p],
                new_pos,
                new_score,
                step_count
                )


def task(data_set: list[str]) -> int:
    pos_1 = int(data_set[0][-1]) - 1
    pos_2 = int(data_set[1][-1]) - 1

    steps_to_universes_1 = {}
    steps_to_universes_2 = {}

    play(steps_to_universes_1, 1, pos_1, 0, 0)
    play(steps_to_universes_2, 1, pos_2, 0, 0)

    sorted_keys_1 = sorted(steps_to_universes_1.keys())
    sorted_keys_2 = sorted(steps_to_universes_2.keys())

    player_1_wins = 0
    player_2_wins = 0

    sum_1 = sum(steps_to_universes_1.values())
    sum_2 = sum(steps_to_universes_2.values())

    for i in sorted_keys_1:
        mult = steps_to_universes_1[i]
        acc = 0

        for j in sorted_keys_2:
            if i <= j:
                acc += steps_to_universes_2[j]

        player_1_wins += acc * mult


    for i in sorted_keys_2:
        mult = steps_to_universes_2[i]
        acc = 0

        for j in sorted_keys_1:
            if i < j:
                acc += steps_to_universes_1[j]

        player_2_wins += acc * mult


    return max(player_1_wins, player_2_wins)


aoc_util.run_with_data_str(task, data_str)
aoc_util.run_with_data_set(task, day)
