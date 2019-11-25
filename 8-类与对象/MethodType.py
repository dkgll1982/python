#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-08-15 14:27
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : MethodType
# @Software: PyCharm

#!/usr/bin/python
# -*-coding:utf-8-*-

from types import MethodType

class Student(object):
    __slots__ = ('set_ages', 'age') # 用tuple定义允许绑定的属性名称

def set_name(self,name):
    self.name = name

def set_age(self,age):
    self.age = age

def set_sc(self,x,y):
    self.x = x
    self.y = y

x1 = Student()   #类的实例化
x2 = Student()

x1.set_ages = MethodType(set_age,x1)   #实例绑定一个方法
x2.set_ages = MethodType(set_age,x2)

Student.setsc = MethodType(set_sc,Student)  #另一种绑定

Student.set_name = MethodType(set_name,Student)  #给此类绑定一个方法

x1.set_ages(12)    #初始化
x2.set_ages(13)

x1.setsc("xmc","xu")

Student.set_name("hhh")

print(x1.age)   #12
print(x2.age)    #13
print(x1.x,x1.y)    #xmc xu
print(x1.name)     #hhh
print(x2.name)     #hhh