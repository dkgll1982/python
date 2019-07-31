#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-07-28 12:02
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 装饰器复习
# @Software: PyCharm
import functools
import time

def avg(x,y):
    print((x+y)/2)
def sum1():
    sum = 1+ 2
    print (sum)

def timeit(func,*a):
    start = time.clock()
    func(*a)
    end =time.clock()
    print("time used:", end - start)

timeit(sum1)

timeit(avg,12,32);

print('------------------------------------------------------')

import time

def timeit2(func):
    def test():
        start = time.clock()
        func()
        end =time.clock()
        print("time used:", end - start)
    return test

@timeit2
def sum1():
    sum = 1+ 2
    print (sum)

#@timeit2，在定义上加上这一行与另外写sum1 = timeit2(sum1)完全等价
#sum1 = timeit2(sum1)
sum1()
print(sum1.__name__)

print('-'*40)---------------------------------------------------------')

def decorator(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        print("before doing something");
        ret = func (*args,**kwargs);
        print("something finished");
        return ret;
    return  wrapper;

@decorator
def sum1(a,b):
    sum = a+ b
    return sum
    print (sum)

print(sum1.__name__);
t = sum1(12,34)
print('t=',t)
print('-'*40)

import functools

def decorator(param):                 # 装饰器接受参数param
    def outer_wrapper(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if param == 'task1':      # 根据参数param判断当前修饰的是哪个函数
                func(*args, **kwargs)
            elif param == 'task2':
                func(*args, **kwargs)
            print(param,"is finished.")
        return wrapper
    return outer_wrapper

@decorator('task1')
def task1():
    print("doing task1 right now..")

@decorator('task2')
def task2():
    print("doing task2 right now..")

print(task1.__name__, task2.__name__)
task1()
task2()
'''输出： 
        task1   task2
        doing task1 right now..
        task1 is finished.
        doing task2 right now..
        task2 is finished.
'''