#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Student(object):
    def o_func(self):
        print('实例方法')

    @classmethod
    def class_func(cls):
        print('类方法')

    @staticmethod
    def static_func():
        print('静态方法')


s1 = Student()
s1.o_func()
s1.class_func()
s1.static_func()

Student.class_func()
Student.static_func()