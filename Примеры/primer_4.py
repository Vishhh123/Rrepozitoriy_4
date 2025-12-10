#!/usr/bin/env python3
# -*- coding: utf-8 -*-


A = ("Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat")

day = str(input("Enter day: "))

if day in A:
    num = A.index(day)
    print("Number of day =", num + 1)
else:
    num = -1
    print("Wrong day.")