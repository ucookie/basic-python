#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def func1():
    print('[debug]: 进入函数1')
    print('执行函数1')

def func2():
    print('[debug]: 进入函数2')
    print('执行函数2')

def func3():
    print('[debug]: 进入函数3')
    print('执行函数3')

def func4():
    print('[debug]: 进入函数4')
    print('执行函数4')

def main():
    # 假如此处是在其他模块中调用
    func1()
    func2()
    func3()
    func4()

if __name__ == '__main__':
    main()
