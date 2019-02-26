#!/usr/bin/env python3
# -*- coding: utf-8 -*-

str_1 = 'Hello python'
# 判断是否为空格
str_1.isspace()
str_1.isupper()

# 查找p字符位置
str_1.find('p')

# 替换ptyhon为world
str_1.replace('python', 'World')

# 转换大小写
str_1.swapcase()

# 去除空白
str_1 = str_1 + ' '
str_1.strip()

# 拆分
str_1.split(' ')

# 连接
str_1.join('你好世界')