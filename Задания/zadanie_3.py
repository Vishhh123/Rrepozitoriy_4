#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    print("Введите целые числа через пробел:")
    a = tuple(map(int, input().split()))

    if not a:
        print("Кортеж пуст!", file=sys.stderr)
        exit(1)

    print(f"Исходный кортеж a: {a}")

    b_list = []

    for i in a:
        if i % 2 == 0:
            b_list.append(i * 2)
        else:
            b_list.append(i)

    b = tuple(b_list)

    print(f"Результирующий кортеж b: {b}")


    