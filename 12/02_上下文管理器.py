#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 方法1
class OpenFile(object):
    def __init__(self, filepath):
        self.__file = open(filepath)

    def print_line(self):
        for line in self.__file:
            print(line)

    def __enter__(self):
        return self.__file

    def __exit__(self, exc_type, exc_value, traceback):
        self.__file.close()
        return True

a = OpenFile('file.txt')
a.print_line()

# 方法2
try:
    f = open('file.txt')
    for line in f:
        print(line)
except Exception as e:
    print(e)
finally:
    f.close()

# 方法3：使用with
with open('file.txt') as fobj:
    print(fobj.read())