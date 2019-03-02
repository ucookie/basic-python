#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# for循环
for i in range(0, 10):
    print(i)

# 循环和列表
num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in num_list:
    print(i)

# 循环和字典
s1 = {'name': '小明', 'gender': True, 'age': 18, 'number': '2019001'}
for k in s1:
    print(k)

for k in s1:
    print(k, ':', s1[k])