#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def func_log(func):
    def wrapper(*args, **kwargs):
        print("[DEBUG]: enter {0}()".format(func.__name__))
        print('Prepare and say...',)
        return func(*args, **kwargs)
    return wrapper  # 返回


@func_log
def func1(name):
    print('执行函数1, my name is', name)

@func_log
def func2(doing):
    print('执行函数2, the action is', doing)

def main():
    # 假如此处是在其他模块中调用
    func1('python')
    func2('runing')

if __name__ == '__main__':
    main()
