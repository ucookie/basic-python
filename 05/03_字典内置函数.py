#!/usr/bin/env python3
# -*- coding: utf-8 -*-


s1 = {'name': '小明', 'gender': True, 'age': 18, 'number': '2019001'}

s1.get('name')
s1.get('name', 'nobody')

s1.setdefault('age')
s1.setdefault('age', 18)

s1.keys()
s1.values()

list()强制转换
循环遍历