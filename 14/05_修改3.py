#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def debug(func):
    def wrapper():
        print "[DEBUG]: enter {}()".format(func.__name__)
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
    say_hello = debug(func1)
    say_hello = debug(func2)
    say_hello = debug(func3)
    say_hello = debug(func4)

if __name__ == '__main__':
    main()
