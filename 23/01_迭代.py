#!/usr/bin/env python3
# -*- coding: utf-8 -*-

for i in [1, 2, 3]:
    print(i)

for i in "abcdef":
    print(i)

for i in 100:
    print(i)

# 可迭代的类型, 才能使用 for
from collections import Iterable
isinstance(100, Iterable)


