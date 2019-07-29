#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-06-13 10:54
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : reduce.PY
# @Software: PyCharm

def fun(x,y):
    return  x+y

def fun2(x):
    return  x+x
from functools import  reduce;

import math;

rn =reduce(fun,[1,2,3,4,5,6,7,8,9,10]);
rn1 =list(map(fun2,[1,2,3,4,5,6,7,8,9,10]));
rn2 =list(map(str,[1,2,3,4,5,6,7,8,9,10]));
rn3 =list(map(abs,[-1,2,3,4,5,6,7,8,9,10]));
rn4 =list(map(round,list(map(math.sqrt,[1,2,3,4,5,6,7,8,9,10]))));

rn5=list(map(fun,[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]));

list1 = [11,22,33]
r2 = map(None,list1);


list1 = [11,22,33]
map(None,list1)
list1 = [11,22,33]
list2 = [44,55,66]
list3 = [77,88,99]


def add(x,y,z):
    return x+y+z

list1 = [1,2,3]
list2 = [1,2,3,4]
list3 = [1,2,3,4,5]
res = reduce(fun,list(map(add, list1, list2, list3)));
res2 = reduce(fun,map(add, list1, list2, list3));


print(res == res2)

def oushu(x):
    return x%2==1;

#过滤去重
li = list(filter(oushu,[1,2,3,4,5,6,7,0,-21,8,9,12,232,4,234,24,2,42,34,2,4,354,34,5,4,64,6,4,64,6,45,656,7,5,7,567,65]));
new_li=list(set(li))
new_li.sort(key=li.index,reverse=True)
print(li);
print(new_li);

print(sorted(li,reverse=True,key=li.index))
print(sorted(li,key=li.index))
print(sorted(li,key=abs))
print(sorted(li,key=abs,reverse=True))

print(sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower,reverse=True))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return t[0];
def by_score(t):
    return -t[1];

print(sorted(L,key=by_name))
print(sorted(L,key=by_score))

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f1 = lazy_sum(1, 3, 5, 7, 9)
print(f1())
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
print(count())
f1, f2, f3 = count()
print(f1());
print(f2());
print(f3());

import time;
def deco(arg = True):
    if arg:
        def _deco(func):
            def wrapper(a,b):
                startTime=time.time();
                func(a,b);
                endTime=time.time();
                msecs = (endTime-startTime)*1000
                print ("执行func耗时：%f ms" %msecs);
            return wrapper;
    else:
        def _deco(func):
            return  func;
    return  _deco;

@deco(False)
def myfunc(a,b):
    print("start myfunc!");
    time.sleep(1.234);
    print("result is %d" %(a+b));
    print("stop myfunc!");

myfunc(1,2);