#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-07-09 17:25
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 协程
# @Software: PyCharm
#! -*- coding: utf-8 -*-
import inspect

def simple_coro2(a):
    print('-> coroutine started: a =', a)
    b = yield a
    print('-> Received: b =', b)
    c = yield a + b
    print('-> Received: c =', c)
    d = yield a + c
    print('-> Received: d =', d)

my_coro2 = simple_coro2(14)
print(inspect.getgeneratorstate(my_coro2))
# 这里inspect.getgeneratorstate(my_coro2) 得到结果为 GEN_CREATED （协程未启动）

next(my_coro2)
# 向前执行到第一个yield 处 打印 “-> coroutine started: a = 14”
# 并且产生值 14 （yield a 执行 等待为b赋值）
print(inspect.getgeneratorstate(my_coro2))
# 这里inspect.getgeneratorstate(my_coro2) 得到结果为 GEN_SUSPENDED （协程处于暂停状态）

print('-------'+str(my_coro2.send(28)))
# 向前执行到第二个yield 处 打印 “-> Received: b = 28”
# 并且产生值 a + b = 42（yield a + b 执行 得到结果42 等待为c赋值）
print(inspect.getgeneratorstate(my_coro2))
# 这里inspect.getgeneratorstate(my_coro2) 得到结果为 GEN_SUSPENDED （协程处于暂停状态）

print('-------'+str(my_coro2.send(99)))
# 把数字99发送给暂停协程，计算yield 表达式，得到99，然后把那个数赋值给c 打印 “-> Received: c = 99”
# 协程终止，抛出StopIteration