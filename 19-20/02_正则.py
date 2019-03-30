import re
# 待匹配文本
h1 = '<H1>Chapter 3.2.1 - 介绍正则表达式</H1>'
# 将正则字符串编译成正则表达式对象，方便在后面的匹配中复用
pat = re.compile('<H1>(.*?)</H1>', re.S)
# re.search 扫描整个字符串并返回第一个成功的匹配
result = re.search(pat, h1)
# 匹配的整个表达式的字符串，group() 可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组。
print(result.group(0))
# 匹配的第一个括号内的字符串，group() 可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组。
print(result.group(1))





