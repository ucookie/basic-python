#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 使用字典方式
s = {'name':'小明', 'number':'201901'}

# 使用类的方式
class Student(object):
    def __init__(self):
        self.name = ''
        self.number = ''

# 完善类
class StudentNew(object):
    def __init__(self):
        self.name = ''
        self.number = ''
        self.gender = True
        self.class_num = 1

    def get_number(self):
        '''获取学号'''
        return self.number

    def update_class_num(self, num):
        '''修改班级'''
        self.class_num = num