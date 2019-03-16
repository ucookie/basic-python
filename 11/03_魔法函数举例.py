#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Student(object):

    school = '实验小学'
    def __init__(self, name):
        self.name = name

    # def __str__(self):
    #     return self.school + ':' + self.name

s1 = Student('小明')
print(str(s1))