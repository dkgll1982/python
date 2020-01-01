#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-07-09 17:25
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 协程
# @Software: PyCharm
#! -*- coding: utf-8 -*-

from collections import namedtuple

Result = namedtuple('Result', 'count average') 

def averager(s):
    total = 0.0
    count = 0
    term = s
    average = None
    while True:
        term = yield s + term
        print('---'+str(term))
        if term is None:
            break  # 为了返回值，协程必须正常终止；这里是退出条件
        total += term
        count += 1
        average = total/count
    # 返回一个namedtuple，包含count和average两个字段。在python3.3前，如果生成器返回值，会报错
    # return Result(count, average)


# 如果我们想获取协程的返回值，可以这么操作：
coro_avg = averager(2)
print(next(coro_avg))
print(coro_avg.send(20))  # 并没有返回值
print(coro_avg.send(30))
print(coro_avg.send(40))
# coro_avg.send(None) # 发送None终止循环，导致协程结束。生成器对象会抛出StopIteration异常。异常对象的value属性保存着返回值。
try:
    coro_avg.send(None)
except StopIteration as exc:
    result = exc.value

# print(result)
