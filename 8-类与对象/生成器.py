#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-08-08 15:13
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 生成器
# @Software: PyCharm
from functools import reduce

def f(x):
    return x * x

def add(x,y):
    return x + y

def fil(x):
    return x%3==0;

r = map(f, [x for x in range(1,100)])

m = reduce(lambda x,y:x+y,map(f, [x for x in range(1,100)]),1000000000000000000000);

#过滤数据
n = list(filter(fil,map(f, [x for x in range(1,100)])))

print(n)

import random
#将序列中的元素顺序打乱
n2 = list(filter(fil,map(f, [x for x in range(1,100)])))
random.shuffle(n2)
print(n2)

print(m)

print(r.__next__())
print(r.__next__())
print(r.__next__())
print(r.__next__())
print(len(list(r)));

def gen_generator(n):
    for i in range(1,n):
        yield i

def gen_value():
    return 1

if __name__ == '__main__':
    ret = gen_generator(12)
    print(ret.__next__(), type(ret))  # <generator object gen_generator at 0x02645648> <type 'generator'>
    print(ret.__next__())
    ret = gen_value()
    print(ret, type(ret))  # 1 <type 'int'>


L = [x * x for x in range(10)]

g = (x * x for x in range(122))

print(g.__next__(),g.__next__(),g.__next__(),g.__next__(),g.__next__(),g.__next__(),g.__next__(),g.__next__(),g.__next__(),g.__next__(),g.__next__())

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

g = fib(20);

print(g.__next__(),g.__next__(),g.__next__(),g.__next__(),g.__next__(),g.__next__(),g.__next__(),g.__next__(),g.__next__(),g.__next__(),g.__next__())

def odd(n):
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)

print(type(odd(10)))
