#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 学校成员基类
class SchoolMember(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

# 学生子类
class Student(SchoolMember):
    def __init__(self, name, gender, parent):
        SchoolMember.__init__(self, name, gender)
        # 学生家长
        self.parent = parent

# 老师子类
class Teacher(SchoolMember):
    def __init__(self, name, gender):
        SchoolMember.__init__(self, name, gender)
        # 老师管理的班级
        self.manage_class = 1
        # 老师的电话
        self.phone_num = '1234567'

    def get_phone_num(self):
        return self.phone_num

    def update_manage_class(self, class_num):
        self.manage_class = class_num

# 定义一个学生
s1 = Student('小明', True, '大明')

# 定义一个老师
t1 = Teacher('小华', False)

# 查看老师电话
print(t1.get_phone_num())

# 修改老师管理班级
t1.update_manage_class(9)
print(t1.manage_class)