#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-07-28 11:22
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 类的方法
# @Software: PyCharm

class Bird:
    # classmethod修饰的方法是类方法
    @classmethod
    def fly (cls):
        print('类方法fly: ', cls)
    # staticmethod修饰的方法是静态方法
    @staticmethod
    def info (p):
        print('静态方法info: ', p)
# 调用类方法，Bird类会自动绑定到第一个参数
Bird.fly()  #①
# 调用静态方法，不会自动绑定，因此程序必须手动绑定第一个参数
Bird.info('crazyit')
# 创建Bird对象
b = Bird()
# 使用对象调用fly()类方法，其实依然还是使用类调用，
# 因此第一个参数依然被自动绑定到Bird类
b.fly()  #②
# 使用对象调用info()静态方法，其实依然还是使用类调用，
# 因此程序必须为第一个参数执行绑定
b.info('fkit')

print('------------------------------------------------------------')

class Test:
    #普通方法: 默认有个self参数，且只能被对象调用。
    def prt(self):
        print(self)
        print(self.__class__)

    @staticmethod
    #静态方法: 用 @staticmethod 装饰的不带 self 参数的方法叫做静态方法，类的静态方法可以没有参数，可以直接使用类名调用。
    def mystaticmethon():
        print("静态方法可以不传入参数！");

    @classmethod
    #默认有个 cls 参数，可以被类和对象调用，需要加上 @classmethod 装饰器。
    def myclsmethod(cls, *args, **kwargs):
        cls.name="张三"
        print("类方法！args：",args," kwargs:",kwargs)

t = Test()
t.prt()
#通过实例化对象引用静态方法
t.mystaticmethon()
#直接通过类名调用静态方法
Test.mystaticmethon()
#直接通过类型调用类方法
Test.myclsmethod(4,5,6,7,3,4,5,{"name":"张三","age":12})
t.myclsmethod()

