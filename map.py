#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-06-12 16:51
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : map.py
# @Software: PyCharm

from functools import reduce
def func(x):
    return x*x;

def func2(x,y):
    return x+y;

def aaa(x):
    return x>=2;

print(sorted(list(filter(aaa,[1,2,3,4,5,65,6,7,8,9,0])),reverse=True))

r = list(map(func,[1,2,3,4,5,6,7,8,9,10]));
r2 = reduce(func2,[1,2,3,4,5,6,7,8,9,10]);

print(r);
print(r2);

#带有参数的装饰器
import time

def deco(func):
    def wrapper(a,b):
        startTime = time.time()
        func(a,b)
        endTime = time.time()
        msecs = (endTime - startTime)*1000
        print("time is %d ms" %msecs)
    return wrapper


@deco
def func(a,b):
    print("hello，here is a func for add :")
    time.sleep(1)
    print("result is %d" %(a+b))

if __name__ == '__main__':
    f = func
    f(3,4)
    #func()

def a(fun):
    def f():
        print('call %s():' % fun.__name__);
        return fun();
    return f
@a
def b():
    print("之后的参数");

b();


def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator;
@log("老子")
def now():
    print('2015-3-25')

now()

def f(x):
    return x

f2 = lambda x:x;

print(f.__name__);
print(f2.__name__);
print(type(f2))

r = map(f, '1232132133234')
print(next(r));
print(next(r));
print(next(r));
print(next(r));
print(next(r));
print(next(r));
print(next(r));
print(next(r));

f=list(map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10]));
print(f);

def addF(x, y):
    return x + y
def fn(x, y):
    return x * 10 + y

n = reduce(fn,[1,2,3,4,5,6,7,8,9]);
print(n);

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))

print(type(str2int('242424242')));

def is_odd(n):
    return n % 2 == 1

l11=list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]));
print(l11);

print(list(x for x in [1, 2, 4, 5, 6, 9, 10, 15] if x%2==1))