#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 学生信息
name = '小明'
gender = True
age = 18
number = 2019001

# 方法1
s1 = {'name': '小明', 'gender': True, 'age': 18, 'number': '2019001'}



# 方法2
s2 = dict()
s2['name'] = '小红'
s2['gender'] = False
s2['age'] = 18
s2['number'] = '2019002'

print(s1, s2)

# 打印学号
print(s1['number'])
print(s2['number'])

# 打印不存在的值
print(s1['class'])

# key不能相同
s3 = {'name': '小明', 'name': '小红'}

# 键必须不可变，所以可以用数字，字符串或元组充当，所以用列表就不行
s4 = {['name']:'小华'}
s4 = {('name'):'小华'}

