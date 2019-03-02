#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 输入第一个数字
num1 = input('请输入第一个数字：')
operate = input('请输入运算符号：')
num2 = input('请输入第二个数字：')

num1 = int(num1)
num2 = int(num2)

# 进行计算
if operate == '+':
    result = num1 + num2
    print(num1, operate, num2, '=', result)
elif operate == '-':
    result = num1 - num2
    print(num1, operate, num2, '=', result)
elif operate == '*':
    result = num1 * num2
    print(num1, operate, num2, '=', result)
elif operate == '/':
    result = num1 / num2
    print(num1, operate, num2, '=', result)
else:
    print('operate error')
