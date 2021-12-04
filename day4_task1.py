###############################################################################
# Day 4, Task 1                                                               #
###############################################################################

import aoc_util

day = 4
data_str = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""


def check_board(board):
    cols_finished = [True] * 5
    for row in board:
        row_finished = True
        for i, n in enumerate(row):
            if not n[1]:
                row_finished = False
                cols_finished[i] = False

        if row_finished:
            return True

    for n in cols_finished:
        if n:
            return True

    return False


def count_board(board):
    count = 0
    for row in board:
        for c in row:
            if c[1] == False:
                count += c[0]

    return count



def task(data_set: list[str]) -> int:
    bingo_boards = []

    for index, row in enumerate(data_set[1:]):
        if index % 6 == 0:
            bingo_boards.append([])
        else:
            last = bingo_boards[-1]
            last.append([[int(x), False] for x in row.split()])

    nums = [int(x) for x in data_set[0].split(",")]
    for num in nums:
        for board in bingo_boards:
            for row in board:
                for e in row:
                    if e[0] == num:
                        e[1] = True
            if (check_board(board)):
                return count_board(board) * num



aoc_util.run_with_data_str(task, data_str)
aoc_util.run_with_data_set(task, day)
