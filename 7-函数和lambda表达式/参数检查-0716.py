#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-07-16 15:24
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 参数检查-0716
# @Software: PyCharm

def func(name,age,*k,**kw):
    print(k);
    print(kw);
    if 'city' in kw:
        print("you do it:%s" %kw["city"]);
    elif 'job' in kw:
        print("you have it:%s"%kw["job"]);
    else:
        print("have nothing");


def func2(name,age,*k,city,job,sex='男',**kw):
    print(k[0]);
    print(city);
    print(job)
    print(sex)
    print(kw["ciw"])


func2("zhang",12,35,3567,67686,city="sdf",job='234',ci="jsdf",ci2="jsdf",ciw="jsdf",c6i="jsdf")


def product(*k):
    result = 1
    for x in k:
        result=x*result;
    return result;


def fac(k):
    if k == 1:
        return 1;
    return k * fac(k - 1);

def e(f,n):
    if n==1:
        return f;
    return  f*e(f,n-1);
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))

print("fac(10)=",fac(10))

#切片
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
s="我来自中国"
#for x in range(len(L)+1):
#    print(L[:-x])

#for x in range(len(s)+1):
#    print(s[:x:2])

#去空格
def trim(str):
    string = s
    for x in range(len(str)):
        if str[x]==' ' :
            string = str[(x+1):]
        else:
            break;
    print("str:"+string)
    for x in range(len(str)):
        if str[x]==' ':
            return str[:x];
    return str


s='123456789';
print(s[1]);
print(s[1:]);
print(s[:1]);
print(s[1:5]);
print(s[-1]);