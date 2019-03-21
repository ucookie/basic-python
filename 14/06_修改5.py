#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def debug(func):
    def wrapper():
        print("[DEBUG]: enter {}()".format(func.__name__))
        return func()
    return wrapper
# 这是最简单的装饰器，但是有一个问题，如果被装饰的函数需要传入参数，那么这个装饰器就坏了

# def debug(func):
#     def wrapper(*args, **kwargs):  # 指定宇宙无敌参数
#         print "[DEBUG]: enter {}()".format(func.__name__)
#         print 'Prepare and say...',
#         return func(*args, **kwargs)
#     return wrapper  # 返回


@debug
def func1():
    print('执行函数1')

@debug
def func2():
    print('执行函数2')

@debug
def func3():
    print('执行函数3')

@debug
def func4():
    print('执行函数4')

def main():
    # 假如此处是在其他模块中调用
    func1()
    func2()
    func3()
    func4()


if __name__ == '__main__':
    main()
