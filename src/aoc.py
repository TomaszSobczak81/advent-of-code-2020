import fire

# from day.day_1_report_repair import Day1
# from day.day_2_password_philosophy import Day2
# from day.day_3_toboggan_trajectory import Day3
# from day.day_4_passport_processing import Day4
# from day.day_5_binary_boarding import Day5


class AoC2022(object):
    @staticmethod
    def day00():
        from aoc.day00 import Day00
        Day00(str(123), str(123)[::-1]).solve()

    @staticmethod
    def day01():
        from aoc.day01 import Day01
        Day01(str(514579), str(241861950)).solve()

    @staticmethod
    def day02():
        from aoc.day02 import Day02
        Day02(str(2), str(1)).solve()

    @staticmethod
    def day03():
        from aoc.day03 import Day03
        Day03(str(7), str(336)).solve()

    @staticmethod
    def day04():
        from aoc.day04 import Day04
        Day04(str(2), str(2)).solve()

    @staticmethod
    def day05():
        from aoc.day05 import Day05
        Day05(str(357), str(358)).solve()

if __name__ == '__main__':
    fire.Fire(AoC2022)
