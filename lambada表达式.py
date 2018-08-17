#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-06-29 16:59
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : lambada表达式
# @Software: PyCharm

def build(x, y):
    return lambda: x * x + y * y

print(type(build(12,33)));

f=lambda x,y,z:x+y+z
print(f(23,345,53));

f = 2 if 1==12 else 23;
print(f)
print(list(range(1,23)))

import time;
import datetime;

def Before(request, kargs):
    print('开始计时：%s'%time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))+':'+str(datetime.datetime.now().microsecond))

def After(request, kargs):
    print('结束计时：%s'%time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))+':'+str(datetime.datetime.now().microsecond))

def Filter(before_func, after_func):
    def outer(main_func):
        def wrapper(request, kargs):

            before_result = before_func(request, kargs)
            if (before_result != None):
                return before_result;

            main_result = main_func(request, kargs)
            if (main_result != None):
                return main_result;

            after_result = after_func(request, kargs)
            if (after_result != None):
                return after_result;

        return wrapper

    return outer


@Filter(Before, After)
def Index(request,kargs):
    time.sleep(0.13)
    print('index')

Index(1,2)


def f1(*args, **kwargs):
    print(args);
    print(kwargs);

f1(1,2,3,4,6,7,a=1,b=2,c=3)

import functools;
int2 = functools.partial(int, base=2)

print(int2('1010101'))
