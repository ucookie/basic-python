
注：1.所有题目基于 3.x 版本 Python
    2.答案前的 * 号多少, 表示难易程度, 如: **答案: b, 表示中等难度

共 39 题

概念
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

03.
下列对程序描述不正确的是？

a. 程序是由一系列函数组成的
b. 程序是由一系列代码组成的
c. 可以利用函数对程序进行模块化设计
d. 通过封装可以实现代码复用

*答案：a

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

17.
已知有如下代码:
Kvps = {'1': 1, '2': 2}
theCopy = kvps
kvps['1'] = 5
sum = kvps['1'] + theCopy['1']
print(sum)

a. 1
b. 2
c. 7
d. 10

**答案：d

18.
下列说法正确的是?

a.
a = [1,2,3]
b = [1,2,3]
a与b指向同一个内存地址。

b.
i1 = 356
I2 = 356
i1 与 i2是同一个内存地址。

c.
s1 ='laonanhai'
s2 ='laonanhai'
s1 与 s2 是同一个内存地址。

d. tu = (1) tu是元组类型

***答案：c


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

4.
哪个选项给出的保留字不直接用于表示分支结构？

a. if
b. elif
c. else
d. in

*答案：d

5.
已知 x=43, ch='A', y = 1，则表达式 ( x>=y and ch <'b' and y) 的值是?

a. 0
b. 1
c. True
d. 执行错误

***答案：b

6.
下列语句正确的是?

a. min_num = x if x < y else y

b. max_num = x > y ? x : y

c. if(x > y) print(x)

d. while True:pass

**答案：a,d

7.
下列代码执行的次数为?

k=1000
while k>1:
    print(k)
    k=k/2

a. 9
b. 10
c. 11
d. 100

**答案：b

8.
以下叙述正确的是：
a. continue语句的作用是结束整个循环的执行
b. 只能在循环体内使用break语句
c. 在循环体内使用break语句或continue语句的作用相同
d. 从多层循环嵌套中退出时，只能使用goto语句

*选择：b

9.
10、下面的语句哪个会无限循环下去：

a.
for a in range(10):
    time.sleep(10)
b.
while 1<10:
    time.sleep(10)
c.
while True:
    break

d.
a = [3,-1,',']
for i in a[:]:
    if not a: break

***选择:b

10.
下面的代码, 哪些是输出 1,2,3 三个数字?

a.
for i in range(3):
   print(i)
   print(i+1)

b.
aList = [0,1,2]
for i in aList:
   print(i+1)

c.
i = 1
while i < 3:
   print(i)
   i+=1

d.
for i in range(3):
   print(i+1)

***选择：b,d


函数, 类
=======================================================
=======================================================
1.
有如下代码：
def get():
    number = '911'
    return
ret = int(get())
则 ret 的值为?

a. '911'
b. 911
c. None
d. 执行出错

**答案：d

2.
执行下面代码, 输出的信息为?
a = 1
def func1():
    a += 1
    print(a)
func1()

a. 1
b. 2
c. 无输出
d. 执行出错

*答案：a

3.
执行下面代码, 输出的信息为?

def wrapper():
    a = 1
    def inner():
        a += 1
        print(a)
        inner()
wrapper()

a. 1
b. 2
c. 无输出
d. 执行出错

4.
已知有下列代码:
import copy
score = [90, 90, 90]
student = {'name':'小明', 'score': score}
s1 = copy.copy(student)
s2 = copy.deepcopy(student)
s3 = student
score[0] = 100
print([x['score'][0] for x in [s1, s2, s3]])

则解释器打印的结果为?

a. [100, 100, 100]
b. [90, 100, 100]
c. [100, 90, 100]
d. [100, 100 90]
e. [90, 90, 100]
f. [90, 90, 90]

***答案：c

5.
下面是定义函数的语句, 正确的是?

a. def func(*args, **kwargs)
b. def func(name, *args, **kwargs)
c. def func(*args, name, **kwargs)
d. def func(*args, **kwargs, name)
e. def func(name, num='001')
f. def func(num='001', name)

***答案：a,b,e

6.
func() 函数使用装饰器打印日志, 请选择合适的装饰器实现, 使其能完成功能

@func_log
def func(name):
    print('do something')

a.
def func_log():
    def wrapper(*args, **kwargs):
        print('do log')
        return func()
    return wrapper

b.
def func_log():
    def wrapper(*args, **kwargs):
        print('do log')
        return func()
    return wrapper

c.
def func_log(func):
    def wrapper(*args, **kwargs):
        print('do log')
        return func(*args, **kwargs)
    return wrapper

d.
def func_log(func):
    def wrapper(*args, **kwargs):
        print('do log')
        return func(*args, **kwargs)
    return wrapper(*args, **kwargs)

***答案: c

文件操作
=======================================================
=======================================================
1.
下列语句是某脚本的一部分, 该脚本目录下有 file.txt 文件, 那么下列代码中能够读取到 file.txt 文件中数据的是?

a.
fobj = open('file.txt')
fobj.read()

b.
fobj = open('file.txt', 'w')
fobj.read()

c.
with open('file.txt') as fobj:
    fobj.read()

d.
with open('file.txt', 'w') as fobj:
    fobj.read()

**答案：b,d

2.
已知有文本文件内容如下,

小明,"2019,01",18,True,1300000001
小红,"2019,02",18,False,1300000002
小蓝,"2019,01",19,True,1300000002

则下列语句中, 能够格式化读取文件的是：

a.
with open('file', 'r') as fboj:
    obj = csv.reader(fboj)

b.
with open('file', 'r') as fboj:
    obj = json.loads(fboj.read())

c.
config = configparser.ConfigParser()
with open('file', 'r') as fboj:
    config.readfp(fboj)

d.
tree = ET.ElementTree(file='file')
root = tree.getroot()
