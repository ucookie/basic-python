#!/usr/bin/env python3
# -*- coding: utf-8 -*-



# 正则表达式（英语：Regular Expression，在代码中常简写为regex、regexp或RE）
# 又称正规表示式、正规表示法、正规表达式、规则表达式、常规表示法，是计算机科学的一个概念
# 正则表达式使用单个字符串来描述、匹配一系列匹配某个句法规则的字符串
# 在很多文本编辑器里，正则表达式通常被用来检索、替换那些匹配某个模式的文本



import re


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
   print("matchObj.group(2) : ", matchObj.group(3))
else:
   print("No match!!")

# search 匹配
# re.search 扫描整个字符串并返回第一个成功的匹配
import re
print(re.search('hello', 'hello python').span())  # 在起始位置匹配
print(re.search('python', 'hello python').span())         # 不在起始位置匹配


# 提取email address
string = 'purple xiaoming-cn@gmail.com monkey dishwasher'
match = re.search(r'\w+@\w+', string)
if match:
    print(match.group())  ## 'b@google'

match = re.search(r'[\w.-]+@\w+',string)
if match:
    print(match.group())

