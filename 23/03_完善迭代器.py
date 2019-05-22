#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Students(object):
    def __init__(self):
        self.names = list()

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        return ClassIterator(self)

class ClassIterator(object):

    def __init__(self, obj):
        self.obj = obj
        self.curr = 0

    def __iter__(self):
        pass

    # def __next__(self):
    #     ret = self.obj.names[self.curr]
    #     self.curr += 1
    #     return ret

    # def __next__(self):
    #     if self.curr < len(self.obj.names):
    #         ret = self.obj.names[self.curr]
    #         self.curr += 1
    #         return ret

    def __next__(self):
        if self.curr < len(self.obj.names):
            ret = self.obj.names[self.curr]
            self.curr += 1
            return ret
        else:
            raise StopIteration

s = Students()
s.add('小明')
s.add('小红')
s.add('小华')

from collections import Iterable
print('是否为可迭代对象:', isinstance(s, Iterable))

for name in s:
    print(name)

# __iter__方法需要返回一个具有 __inter__方法和 __next__ 方法的对象的引用