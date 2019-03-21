#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def debug(func):
    def wrapper():
        print("[DEBUG]: enter {}()".format(func.__name__))
        return func()
    return wrapper

def func1():
    print('执行函数1')

def func2():
    print('执行函数2')

def func3():
    print('执行函数3')

def func4():
    print('执行函数4')

def main():
    # 假如此处是在其他模块中调用
    f1 = debug(func1)
    f1()
    f2 = debug(func2)
    f2()
    f3 = debug(func3)
    f3()
    f4 = debug(func4)
    f4()

if __name__ == '__main__':
    main()
