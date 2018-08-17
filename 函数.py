#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-08-08 14:17
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 函数
# @Software: PyCharm

def func(func,x):
    return  func(x);

t = func(abs,-122);

print(t)


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