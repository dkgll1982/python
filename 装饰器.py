#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-08-13 10:30
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 装饰器
# @Software: PyCharm

from functools import wraps




def sum_add(*args1):  # 我们要给我们的装饰器decorator，带上参数
    def decorator(func):
        @wraps(func)  # 加上这句，原函数func被decorator作用后，函数性质不变
        def my_sum(*args2):  # 注意，参数要和原函数保持一致，真正实行扩展功能的是外层的装饰器
            my_s = 0
            for n in args1:
                my_s = my_s + n  # 这个是我们新加的求和结果
            return func(*args2) + my_s  # 这个，我们在原求和函数的结果上再加上s，并返回这个值
        return my_sum  # 返回my_sum函数，该函数扩展原函数的功能
    return decorator  # 返回我们的装饰器

@sum_add(10, 20)  # 启用装饰器 对sum函数进行功能扩展
def sum(*args):
    s = 0
    for n in args:
        s = s + n
    return s

print(sum(1, 2, 3, 4, 5))

from functools import wraps
def log(text):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print('2015-3-25')

now()
print(now.__name__)