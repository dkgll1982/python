#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-07-28 14:22
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 类命名空间
# @Software: PyCharm

global_fn = lambda p: print('执行lambda表达式，p参数: ', p)
class Category:
    def __init__(self, *args,**kwargs):
        self.args = args;
        self.kwargs = kwargs;
    cate_fn = lambda self: print('执行lambda表达式，args参数: ', self.args,"，kwargs参数：", self.kwargs)
# 调用全局范围内的global_fn，为参数p传入参数值
global_fn('fkit')  # ①
c = Category('0','1','2',姓名="张三",年龄="20",性别="女")
# 调用类命名空间内的cate_fn，Python自动绑定第一个参数, 内部lambada表达式的p相当于self
c.cate_fn()  # ②