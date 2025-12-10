#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    print("Введите больше 10 результатов спортсменов через пробел:")
    result = list(map(int, input().split()))

    if len(result) <= 10:
        print("Кол-во спортсменов должно быть > 10!", file=sys.stderr)
        exit(1)

    luchshij_result = min(result)

    print(f"Лучший результат на дистанции 200 м: {luchshij_result} секунд")