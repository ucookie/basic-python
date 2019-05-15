#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# class Students(object):
#     def __init__(self):
#         self.names = list()
#     def add(self, name):
#         self.names.append(name)

# s = Students()
# s.add('小明')
# s.add('小红')
# s.add('小华')

# for name in s:
#     print(s)

# 普通类无法实现迭代

class Students(object):
    def __init__(self):
        self.names = list()
    def add(self, name):
        self.names.append(name)
    def __iter__(self):
        return ClassIterator()

class ClassIterator(object):
    def __iter__(self):
        pass
    def __next__(self):
        pass

s = Students()
s.add('小明')
s.add('小红')
s.add('小华')

from collections import Iterable
print('是否为可迭代对象:', isinstance(s, Iterable))

for name in s:
    print(s)

# __iter__方法需要返回一个具有 __inter__方法和 __next__ 方法的对象的引用