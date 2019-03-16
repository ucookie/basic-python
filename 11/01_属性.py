#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Student(object):
    school = '实验小学'

    def __init__(self, name):
        self.name = name

s1 = Student('小明')
s2 = Student('小红')

print(s1.name)
print(s1.school)

print(Student.school)


# 修改实例属性
s1.name = '小小明'

# 修改类属性
s1.school = '第一小学'
print(s1.school)
print(Student.school)

# 方法一
Student.school = '第一小学'
print(s1.school)

# 方法二
s1.__class__.school = '第一小学'
print(s2.school)