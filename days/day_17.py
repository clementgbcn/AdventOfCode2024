import logging

from day_factory.day import Day
from day_factory.day_utils import TestEnum
from utils.input_parser import InputParser
from utils.utils import extract_int

logger = logging.getLogger(__name__)

DISPLAY_BOT = False


class Memory:
    def __init__(self, a, b, c):
        self.pointer = 0
        self.a = a
        self.b = b
        self.c = c
        self.output = []

    def get_operand(self, op):
        if op < 4:
            return op
        if op == 4:
            return self.a
        if op == 5:
            return self.b
        if op == 6:
            return self.c

    def execute(self, instructions):
        while self.pointer < len(instructions):
            instructions[self.pointer].execute(
                instructions[self.pointer + 1].code, self
            )


class Instruction:
    def __init__(self, code):
        self.code = code

    def execute(self, op, mem: Memory):
        if self.code == 0:
            mem.a = mem.a // (2 ** mem.get_operand(op))
        elif self.code == 1:
            mem.b = mem.b ^ op
        elif self.code == 2:
            mem.b = mem.get_operand(op) % 8
        elif self.code == 3 and mem.a != 0:
            mem.pointer = op
            return
        elif self.code == 4:
            mem.b = mem.b ^ mem.c
        elif self.code == 5:
            mem.output.append(mem.get_operand(op) % 8)
        elif self.code == 6:
            mem.b = mem.a // (2 ** mem.get_operand(op))
        elif self.code == 7:
            mem.c = mem.a // (2 ** mem.get_operand(op))
        mem.pointer += 2


class Day17(Day):
    FIRST_STAR_TEST_RESULT = 5730
    SECOND_STAR_TEST_RESULT = 117440

    def __init__(self):
        super().__init__(self)

    @staticmethod
    def extract_input(input_value: InputParser):
        iterator = input_value.get_iterator()
        a = extract_int(next(iterator))[0]
        b = extract_int(next(iterator))[0]
        c = extract_int(next(iterator))[0]
        mem = Memory(a, b, c)
        next(iterator)
        ops = extract_int(next(iterator))
        instructions = [Instruction(x) for x in ops]
        return mem, ops, instructions

    @staticmethod
    def compute_robots(input_value: InputParser) -> int:
        mem, _, instructions = Day17.extract_input(input_value)
        mem.execute(instructions)
        print(f"String to copy: {mem.output}")
        return int("".join([str(x) for x in mem.output]))

    @staticmethod
    def compute_robots_2(input_value: InputParser, input_type) -> int:
        mem, ops, instructions = Day17.extract_input(input_value)
        res = 0
        current = 0
        while res < len(ops):
            current *= 8
            for idx in range(64):
                m = Memory(current + idx, mem.b, mem.c)
                m.execute(instructions)
                if m.output[0] == ops[-res - 1]:
                    current += idx
                    res += 1
                    break
        return current

    def solution_first_star(
        self, input_value: InputParser, input_type: TestEnum
    ) -> int:
        return self.compute_robots(input_value)

    def solution_second_star(
        self, input_value: InputParser, input_type: TestEnum
    ) -> int:
        return self.compute_robots_2(input_value, input_type)
