#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time


def list(poezd):
    if poezd:
        line = "+-{}-+-{}-+-{}-+-{}-+".format("-" * 4, "-" * 30, "-" * 20, "-" * 13)
        print(line)
        print(
            "| {:^4} | {:^30} | {:^20} | {:^13} |".format(
                "No", "Название пункта", "Номер поезда", "Время"
            )
        )
        print(line)
        for idx, po in enumerate(poezd, 1):
            print(
                "| {:>4} | {:<30} | {:<20} | {}{} |".format(
                    idx,
                    po.get("name", ""),
                    po.get("no", ""),
                    time.strftime("%H:%M:%S", po.get("t", 0)),
                    " " * 5,
                )
            )
        print(line)
