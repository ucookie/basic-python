#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# json是一种轻量级的数据交换语言, 该语言以易于让人阅读的文字为基础，用来传输由属性值或者序列性的值组成的数据对象, json是独立于语言的文本格式

# json的优势
# 在http当中的使用

import json

student = {}
s1 = {'name': '小明', 'class_num': '2019,01', 'age': 18}
s2 = {'name': '小红', 'class_num': '2019,02', 'age': 18}
s3 = {'name': '小蓝', 'class_num': '2019,01', 'age': 19}
student['01'] = s1
student['02'] = s2
student['03'] = s3
# print(student)

# 展示
js = json.dumps(student, sort_keys=True, indent=4, separators=(',', ':'), ensure_ascii=False)
# print(js)

# 编码成json字符串
js = json.dumps(student)
print(js)

# 要输出中文需要指定ensure_ascii参数为False
js = json.dumps(student, ensure_ascii=False)
print(js)
# 本质是一个字符串
print(type(js))

# 写入文件
with open('student.json', 'w') as fjson:
    fjson.write(js)


# 从文件读取
with open('student.json', 'r') as fjson:
    data = fjson.read()
    print(data)
    json_obj = json.loads(data)
    # 先输出
    print(json_obj)

    # 完整打印
    print(json_obj['01'])
    print(json_obj['02'])
    print(json_obj['03'])