#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# '学生信息系统'.center(50, '=')
from .model import Model

class View(object):

    width = 40

    @classmethod
    def menu(cls):
        """主菜单"""

        option_view = '''
        1. 列出所有学生
        2. 查询
        '''
        print('学生信息系统'.center(cls.width, '='))
        print(option_view)

        number = input('请选择:')

        func_dict = {
            '1': cls.list_student,
            '2': cls.search,
        }

        if number not in func_dict.keys():
            raise Exception('【提示】:输入有误, 请重新选择')

        func = func_dict[number]

        is_exit = False
        while not is_exit:
            try:
                func()
            except KeyboardInterrupt:
                print('回到主菜单')
                is_exit = True
            except Exception as ex:
                raise ex

    @classmethod
    def list_student(cls):
        '''列出所有学生'''
        print('list student')
        raise(KeyboardInterrupt)

    @classmethod
    def search(cls):
        '''查询'''
        option_view = '''
        1. 查询学生信息
        2. 查询成绩
        '''
        print('学生信息系统'.center(cls.width, '='))
        print(option_view)

        number = input('请选择(Ctrl + c 返回上一级):')

        func_dict = {
            '1': cls.search_student,
            '2': cls.search_score,
        }

        if number not in func_dict.keys():
            raise Exception('【提示】:输入有误, 请重新选择')

        func = func_dict[number]

        is_exit = False
        while not is_exit:
            try:
                func()
            except KeyboardInterrupt:
                is_exit = True
            except Exception as ex:
                raise ex

    @classmethod
    def search_student(cls):
        '''查询学生信息'''
        number = input('输入学号')
        print('查询信息', number)
        raise(KeyboardInterrupt)

    @classmethod
    def search_score(cls):
        '''查询成绩'''
        number = input('输入学号')
        print('查询', number)
        raise(KeyboardInterrupt)