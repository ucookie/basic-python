#!/usr/bin/env python3
# -*- coding: utf-8 -*-



# match匹配
# re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none

import re
print(re.match('hello', 'hello python').span())  # 在起始位置匹配
print(re.match('python', 'hello python'))         # 不在起始位置匹配


line = "There two files: db.txt and data.txt"

matchObj = re.match( r'(.*) (.*\.txt)? and (.*)', line)

if matchObj:
   print("matchObj.group() : ", matchObj.group())
   print("matchObj.group(1) : ", matchObj.group(1))
   print("matchObj.group(2) : ", matchObj.group(2))
   print("matchObj.group(3) : ", matchObj.group(3))
else:
   print("No match!!")

# 字典分组
import re
m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Donald Trump")
person_obj = m.groupdict()
print(person_obj['first_name'])
print(person_obj['last_name'])

# search 匹配
# re.search 扫描整个字符串并返回第一个成功的匹配
import re
print(re.search('hello', 'hello python').span())  # 在起始位置匹配
print(re.search('python', 'hello python').span()) # 不在起始位置匹配


# 提取email address
string = 'xiaoming has an email, named xiaoming-cn@gmail.com'
match = re.search(r'\w+@\w+', string)
if match:
    print(match.group())  ## 'b@google'
# 优化
match = re.search(r'[\w.-]+@\w+',string)
if match:
    print(match.group())
