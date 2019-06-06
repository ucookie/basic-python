#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 1. 直接执行
# import time

# def create1():
#     while True:
#         print(1)
#         time.sleep(0.5)

# def create2():
#     while True:
#         print(2)
#         time.sleep(0.5)

# create1()
# create2()

# 2. 多任务

import time

def create1():
    while True:
        print(1)
        time.sleep(0.5)
        yield

def create2():
    while True:
        print(2)
        time.sleep(0.5)
        yield
c1 = create1()
c2 = create2()
while True:
    next(c1)
    next(c2)