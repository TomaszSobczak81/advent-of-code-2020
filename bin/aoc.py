#!/usr/bin/env python
import os
import sys

import fire

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'src')))


from day.day_1_report_repair import Day1
from day.day_2_password_philosophy import Day2


class AoC2022(object):
    @staticmethod
    def day_1_report_repair():
        Day1().solve()

    @staticmethod
    def day_2_password_philosophy():
        Day2().solve()


if __name__ == '__main__':
    fire.Fire(AoC2022)
