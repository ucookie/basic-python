#!/usr/bin/env python3
# -*- coding: utf-8 -*-
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

        number = input('请选择(Ctrl + c 退出):')

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
        # (number, name)
        students_list = Model.get_all_students()

        print('')
        for each_one in students_list:
            print('学号:%s  姓名:%s' % each_one)
        print('')

        raise(KeyboardInterrupt)

    @classmethod
    def search(cls):
        '''查询'''
        option_view = '''
        1. 查询学生信息
        2. 查询成绩
        '''
        print('查询导航'.center(cls.width + 2, '='))
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
        number = input('输入学号: ')
        student = Model.search_student_detail(number)

        gender = {'True': '男', 'False': '女'}
        detail = '''
        姓名: %s
        班级: %s
        年龄: %s
        性别: %s
        学号: %s
        ''' % (
            student[0], student[1], student[2], gender[student[3]], number
        )
        title = '%s同学详细信息' % student[0]
        print(title.center(cls.width, '='))
        print(detail)
        raise(KeyboardInterrupt)

    @classmethod
    def search_score(cls):
        '''查询成绩'''
        number = input('输入学号: ')
        score = Model.search_scores(number)

        sum_score = sum(score)
        avg_score = float(sum_score) / len(score)

        score_data = '''
        语文: %d
        数学: %d
        英语: %d
        美术: %d
        体育: %d
        总分: %d
        平均分: %.2f
        ''' % (
            score[0], score[1], score[2], score[3], score[4], sum_score, avg_score
        )

        title = '%s同学成绩' % Model.get_name(number)
        print(title.center(cls.width, '='))
        print(score_data)

        raise(KeyboardInterrupt)