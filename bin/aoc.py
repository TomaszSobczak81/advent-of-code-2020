#!/usr/bin/env python
import os
import sys

import fire

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'src')))

from day.day_1_report_repair import Day1


class AoC2022(object):
    def day_1_report_repair(self):
        Day1().solve()


if __name__ == '__main__':
    fire.Fire(AoC2022)
