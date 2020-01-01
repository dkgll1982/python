#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-07-09 17:25
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 协程
# @Software: PyCharm
#! -*- coding: utf-8 -*-

from functools import wraps

def coroutinue(func):
    '''
    装饰器： 向前执行到第一个`yield`表达式，预激`func`
    :param func: func name
    :return: primer
    '''

    @wraps(func)
    def primer(*args, **kwargs):
        # 把装饰器生成器函数替换成这里的primer函数；调用primer函数时，返回预激后的生成器。
        gen = func(*args, **kwargs)
        # 调用被被装饰函数，获取生成器对象
        next(gen)   # 预激生成器
        return gen  # 返回生成器
    return primer


# 使用方法如下

@coroutinue
def simple_coro(a):
    a = yield

simple_coro(12)  # 已经预激