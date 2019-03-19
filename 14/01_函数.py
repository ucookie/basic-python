#!/usr/bin/env python3
# -*- coding: utf-8 -*-

在python中，函数通过def关键字、函数名和可选的参数列表定义。通过return关键字返回值

函数参数
def foo(x):
     print locals()
foo(1)


def foo(x, y=0): # 1
     return x - y
foo(3, 1) # 2
2
foo(3) # 3
3
foo() # 4
Traceback (most recent call last):

TypeError: foo() takes at least 1 argument (0 given)
foo(y=1, x=3) # 5
2



嵌套函数
def outer():
     x = 1
     def inner():
         print x # 1
     inner() # 2

outer()
1


闭包
def outer():
     x = 1
     def inner():
         print x # 1
     return inner
foo = outer()
foo.func_closure # doctest: +ELLIPSIS
(<cell at 0x: int object at 0x>,)


装饰器
def outer(some_func):
     def inner():
         print "before some_func"
         ret = some_func() # 1
         return ret + 1
     return inner
def foo():
     return 1
decorated = outer(foo) # 2
decorated()
before some_func
2


class Coordinate(object):
     def __init__(self, x, y):
         self.x = x
         self.y = y
     def __repr__(self):
         return "Coord: " + str(self.__dict__)
def add(a, b):
     return Coordinate(a.x + b.x, a.y + b.y)
def sub(a, b):
     return Coordinate(a.x - b.x, a.y - b.y)
one = Coordinate(100, 200)
two = Coordinate(300, 200)
add(one, two)
Coord: {'y': 400, 'x': 400}


使用@符的装饰器
add = wrapper(add)
@wrapper
 def add(a, b):
     return Coordinate(a.x + b.x, a.y + b.y)