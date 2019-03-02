#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 打印到3截止
for i in range(0, 10):
    if i == 3:
        break
    print(i, end=' ')

# 不打印数字3
for i in range(0, 10):
    if i == 3:
        continue
    print(i, end=' ')