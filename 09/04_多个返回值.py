#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_name():
    error = ''
    name = '小明'
    return name, error
s_name, err = get_name()


def get_obj():
    name = '小明'
    age = 18
    gender = True
    return name, age, gender

s_tuple = get_obj()

s1 = dict()
s1['name'] = s_tuple[0]
s1['age'] = s_tuple[1]
s1['gender'] = s_tuple[2]
