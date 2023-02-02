#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time


def select(poezd, nom):
    count = 0
    for idx, po in enumerate(poezd, 1):
        if po["no"] == str(nom):
            print(
                "Название пункта: ",
                po["name"],
                "\nВремя отправления: ",
                time.strftime("%H:%M:%S", po["t"]),
            )
            count += 1

    if count == 0:
        print("Поезда с таким номером нет")
