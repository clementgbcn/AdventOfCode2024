from day_factory.day import Day
from utils.utils import extract_int


class Day02(Day):
    FIRST_STAR_TEST_RESULT = 2
    SECOND_STAR_TEST_RESULT = 4

    def __init__(self):
        super().__init__(self)

    @staticmethod
    def valid_report(report, tolerate_error=False):
        increasing_level = report[0] < report[1]
        for idx in range(len(report) - 1):
            diff = report[idx + 1] - report[idx]
            if (
                (increasing_level and diff < 0)
                or (not increasing_level and diff > 0)
                or diff == 0
                or abs(diff) > 3
            ):
                if not tolerate_error:
                    return False
                else:
                    return (
                        (
                            Day02.valid_report(report[: idx - 1] + report[idx:])
                            if idx > 0
                            else False
                        )
                        or Day02.valid_report(report[:idx] + report[idx + 1 :])
                        or Day02.valid_report(report[: idx + 1] + report[idx + 2 :])
                    )
        return True

    @staticmethod
    def check_reports(input_value):
        return sum(
            map(lambda x: 1 if Day02.valid_report(extract_int(x)) else 0, input_value)
        )

    @staticmethod
    def check_reports_2(input_value):
        return sum(
            map(
                lambda x: 1 if Day02.valid_report(extract_int(x), True) else 0,
                input_value,
            )
        )

    def solution_first_star(self, input_value, input_type):
        return self.check_reports(input_value)

    def solution_second_star(self, input_value, input_type):
        return self.check_reports_2(input_value)
