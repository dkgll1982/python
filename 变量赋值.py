#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-07-03 09:53
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 变量赋值
# @Software: PyCharm


def fn(self, name):
    print("Hello，"+name) 

#动态创建class

Hello = type('dfdfdgdfgdgdgd', (object,), dict(
    hello=fn, hell2=fn))  # 创建Hello class

c = Hello()
c.hell2("张三")

print(type(Hello))

def now(who):  # 创建一个方法
    print('anxious')

Mood = type('me', (object,), dict(now=now))
s = Mood();

print(type(Mood))
print(type(s))

class pmethod(object):
    say_hello = ""
    age = 10

    def __init__(self, name):
        self.name = name

    def func(self, value):
        return self.name + "----" + value

    def method(self, name):
        age = 10
        #say_hello = lambda self, value, saying=name: saying + ',' + value + '!'
        say_hello = pmethod(name).func
        return say_hello


clr = pmethod("zhangsan")
plr = clr.method("zhangsan")
print(plr('2'))