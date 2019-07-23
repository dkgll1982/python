#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-07-22 15:36
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 转义字符
# @Software: PyCharm

s = 'Hello\nCharlie\nGood\nMorning'
print(s)

s2 = '商品名\t\t单价\t\t数量\t\t总价'
s3 = 'C语言小白变怪兽\t99\t\t2\t\t198'
s4= r'C语言小白变怪兽\t99\t\t2\t\t198'
s5= r"\\"+s3
print(s2)
print(s3)
print(s4);

print(s5);

height = 70.0
print("您的身高："+str(height))


import time
# 获取当前时间
a = time.gmtime()
b =  time.gmtime()
c=a;
print(a == b) # a和b两个时间相等，输出True
print(a is b) # a和b不是同一个对象，输出False

print (type(True))
print (False is True)
print (type(False) is type(True))
print (type(1) is type(True))
print (id(True))
print (id(type(False)))
print (id(type(True)))
print (id(False))
print (id(1))

#id(object)函数是返回对象object在其生命周期内位于内存中的地址，id函数的参数类型是一个对象
print(c is a)

a='1 2';
b='1 2';
print(id(a));
print(id(b))

i = 'a  b'
i1= 'a  b'
print(i is i1)