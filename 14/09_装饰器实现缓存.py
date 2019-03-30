#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import wraps
def memoize(function):
    memo = {}
    @wraps(function)
    def wrapper(*args):
        if args in memo:
            return memo[args]
        else:
            rv = function(*args)
            memo[args] = rv
            return rv
    return wrapper

# 使用缓存，计算斐波拉协数
@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

ret = fibonacci(25)
print(ret)