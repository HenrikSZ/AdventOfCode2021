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
        return 3
    if s == "]":
        return 57
    if s == "}":
        return 1197
    if s == ">":
        return 25137


def task(data_set: list[str]) -> int:
    score = 0
    for line in data_set:
        chars = []
        for i in line:
            if i in "([<{":
                chars.append(i)
            else:
                last = chars.pop()
                if last == "(" and i != ")" \
                    or last == "[" and i != "]" \
                    or last == "{" and i != "}" \
                    or last == "<" and i != ">":
                    score += score_sign(i)
                    break
    return score



aoc_util.run_with_data_str(task, data_str)
aoc_util.run_with_data_set(task, day)
