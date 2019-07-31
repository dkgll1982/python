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
print('-'*40)
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

# yield方式求平方
# def func():
#     i = 1 ;
#     val = 0;
#     while True:
#         val = (yield val**2) if val is not None  else (yield i**2);
#         i+=1;    
#         print("%s的平方：%s"%(i,val));

# s = func();
# s.send(None);
# print(s.__next__())
# print(s.__next__())
# print(s.__next__())
# print(s.__next__())
# print(s.__next__())
# s.send(6);
# print(s.__next__())


def square_gen():
    i = 0
    out_val = None
    while True:
        # 使用yield语句生成值，使用out_val接收send()方法发送的参数值
        out_val = (yield out_val ** 2) if out_val is not None else (yield i ** 2)
        # 如果程序使用send()方法获取下一个值，out_val会获取send()方法的参数
        i += 1
        if out_val is not None : print("====%d" % out_val)
sg = square_gen()
# 第一次调用send()方法获取值，只能传入None作为参数
print(sg.send(None))  # 0
print(next(sg))  # 1
print(next(sg))  # 1
print(next(sg))  # 1
print(next(sg))  # 1
print('-'*40)
# 调用send()方法获取生成器的下一个值，参数9会被发送给生成器
print(sg.send(9))  # 81
# 再次调用next()函数获取生成器的下一个值
print(next(sg))  # 9