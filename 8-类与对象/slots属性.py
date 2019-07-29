#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-07-28 22:12
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : slots属性
# @Software: PyCharm

def wbfun(name):
    print("name:",name);

class Dog:
    __slots__ = ('walk', 'age', 'name',"wbfun")
    def __init__(self, name):
        self.name = name
    def test(self):
        print('预先定义的test方法')
d = Dog('Snoopy')
from types import MethodType
# 只允许动态为实例添加walk、age、name这3个属性或方法
d.walk = MethodType(lambda self: print('%s正在慢慢地走' % self.name), d)
d.age = 5
d.walk();
d.wbfun = wbfun
d.wbfun("李四")
#_在类外添加属性，对  类.属性名  格式限制不起作用（对类添加的属性不起作用）
Dog.ah = lambda self:print("name =",self.name)

d.ah()
li = Dog("比尔盖茨")
print(d.__dir__())

#d.foo = 30              # AttributeError

#!/usr/bin/python
# -*-coding:utf-8-*-

from types import MethodType
"""
文件名 class2.py
MethodType 测试
"""
# 首先看第一种方式
#创建一个方法
def set_age(self, arg):
    self.age = arg
#创建一个类
class Student(object):
    pass

#导入MethodType
from types import MethodType
class Student(object):
    pass
#组装方法
def set_name(self, name):
    self.name = name
    print(self.name)

s1 = Student()
#依次传入方法名, 实例, 类名 完成实例绑定方法
s1.set_name = MethodType(set_name, s1);


s1.set_name("张三")

