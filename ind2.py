#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from Packet.add import add
from Packet.list import list
from Packet.select import select
from Packet.help import help


def main():
    poezd = []
    while True:
        command = input(">>> ").lower()
        if command == "exit":
            break
        elif command == "add":
            po = add()
            poezd.append(po)
        elif command == "list":
            list(poezd)
        elif command.startswith("select"):
            nom = input("Введите номер поезда: ")
            select(poezd, nom)
        elif command == "help":
            help()
        else:
            print(f"неизвестная команда {command}", file=sys.stderr)


if __name__ == "__main__":
    main()
