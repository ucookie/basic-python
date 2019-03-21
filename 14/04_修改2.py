#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def debug():
    import inspect
    caller_name = inspect.stack()[1][3]
    print("[DEBUG]: enter {}()".format(caller_name))

# 每个模块中都包含验证模块, 修改验证功能只在验证模块中修改
def func1():
    debug()
    print('执行函数1')

def func2():
    debug()
    print('执行函数2')

def func3():
    debug()
    print('执行函数3')

def func4():
    debug()
    print('执行函数4')

def main():
    # 假如此处是在其他模块中调用
    func1()
    func2()
    func3()
    func4()

if __name__ == '__main__':
    main()
