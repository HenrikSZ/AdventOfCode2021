###############################################################################
# Day x, Task y                                                               #
###############################################################################

import math
import aoc_util


day = 24
data_str = """"""


class InputSet:
    def __init__(self):
        self.lst = [9] * 14
        self.index = -1


    def get_next_number(self):
        self.index += 1
        return self.lst[self.index]


    def generate_next_input(self):
        self.index = -1

        curr_mod = 13
        while 1:
            self.lst[curr_mod] -= 1
            if self.lst[curr_mod] >= 1:
                break

            self.lst[curr_mod] = 9
            curr_mod -= 1


class RegisterSet:
    def __init__(self):
        self.reset()
    

    def reset(self):
        self.w = 0
        self.x = 0
        self.y = 0
        self.z = 0


    def get(self, str):
        if str[0] == "-" or str[0].isdigit():
            return int(str)
        if str == "w":
            return self.w
        if str == "x":
            return self.x
        if str == "y":
            return self.y
        if str == "z":
            return self.z


    def set(self, str, val):
        if str == "w":
            self.w = val
        if str == "x":
            self.x = val
        if str == "y":
            self.y = val
        if str == "z":
            self.z = val


class Instruction:
    def __init__(self, line, register):
        self.register = register

        spl = line.split(" ")

        op = spl[0]
        if len(spl) == 2:
            self.arg1 = spl[1]
            self.arg2 = ""
        else:
            self.arg1 = spl[1]
            self.arg2 = spl[2]

        if op == "inp":
            self.execute = self.input
        if op == "add":
            self.execute = self.add
        if op == "mul":
            self.execute = self.multiply
        if op == "div":
            self.execute = self.divide
        if op == "mod":
            self.execute = self.modulo
        if op == "eql":
            self.execute = self.equal


    def input(self, input):
        self.register.set(self.arg1, input.get_next_number())


    def add(self, input):
        self.register.set(self.arg1,
        self.register.get(self.arg1) + self.register.get(self.arg2))


    def multiply(self, input):
        self.register.set(self.arg1,
        self.register.get(self.arg1) * self.register.get(self.arg2))


    def divide(self, input):
        self.register.set(self.arg1,
        math.trunc(self.register.get(self.arg1) / self.register.get(self.arg2)))


    def modulo(self, input):
        self.register.set(self.arg1,
        self.register.get(self.arg1) % self.register.get(self.arg2))


    def equal(self, input):
        self.register.set(self.arg1,
        int(self.register.get(self.arg1) == self.register.get(self.arg2)))



class Program:
    def __init__(self, lines):
        self.instructions = []
        self.registers = RegisterSet()

        for i in lines:
            self.instructions.append(Instruction(i, self.registers))


    def is_valid_n(self, input_set):
        self.registers.reset()
        for instr in self.instructions:
            instr.execute(input_set)

        #print(self.registers.z)

        return self.registers.z == 0


def task(data_set: list[str]) -> int:
    program = Program(data_set)

    input_set = InputSet()

    while not program.is_valid_n(input_set):
        input_set.generate_next_input()


    return "".join([int(d) for d in input_set.lst])


#aoc_util.run_with_data_str(task, data_str)
aoc_util.run_with_data_set(task, day)
