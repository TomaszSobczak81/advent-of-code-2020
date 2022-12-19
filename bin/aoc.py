#!/usr/bin/env python

import fire

from day.day_1_report_repair import Day1
from day.day_2_password_philosophy import Day2
from day.day_3_toboggan_trajectory import Day3
from day.day_4_passport_processing import Day4


class AoC2022(object):
    @staticmethod
    def day_1_report_repair():
        Day1().solve()

    @staticmethod
    def day_2_password_philosophy():
        Day2().solve()

    @staticmethod
    def day_3_toboggan_trajectory():
        Day3().solve()

    @staticmethod
    def day_4_passport_processing():
        Day4().solve()


if __name__ == '__main__':
    fire.Fire(AoC2022)
