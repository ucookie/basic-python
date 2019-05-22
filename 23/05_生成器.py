#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 生成器是一类特殊的迭代器

# 1. 创建一个简单的生成器
L = [ x*2 for x in range(5) ]

# 将中括号改为小括号

L = ( x*2 for x in range(5) )

# 2.
def create(num):
    while num <= 0:
        print(num)
        num -= 1
create(10)
# 如果一个函数中有 yield 语句, 变成了一个生成器模板
# 在调用函数的时候, 发现这个函数中有 yield， 那么此时不是调用函数, 而是返回生成器对象
