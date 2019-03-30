#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# id,姓名,班级,随机基准分
data = (
    ('001','小明','201901',True,90),
    ('002','小红','201902',False,90),
    ('003','小张','201902',True,70),
    ('004','小李','201904',True,80),
    ('005','小王','201903',True,80),
    ('006','小华','201905',True,80),
    ('007','小玉','201902',True,70),
    ('008','李明','201901',True,75),
    ('009','张红','201903',True,85),
    ('010','王华','201901',True,80),
)

import csv
import random

# 生成 id.csv
with open('id.csv', 'w') as fcsv:
    csv_obj = csv.writer(fcsv)
    for x in data:
        r = (x[0], x[1])
        csv_obj.writerow(r)

# 生成 student
for x in data:
    with open('students/%s.csv' % x[0], 'w') as fcsv:
        csv_obj = csv.writer(fcsv)
        # 姓名,班级,年龄,性别
        r = (x[1], x[2], random.randint(17,20), x[3])
        csv_obj.writerow(r)

# 生成 scores
for x in data:
    with open('scores/%s.csv' % x[0], 'w') as fcsv:
        csv_obj = csv.writer(fcsv)
        # 语文,数学,英语,美术,体育
        r = list()
        for _ in range(5):
            r.append(random.randint(x[4]-10, x[4]+10))
        csv_obj.writerow(r)
