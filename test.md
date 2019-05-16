1、需要每个讲师出50道选择题
2、每个选择题要有5到6个选项，而且都是不定项选择题
3、选择题内容不能是在搜索引擎上搜到的内容，应偏重实战、分析、迁移
4、错选、漏选、多选都不得分
5、出题内容的70%应该是讲课中讲过，或者根据讲课的内容可以推导出来的

难度设置
- 30 基础
- 15 中等
- 5 进阶

注：1.所有题目基于 3.x 版本 Python
    2.答案前的 * 号多少, 表示难易程度

python概念
=======================================================
=======================================================
01.
Python 程序文件的扩展名是?
a. pc
b. py
c. pyc
d. pcy
e. po

*答案：b

02.
在 ubuntu 系统中, 现在需要安装 Python 第三方库 Flask。下面哪些命令可以完成这个任务:

a. python3 install flask
b. python3 install flask==1.0.2
c. pip3 install flask
d. pip3 install flask==1.0.2
e. apt-get install flask
f. apt-get install flask==1.0.2

*答案: c,d

基本类型
=======================================================
=======================================================
01.
下面每一个选项都选自程序中的一行, 语句合法的是?
a. x = '52'+'0'
b. 5
c. length
d. ret = 13 / 0
e. count = 1 + 1.1

*答案：a, b, e

02.
表达式 int('134.5') 的结果为?
a. 134
b. 135
c. 134.5
d. 执行出错

*答案：a

03.
已知 x = 3, 那么下列语句能正常执行的是?
a. x = x + 3
b. x += 3
c. x = x + '3'
d. x += '3'
e. x = 'abc'

*答案: a,b,e

04.
下列定义变量的方式正确的是?
a. print = 'hello world'
b. _i = 12
c. 3th = 'Bob'
d. Ned_ = 39
e. len = 50

*答案：b,d

05.
Python 中正确的注释符号有?
a. #
b. //
c. --
d. """"""
e. ''''''

*答案：a,d,e

06.
执行语句 L = [x for x in range(3)]*2 后, 打印出 L 的结果为?
a. [0, 0, 1, 1, 2, 2]
b. [0, 0, 1, 1, 2, 2, 3, 3]
c. [0, 1, 2, 0, 1, 2]
d. [0, 1, 2, 3, 0, 1, 2, 3]
e. [2, 2, 2, 2, 2, 2]
f. [2, 2, 2, 2, 2, 2, 2, 2]

**答案：c

07.
list(map(str, [1, 2, 3])) 的类型为?
a. list
b. map
c. str
d. int
e. None

*答案: a

08.
下列定义字典的方式正确的是?
a. aDict = dict(name='Bob')
b. aDict = dict('name'='Bob')
c. aDict = {name='Bob'}
d. aDict = {'name'='Bob'}
e. aDict = {'name':'Bob'}

*答案：a,e

09.
下列格式化字符串的语句正确的是?
a. 'The version is %d' % '3.7'
b. 'The version is %s' % '3.7'
c. 'The version is %d' % 3.7
d. 'The version is %s' % 3.7
e. 'The version is %f' % 3.7

**答案：b,c,d,e

10.
已知一段代码：
t_number = tuple(1, 3, 5)
l_number = list(1, 2, 3)
____待填入____
sum_number = len(t_number) + t_number[0] + l_number[1]
在下划线处填入哪些语句, 可以让 sum_number 的值等于 7

a. t_number.append(7)
b. t_number.remove(1)
c. l_number.append(2)
d. l_number.remove(2)
e. t_number[0] = 2
f. l_number[1] = 3

***答案：d,f

11.
下列定义元组的语句正确的是:

a. T = list(3)
b. T = list(3,)
c. T = tuple(3)
d. T = tuple(3,)
e. T = [3]
f. T = (3)

*答案: c,d

12.
使用 dir(A) 查看变量 A 的方法, 其中有一个方法名为 sort(), 则 A 的类型可能是:

a. list
b. tuple
c. dict
d. str

*答案: a

13.
使用 dir(A) 查看变量 A 的方法, 其中有一个方法名为 split(), 则 A 的类型可能是:

a. list
b. tuple
c. dict
d. str

*答案:e

14.
使用 dir(A) 查看变量 A 的方法, 其中有一个方法名为 index(), 则 A 的类型可能是:

a. list
b. tuple
c. dict
d. str

**答案: a,b,d

15.
已知存在字典 student = {'number':'001'}, 则下列语句正确的是?
a. print(student.number)
b. print(student(number))
c. print(student[number])
d. print(student['number'])
e. print(student.get('name', ''))

**答案：d,e

16.
有如下代码:
D = {'num': 1, 'num': 2}
print(D)
则打印出的结果为:

a. {'num': 1, 'num': 2}
b. {'num': 1}
c. {'num': 2}
d. 语法错误, 无法打印

**答案：c

判断, 循环
=======================================================
=======================================================
1.
有如下代码:
if x ____ 90:
    print('优秀')
elif x ____ 60:
    print('良好')
else:
    print('不及格')

已知输入的 x 为 0 ~ 100 之间的分数, 则在空格处填入符号让结果合理的是:

a. >==
b. >=
c. >
d. <==
e. <=
f. <

**答案：b

2.
下列逻辑计算中, 结果为真的是:

a. not True
b. not False
c. True and True
d. True and False
e. True or True
f. True or False

*答案: b,c,e,f

3.
已知如下代码：
L1 = [i for i in range(3)]
L2 = L1[::-1]

则 L2 的值为：

a. [0, 1, 2, 3]
b. [0, 1, 2]
c. [3, 2, 1, 0]
d. [2, 1, 0]

**答案：d

函数, 类
=======================================================
=======================================================

文件操作
=======================================================
=======================================================

多任务
=======================================================
=======================================================






31.基本类型
32.序列字典
33.进程
34.条件循环
35.线程
36.函数
37.模块类
38.文件操作
39.文本处理
40.深浅拷贝
41.协程
42.正则
43.爬虫
44.多任务
45.GIL

