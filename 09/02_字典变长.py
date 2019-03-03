#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 传统方法
# def count(student):
#     ...
# count(s1)

# 使用字典变长参数
def count(**kwargs):
    if 'math' in kwargs:
        if kwargs['math'] > 80:
            print(kwargs['name'], '优秀')
        else:
            print(kwargs['name'], '合格')
    else:
        print(kwargs['name'], '未找到数学成绩')

count(name='小明', math=90)