#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def add(new_item, save_list=[]):
    save_list.append(new_item)
    return save_list

print(add('1'))
print(add('2'))



# 初始化后，就有了函数名到函数对象这样一个映射关系，
# 可以通过函数名访问到函数对象了，并且，
# 函数的一切属性也确定下来，包括所需的参数，默认参数的值