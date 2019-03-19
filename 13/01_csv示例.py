#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv

DATA = (('小明', '2019,01', 18, True, '1300000001'),
        ('小红', '2019,02', 18, False, '1300000002'),
        ('小蓝', '2019,01', 19, True, '1300000002'),
        )

print('写入文件')

with open('students.csv', 'w') as fcsv:
    csv_obj = csv.writer(fcsv)

    for student in DATA:
        csv_obj.writerow(student)

print('读取csv文件')

with open('students.csv', 'r') as fcsv:
    csv_obj = csv.reader(fcsv)
    for name, class_num, age, gender, phone_number in csv_obj:
        print('姓名:%s' % name,
              '班级:%s' % class_num,
              '年龄:%s' % age,
              '性别:%s' % gender,
              '电话:%s' % phone_number)
