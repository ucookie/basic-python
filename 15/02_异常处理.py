#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 语法错误
while True print('hello python')

  File "d:/code/basic-python/15/02_异常处理.py", line 4
    while True print('hello python')
                   ^
SyntaxError: invalid syntax

# 异常
3 + '9'
Traceback (most recent call last):
  File "d:/code/basic-python/15/02_异常处理.py", line 13, in <module>
    3 + '9'
TypeError: unsupported operand type(s) for +: 'int' and 'str'


# 异常处理
def exception1():
    try:
        while True print('hello python')
    except Exception as ex:
        print('执行出错')
    print('继续执行其他任务')


# finally使用
def exception2():
    try:
        fobj = open('none.txt')
        fobj.read('100')
    except Exception as ex:
        print('读取文件失败')
    finally:
        fobj.close()


def exception2(a, b):
    try:
        print(a / b)
    except ZeroDivisionError:
        print("Error: b should not be 0 !!")
    except Exception as e:
        print("Unexpected Error: {}".format(e))
    else:
        print('Run into else only when everything goes well')
    finally:
        print('Always run into finally block.')
