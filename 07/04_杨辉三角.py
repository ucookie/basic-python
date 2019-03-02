#!/usr/bin/env python3
# -*- coding: utf-8 -*-

Last = [1]
row = int(input("输入行数："))
width = row * 4 # 设置打印宽度

for x in range(row):
    s = ""
    for x in Last:
        s += str(x) + "  "
    print(s.center(width))

    Curr = [1]
    for x in range(1, len(Last)):
        Curr.append(Last[x] + Last[x-1])
    Curr.append(1)
    Last = Curr