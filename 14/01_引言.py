#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def foo():
    print('foo')

foo      # 函数对象
foo()    # 执行函数

def foo2():
    print('222')

foo = foo2

# 被第二个函数覆盖了
foo()