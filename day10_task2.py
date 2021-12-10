###############################################################################
# Day 10, Task 1                                                              #
###############################################################################

import aoc_util


day = 10
data_str = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""


def score_sign(s):
    if s == ")":
        return 1
    if s == "]":
        return 2
    if s == "}":
        return 3
    if s == ">":
        return 4


def task(data_set: list[str]) -> int:
    scores = []
    for line in data_set:
        chars = []
        corrupted = False
        for i in line.replace("\n", ""):
            if i == "(":
                chars.append(")")
            elif i == "[":
                chars.append("]")
            elif i == "{":
                chars.append("}")
            elif i == "<":
                chars.append(">")
            else:
                last = chars.pop()
                if last != i:
                    corrupted = True
                    break

        if not corrupted:
            chars.reverse()
            score = 0
            for i in chars:
                score *= 5
                score += score_sign(i)

            scores.append(score)

    scores.sort()

    return scores[len(scores) // 2]



aoc_util.run_with_data_str(task, data_str)
aoc_util.run_with_data_set(task, day)
