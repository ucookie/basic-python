#!/usr/bin/env python3
# -*- coding: utf-8 -*-


fobj = open('file.txt', 'rb')
data = fobj.read()
type(data)

# 二进制转换成字符串
data.decode('utf-8')

# 字符串编码成二进制
''.encode('utf-8')
bytes(data_str)

一.字符集：


ascii
ISO-8859-1 通常叫 做Latin-1，向下兼容ASCII，此字符集支持部分于欧洲使用的语言
GB2312/GBK 这就是汉字的国标码，专门用来表示汉字，是双字节编码，而英文字母和iso8859-1一致（兼容iso8859-1编码）。其中gbk编码能够用来同时表示繁体字和简体字，而gb2312只能表示简体字，gbk是兼容gb2312编码的。
unicode 万国码
二.Unicode 与 UTF 之间的简单关系：


UTF Unicode Transformation Format，通用传输格式
UTF-8 8-bit Unicode Transformation Format
UTF-8 是一种 Unicode 的编码方式，主要作用对 Unicode 码的数据进行转换，转换后方便存储和网络传输

三.Python3 中的字节串与字符串 之间的区别:


节串（二进制数据，bytes）
字符串（Unicode码数据，2个字节作为一个字）
四.Python3 中编码:


二进制 -> 转换 -> 字符串 需要解码 decode
字符串 -> 转换 -> 二进制 需要编码 encode
python3 内存中使用的字符串全部是 unicode 码，但是网络传输的数据或者从磁盘读取的数据是把 unicode 码转换过的数据，通常情况下可能是 utf-8 格式的数据，所以如果从网络中读取或者磁盘中读取其实就是把 utf-8 格式的数据解码成 unicode 码数据，相反如果想把内存中 unicode 码数据存储到磁盘或者网络中需要对 unicode 码进行编码，通常可以采用 utf-8 的形式进行编码

python3解释器中自带UTF-8编码器，python2中不自带，所以需要手动设置： #coding:utf-8
