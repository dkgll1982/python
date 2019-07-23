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
##print(s1 + p)
#使用str()将数值转换成字符串
print(s1 + str(p))
#使用repr()将数值转换成字符串
print(s1 + repr(p))

s = 'crazyit.org is very good'
# 获取s中从索引3处到索引5处（不包含）的子串
print(s[3: 5]) # 输出 zy
# 获取s中从索引3处到倒数第5个字符的子串
print(s[3: -5]) # 输出 zyit.org is very
# 获取s中从倒数第6个字符到倒数第3个字符的子串
print(s[::-1]) # 输出 doog yrev si gro.tiyza
print("".join(reversed(s)))
#每隔 1 个，取一个字符
print(s[::2]) # 输出 caytogi eygo

str = "C语言中文网 >>> c.biancheng.net mycro soft Amercia"
#sep：用于指定分隔符，可以包含多个字符。此参数默认为 None，表示所有空字符，包括空格、换行符“\n”、制表符“\t”等。
list =s.split();

print(list)
list4 = str.split(' ')
list5 = str.split(' ',4)
print(list4)
print(list5)