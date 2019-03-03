#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def print_str(name='world'):
    print_str('hello', name)

print_str()
print_str('python')


# 计算连加
def sum(n=2):
    if n < 2:
        return -1
    result = 0
    for x in range(0, n+1):
        result += x
    return result
print(sum(n))