#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def use_logging(level):
    def func_log(func):
        def wrapper(*args, **kwargs):
            if level == "debug":
                print("[DEBUG] %s is running" % func.__name__)
            elif level == "info":
                print("[INFO] %s is running" % func.__name__)
            return func(*args)
        return wrapper

    return func_log

@use_logging(level='debug')
def func1(name):
    print('执行函数1, my name is', name)

@use_logging(level='info')
def func2(doing):
    print('执行函数2, the action is', doing)


def main():
    # 假如此处是在其他模块中调用
    func1('python')
    func2('runing')

if __name__ == '__main__':
    main()
