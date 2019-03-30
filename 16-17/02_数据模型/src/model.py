#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import csv
import inspect

def script_path():
    '''获取脚本绝对路径'''
    this_file = inspect.getfile(inspect.currentframe())
    return os.path.abspath(os.path.dirname(this_file))
CURR_SCRIPT_PATH = script_path()

# 数据文件路径
DATA_PATH = os.path.join(os.path.dirname(CURR_SCRIPT_PATH), 'data')

class Model(object):
    '''数据处理模块'''

    @classmethod
    def get_all_students(cls):
        '''获取所有学生概况'''
        students_list = list()

        with open(os.path.join(DATA_PATH, 'id.csv'), 'r') as fobj:
            csv_obj = csv.reader(fobj)
            for number, name in csv_obj:
                students_list.append((number, name))

        return students_list

    @classmethod
    def search_student_detail(cls, number):
        '''根据学号查询学生详细信息'''
        with open(os.path.join(DATA_PATH, 'students', '%s.csv' % number), 'r') as fobj:
            data = fobj.read().strip().split(',')

        return data

    @classmethod
    def search_scores(cls, number):
        '''根据学号查询学生分数'''
        with open(os.path.join(DATA_PATH, 'scores', '%s.csv' % number), 'r') as fobj:
            data = fobj.read().strip().split(',')

        # 转换成整型
        for index, value in enumerate(data):
            data[index] = int(value)

        return data

    @classmethod
    def get_name(cls, number):
        '''根据学号查询姓名'''
        with open(os.path.join(DATA_PATH, 'id.csv'), 'r') as fobj:
            csv_obj = csv.reader(fobj)
            for sid, name in csv_obj:
                if sid == number:
                    return name


if __name__ == '__main__':
    for x in Model.get_all_students():
        print(x)

    print(Model.search_student_detail('001'))
    print(Model.search_scores('002'))
    print(Model.get_name('001'))