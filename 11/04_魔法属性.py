#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Student(object):
    """学生信息结构"""
    school = '实验小学'
    def __init__(self, name):
        self.name = name


s1 = Student('小明')
print(s1.__doc__)
print(Student.__doc__)