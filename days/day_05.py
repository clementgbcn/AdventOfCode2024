from day_factory.day import Day
from utils.utils import extract_int


class Day05(Day):
    FIRST_STAR_TEST_RESULT = 143
    SECOND_STAR_TEST_RESULT = 123

    def __init__(self):
        super().__init__(self)

    @staticmethod
    def compute_program(input_value):
        rules = Day05.extract_rules(input_value)
        total = 0
        for line in input_value:
            updates = extract_int(line)
            if not Day05.is_invalid(updates, rules):
                total += updates[len(updates) // 2]
        return total

    @staticmethod
    def compute_program_2(input_value):
        rules = Day05.extract_rules(input_value)
        total = 0
        for line in input_value:
            updates = extract_int(line)
            if not Day05.is_invalid(updates, rules):
                continue
            for idx, update in enumerate(updates):
                constraint = rules.get(update, set())
                subset = set(updates[:idx] + updates[idx + 1 :])
                if len(constraint.intersection(subset)) == len(updates) // 2:
                    total += update
                    break
        return total

    @staticmethod
    def extract_rules(input_value):
        rules = {}
        for line in input_value:
            if line == "":
                break
            values = extract_int(line)
            new_set = rules.get(values[0], set())
            new_set.add(values[1])
            rules[values[0]] = new_set
        return rules

    @staticmethod
    def is_invalid(updates, rules):
        encountered_updates = set()
        is_invalid = False
        for update in updates:
            encountered_updates.add(update)
            if update not in rules:
                continue
            for constraint in list(rules[update]):
                if constraint in encountered_updates:
                    is_invalid = True
                    break
            if is_invalid:
                break
        return is_invalid

    def solution_first_star(self, input_value, input_type):
        return self.compute_program(input_value)

    def solution_second_star(self, input_value, input_type):
        return self.compute_program_2(input_value)
