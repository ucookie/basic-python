#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

# print(fib(50))

# 利用全局缓存优化
memo = {0:0, 1:1}
def fib_great(n):
    if n not in memo:
        memo[n] = fib_great(n-1) + fib_great(n-2)
    return memo[n]
print(fib_great(50))