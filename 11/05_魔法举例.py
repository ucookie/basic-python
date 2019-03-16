#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 这个方法我们一般很少定义，不过我们在一些开源框架中偶尔会遇到定义这个方法的类。实际上，这才是“真正的构造方法”，它会在对象实例化时第一个被调用，然后再调用__init__，它们的区别主要如下：

# __new__的第一个参数是cls，而__init__的第一个参数是self
# __new__返回值是一个实例，而__init__没有任何返回值，只做初始化操作
# __new__由于是返回一个实例对象，所以它可以给所有实例进行统一的初始化操作
# 由于__new__优先于__init__调用，且返回一个实例，所以我们可以利用这种特性，每次返回同一个实例来实现一个单例类：
class Singleton(object):
    """单例"""
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance
class MySingleton(Singleton):
    pass
a = MySingleton()
b = MySingleton()
print(id(a))
print(id(b))


# __str__/__repr__
# 这两个魔法方法一般会放到一起进行讲解，它们的主要差别为：
# __str__强调可读性，而__repr__强调准确性/标准性
# __str__的目标人群是用户，而__repr__的目标人群是机器，它的结果是可以被执行的
# %s调用__str__方法，而%r调用__repr__方法


class Person(object):
    def __setattr__(self, key, value):
        """属性赋值"""
        if key not in ('name', 'age'):
            return
        if key == 'age' and value < 0:
            raise ValueError()
        super(Person, self).__setattr__(key, value)

    def __getattr__(self, key):
        """访问某个不存在的属性"""
        return 'unknown'

    def __delattr__(self, key):
        """删除某个属性"""
        if key == 'name':
            raise AttributeError()
        super(Person, self).__delattr__(key)

    def __getattribute__(self, key):
        """所有属性/方法调用都经过这里"""
        if key == 'money':
            return 100
        if key == 'hello':
            return self.say
        return super(Person, self).__getattribute__(key)

    def say(self):
        return 'hello'

p1 = Person()
p1.name = '小明'	# 调用__setattr__
p1.age = 20				# 调用__setattr__
print(p1.name)	# zhangsan
print(p1.age)	# 20
setattr(p1, 'name', 'lisi')	# 调用__setattr__
setattr(p1, 'age', 30)		# 调用__setattr__
print(p1.name)	# lisi
print(p1.age)	# 30
p1.gender = 'male'	# __setattr__中忽略对gender赋值
print(p1.gender)	# gender不存在,调用__getattr__返回：unknown
print(p1.money)	# money不存在,在__getattribute__中返回100
print(p1.say())	# hello
print(p1.hello()) # hello,调用__getattribute__，间接调用say方法
del p1.name		# __delattr__中引发AttributeError
p2 = Person()
p2.age = -1		# __setattr__中引发ValueError