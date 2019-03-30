#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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
        # 前后换行, 控制格式
        print('')
        # (number, name)
        # 先设计好数据格式
        for each_one in [('001', '小明'), ('002', '小红')]:
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

        # 此处待获取信息
        # (姓名, 班级, 年龄, 性别, 学号)
        gender = {'True': '男', 'False': '女'}
        detail = '''
        姓名: %s
        班级: %s
        年龄: %s
        性别: %s
        学号: %s
        ''' % ('小明', '201901', 20, gender['True'], '001')

        # 标题
        title = '小明同学详细信息'
        print(title.center(cls.width, '='))
        print(detail)
        raise(KeyboardInterrupt)

    @classmethod
    def search_score(cls):
        '''查询成绩'''
        number = input('输入学号: ')

        # 此处待获取分数
        # (int, int, ...)
        score = (100, 100, 100, 100, 100)
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

        title = '小明同学成绩'
        print(title.center(cls.width, '='))
        print(score_data)

        raise(KeyboardInterrupt)