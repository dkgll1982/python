#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-07-02 17:03
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : class执行顺序
# @Software: PyCharm

class Hello(object):
    def __new__(cls, *args, **kwargs):
        print("执行__new__方法");
        return object.__new__(cls, *args, **kwargs)
    def __init__(self):
        print("执行__init__方法");
    def method1(self,name):
        print("执行普通方法");

hello = Hello();

hello.method1("ZHANGSAN");