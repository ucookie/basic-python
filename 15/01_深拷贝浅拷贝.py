#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 演示浅拷贝
a = [1, 2, 138]

# python 中的等号基本是引用, 近似的理解为拷贝
x = a

print(a)
print(x)

# id表示对象的地址
id(a)
id(x)

# 修改
a[0] = 99
print(x)

# 深拷贝
import copy
x = copy.deepcopy(a)
print(a)
print(x)


# 浅拷贝
a = [1, 2, 138]
b = [100, 1000]
c = [a, b]

d = c
id(c)
id(d)

x = copy.copy(c)
id(x)

id(a)
id(x[0])
