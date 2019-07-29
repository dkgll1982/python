#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-07-02 16:44
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 元类
# @Software: PyCharm

# 创建一个Hello类，拥有属性say_hello ----二的起源
class Hello():
    def say_hello(self, name='world'):
        print('Hello, %s.' % name)

# 从Hello类创建一个实例hello ----二生三
hello = Hello()
# 使用hello调用方法say_hello ----三生万物
hello.say_hello()


def fn(self, name='world'):  # 假如我们有一个函数叫fn
    print('Hello, %s.' % name)
def fn2(self, name='world'):  # 假如我们有一个函数叫fn
    print('Hello2, %s.' % name)
Hello2 = type('Hello', (object,), dict(say_hello=fn,say_hello2=fn2,name=1,age=3,))  # 通过type创建Hello class ---- 神秘的“道”，可以点化一切，这次我们直接从“道”生出了“二”

hello2 = Hello2()
# 使用hello调用方法say_hello ----三生万物
hello2.say_hello2()

print(hello2.age)

def func(self,name,value):
    print(name + ',' + value + '!')

# 道生一：传入type
class SayMetaClass(type):
    # 传入三大永恒命题：类名称、父类、属性
    def __new__(cls, name, bases, attrs):
        # 创造“天赋”
        attrs['say_' + name] = lambda self, value, saying=name:  saying + ',' + value + '!'
        #attrs['say_' + name] = func;
        # 传承三大永恒命题：类名称、父类、属性
        return type.__new__(cls, name, bases, attrs)

# 一生二：创建类
class Hello(object, metaclass=SayMetaClass):
    pass
class Sayolala(object, metaclass=SayMetaClass):
    pass

# 二生三：创建实列
hello = Hello()

# 三生万物：调用实例方法
print(type(hello.say_Hello))
print(hello.say_Hello("world"))