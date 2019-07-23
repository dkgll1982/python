#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-07-23 14:52
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 字符串函数
# @Software: PyCharm

s1 = "这是数字: "
p = 99.8
#字符串直接拼接数值，程序报错
print(s1 + p)
#使用str()将数值转换成字符串
print(s1 + str(p))
#使用repr()将数值转换成字符串
print(s1 + repr(p))