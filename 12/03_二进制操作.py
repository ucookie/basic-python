#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open('file.txt', 'rb') as fobj:
    data = fobj.read()
    type(data)

    # 二进制转换成字符串
    data.decode('utf-8')

# 字符串编码成二进制
'hello python'.encode('utf-8')
bytes(data)


# python3 内存中使用的字符串全部是 unicode 码
# 但是网络传输的数据或者从磁盘读取的数据是把 unicode 码转换过的数据
# 通常情况下可能是 utf-8 格式的数据
# 所以如果从网络中读取或者磁盘中读取其实就是把 utf-8 格式的数据解码成 unicode 码数据
# 相反如果想把内存中 unicode 码数据存储到磁盘或者网络中需要对 unicode 码进行编码
# 通常可以采用 utf-8 的形式进行编码

# python3解释器中自带UTF-8编码器，python2中不自带，所以需要手动设置： #coding:utf-8
