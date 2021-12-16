###############################################################################
# Day x, Task y                                                               #
###############################################################################

import aoc_util, sys


day = 16
data_str = """880086C3E88112"""


class BitParser():
    def __init__(self, string):
        self.string = string
        self.int_bit_count = 0
        self.index = 0
        self.current_number = int(string[self.index], base=16)
        self.parsed_bits_count = 0

    def get_next_n_bits(self, n: int) -> int:
        number = 0
        while n > 0:
            if self.int_bit_count == 4:
                self.int_bit_count = 0
                self.index += 1
                self.current_number = int(self.string[self.index], base=16)
            number <<= 1
            significant_bit = self.current_number & 0b1000
            significant_bit >>= 3
            number |=  significant_bit
            self.current_number <<= 1
            self.int_bit_count += 1
            n -= 1
            self.parsed_bits_count += 1

        return number

    def get_parsed_bits_count(self) -> int:
        return self.parsed_bits_count


class Packet():
    def add_version_numbers(self) -> int:
        return 0


class LiteralPacket(Packet):
    def __init__(self, version, bit_parser):
        self.version = version
        self.value = 0
        while 1:
            bits = bit_parser.get_next_n_bits(5)
            self.value <<= 4
            self.value |= bits & 0b01111
            if (bits & 0b10000) == 0b00000:
                break

    def add_version_numbers(self) -> int:
        return self.version


class OperatorPacket(Packet):
    def __init__(self, version: int, type: int, bit_parser: BitParser):
        self.version = version
        self.type = type
        self.length_type = bit_parser.get_next_n_bits(1)
        self.packet_list: list[Packet] = []
        if self.length_type == 1:
            sub_packet_num = bit_parser.get_next_n_bits(11)
            for _ in range(sub_packet_num):
                self.packet_list.append(parse_packet(bit_parser))
        else:
            sub_packet_len = bit_parser.get_next_n_bits(15)
            pre_parser_count = bit_parser.get_parsed_bits_count()
            while bit_parser.get_parsed_bits_count() - pre_parser_count < sub_packet_len:
                self.packet_list.append(parse_packet(bit_parser))
        
    def add_version_numbers(self) -> int:
        acc = self.version
        for packet in self.packet_list:
            acc += packet.add_version_numbers()

        return acc


def parse_packet(bit_parser: BitParser) -> Packet:
    version = bit_parser.get_next_n_bits(3)
    type = bit_parser.get_next_n_bits(3)
    if type == 4:
        return LiteralPacket(version, bit_parser)
    else:
        return OperatorPacket(version, type, bit_parser) 


def task(data_set: list[str]) -> int:
    bit_parser = BitParser(data_set[0])
    packet = parse_packet(bit_parser)

    return packet.add_version_numbers()


aoc_util.run_with_data_str(task, data_str)
aoc_util.run_with_data_set(task, day)
