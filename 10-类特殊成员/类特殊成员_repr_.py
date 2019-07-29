#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-07-29 21:42:23 
# @Last Modified by: guojun 
# @Last Modified time: 2019-07-29 21:42:23 
# @Software: vscode 

class Item:
    def __init__ (self, name, price):
        self.name = name
        self.price = price
# 创建一个Item对象，将之赋给im变量
im = Item('鼠标', 29.8)
# 打印im所引用的Item对象
print(im)
print(im.__repr__)

class Apple:
    # 实现构造器
    def __init__(self, color, weight):
        self.color = color;
        self.weight = weight; 
    # 重写 Apple 类的 __repr__() 方法，就可以让系统在打印 Apple 对象时打印出该对象的“自我描述”信息。 
    # 大部分时候，重写 __repr__() 方法总是返回该对象的所有令人感兴趣的信息所组成的字符串。通常可返回如下格式的字符串：
    #类名[field1 = 值1, field2 =值2, ...]
    def __repr__(self):
        return "Apple[color=" + self.color +\
            ", weight=" + str(self.weight) + "]"
a = Apple("红色" , 5.68)
# 打印Apple对象
print(a)