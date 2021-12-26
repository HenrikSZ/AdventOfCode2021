###############################################################################
# Day x, Task y                                                               #
###############################################################################

import aoc_util, math


day = 18
data_str = """[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]"""


class SnailFishNumber:
    def __init__(self, s: str):
        self.number = []

        for i in s:
            if i.isdigit():
                self.number.append(int(i))
            elif i != ",":
                self.number.append(i)


    def __add__(self, other):
        result = SnailFishNumber("")

        result.number.append("[")
        result.number.extend(self.number)
        result.number.extend(other.number)
        result.number.append("]")

        result.reduce()

        return result


    def explode(self, i):
        to_add_left = self.number[i + 1]
        to_add_right = self.number[i + 2]

        left = i - 1
        right = i + 4

        while left >= 0:
            if type(self.number[left]) == int:
                self.number[left] += to_add_left
                break

            left -= 1


        while right < len(self.number):
            if type(self.number[right]) == int:
                self.number[right] += to_add_right
                break

            right += 1

        for _ in range(3):
            del self.number[i]

        self.number[i] = 0


    def split(self, i):
        n = self.number[i] / 2

        left = math.floor(n)
        right = math.ceil(n)

        self.number[i] = "["
        self.number.insert(i + 1, "]")
        self.number.insert(i + 1, right)
        self.number.insert(i + 1, left)


    def reduce(self):
        changed = True
        while changed == True:
            pair_count = 0
            changed = False
            for i, e in enumerate(self.number):
                if e == "[":
                    pair_count += 1
                elif e == "]":
                    pair_count -= 1

                if pair_count == 5:
                    self.explode(i)
                    changed = True
                    break

            if not changed:
                for i, e in enumerate(self.number):
                    if type(e) == int and e > 9:
                        self.split(i)
                        changed = True
                        break


    def mag_list(self, lst, pos):
        if lst[pos] == "[":
            open_count = 1
            end = pos + 1
            while 1:
                if lst[end] == "[":
                    open_count += 1
                elif lst[end] == "]":
                    open_count -= 1

                end += 1
                if open_count == 1:
                    break

            return 3 * self.mag_list(lst, pos + 1) \
                    + 2 * self.mag_list(lst, end)
        else:
            return lst[pos]


    def magnitude(self):
        return self.mag_list(self.number, 0)


def task(data_set: list[str]) -> int:
    parsed_numbers = []
    for n in data_set:
        parsed_numbers.append(SnailFishNumber(n))

    res = parsed_numbers[0]
    for i in parsed_numbers[1:]:
        res += i

    return res.magnitude()


aoc_util.run_with_data_str(task, data_str)
aoc_util.run_with_data_set(task, day)
