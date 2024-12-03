import fire


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

    @staticmethod
    def day06():
        from aoc.day06 import Day06

        Day06(str(11), str(6)).solve()

    @staticmethod
    def day07():
        from aoc.day07 import Day07

        Day07(str(4), str(126)).solve()

    @staticmethod
    def day08():
        from aoc.day08 import Day08

        Day08(str(5), str(8)).solve()

    @staticmethod
    def day09():
        from aoc.day09 import Day09

        Day09(str(127), str(62)).solve()

    @staticmethod
    def day10():
        from aoc.day10 import Day10

        Day10(str(220), str(19208)).solve()

    @staticmethod
    def day11():
        from aoc.day11 import Day11

        Day11(str(37), str(26)).solve()

    @staticmethod
    def day12():
        from aoc.day12 import Day12

        Day12(str(25), str(286)).solve()

    @staticmethod
    def day13():
        from aoc.day13 import Day13

        Day13(str(295), str(1068781)).solve()

    @staticmethod
    def day14():
        from aoc.day14 import Day14

        Day14(str(165), str(208)).solve()


if __name__ == "__main__":
    fire.Fire(AoC2022)
