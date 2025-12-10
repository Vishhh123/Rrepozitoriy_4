#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    print("Введите целые числа через пробел:")
    a = list(map(int, input().split()))

    if not a:
        print("Список пуст!", file=sys.stderr)
        exit(1)

    print(f"\nИсходный список: {a}")

    #Номер максимального элемента
    max_index = a.index(max(a))
    print(f"Номер максимального элемента: {max_index} (значение {a[max_index]})")

    #Произведение между нулевыми элементами
    if a.count(0) >= 2:
        first_zero = a.index(0)
        second_zero = a.index(0, first_zero + 1)

        product = 1
        for q in a[first_zero + 1:second_zero]:
            product = q * product

        print(f"Произведение между нулевыми элементами = {product}")
    else:
        print("Недостаточно нулевых элементов")

    #Преобразование списка
    pervaya_polovina = [a[i] for i in range(len(a)) if i % 2 == 1]
    vtoraya_polovina = [a[i] for i in range(len(a)) if i % 2 == 0]
    spisok = pervaya_polovina + vtoraya_polovina

    print(f"Преобразованный список: {spisok}")








