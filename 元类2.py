#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-07-03 11:20
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 元类2
# @Software: PyCharm

# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

class MyList(list, metaclass=ListMetaclass):
    pass

c = MyList();
c.add("我是张三");
