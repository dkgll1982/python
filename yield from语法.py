#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-08-17 17:04
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : yield from语法
# @Software: PyCharm

def g1(x):
    yield range(x) 

def g2(x):
    yield from range(x) 

it1 = g1(5)
it2 = g2(5)

print(type(it1))
print(type(it2))

print(type([x for x in it1]))
# out [range(0, 5)]
print(type([x for x in it2]))
# out [0, 1, 2, 3, 4]