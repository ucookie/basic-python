#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def calc(numbers):
    sum = 0
    for n in numbers:
        sum += n*n
    return sum

a_list = [1,2,3,4]
calc(a_list)

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum=sum+n*n
    return sum
calc(1,2,3,4)