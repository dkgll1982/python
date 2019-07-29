#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-08-08 14:17
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 函数
# @Software: PyCharm

def func(func,x):
    '''
    通用函数调用
    :param func:传递函数方法名
    :param x:参数
    :return:返回计算结果
    '''
    return  func(x);

t = func(abs,-122);

print(t)

help(func)

def myfunc(obj):
    #obj+=obj;
    obj=obj+obj;

a=[122,22,3,4]

print(a);
s = myfunc(a);
print(a)
print('-----------------')
#a+=a;

b =a;
a.append(1)
#b.__iadd__(a)
b.__add__(a)
print(a)

#斐波那契数列
def fab(n):
    L = [];
    a,b = 0,1;
    while b<n:
        L.append(b);
        a,b = b,a+b
    return L;

print(fab(100))

# 阶乘
def fac(a,n):
    while n>1:
        return a*fac(a,n-1)
    return a;

print(fac(1.1,365));