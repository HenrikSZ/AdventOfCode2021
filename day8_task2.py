###############################################################################
# Day 8, Task 1                                                               #
###############################################################################


import aoc_util


day = 8
data_str = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""


def intersect_option(o, n, l):
    o[n] = o[n].intersection(l)


def resolve_num(num, options):
    l = len(num)
    ns = set([ord(x) - ord("a") for x in num])

    if l == 2:
        return 1
    elif l == 3:
        return 7
    elif l == 4:
        return 4
    elif l == 7:
        return 8
    elif l == 5:
        if options[1] in ns:
            return 5
        else:
            if options[5] in ns:
                return 3
            else:
                return 2
    elif l == 6:
        if options[2] in ns:
            if options[4] in ns:
                return 0
            else:
                return 9
        else:
            return 6


def optimize_intersects(options):
    all_unique = False
    while not all_unique:
        all_unique = True
        for i in options:
            if len(i) == 1:
                for index in range(len(options)):
                    if len(options[index]) > 1:
                        options[index] = options[index].difference(i)
            else:
                all_unique = False

    converted_options = []
    for o in options:
        converted_options.append(o.pop())

    return converted_options


def determine_intersects(nums):
    options = [set([x for x in range(7)])] * 7

    for n in nums:
        length = len(n)
        char_list = set([ord(x) - ord("a") for x in n])
        
        if length == 2:
            intersect_option(options, 2, char_list)
            intersect_option(options, 5, char_list)
        elif length == 3:
            intersect_option(options, 0, char_list)
            intersect_option(options, 2, char_list)
            intersect_option(options, 5, char_list)
        elif length == 4:
            intersect_option(options, 1, char_list)
            intersect_option(options, 2, char_list)
            intersect_option(options, 3, char_list)
            intersect_option(options, 5, char_list)
        elif length == 5:
            intersect_option(options, 0, char_list)
            intersect_option(options, 3, char_list)
            intersect_option(options, 6, char_list)
        elif length == 6:
            intersect_option(options, 0, char_list)
            intersect_option(options, 1, char_list)
            intersect_option(options, 5, char_list)
            intersect_option(options, 6, char_list)

    return optimize_intersects(options)


def task(data_set: list[str]) -> int:
    count = 0
    for l in data_set:
        
        nums = l.replace("\n", "").split(" ")
        nums.remove("|")

        options = determine_intersects(nums)

        output = nums[-4:]
        curr_num = 0
        for index, n in enumerate(output):
            curr_num += resolve_num(n, options) * (10 ** (3 - index))

        count += curr_num


    return count


aoc_util.run_with_data_str(task, data_str)
aoc_util.run_with_data_set(task, day)
