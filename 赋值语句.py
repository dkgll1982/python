#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-06-20 10:01
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 赋值语句
# @Software: PyCharm

string = 'gabcd'
a,b,c=string[0],string[1],string[2]
a=list(string[:2])+[string[2:]]+['3423']
print("a=%s"%a)


*b,='abcd'

print( *b)