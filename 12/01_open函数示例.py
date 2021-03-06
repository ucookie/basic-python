#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 简单的读取文件
fobj = open('file.txt', 'r')
data = fobj.read()
print(data)

# 重复读取无效, 需要设置文件指针
data = fobj.readlines()
print(data)
fobj.close

# 文件不存在
fobj = open('no-file.txt', 'r')
data = fobj.read()
print(data)

# 写文件
fobj = open('new.txt', 'w')
fobj.write('hello python')

# 注意换行
fobj.write('hello python\n')
fobj.close

# 重复写会覆盖, 使用a追加
fobj = open('new.txt', 'a')
fobj.write('Life is short, i use Python')
