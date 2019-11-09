#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-11-08 13:50:40 
# @Last Modified by: guojun 
# @Last Modified time: 2019-11-08 13:50:40 
# @Software: vscode 

# enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，
# 同时列出数据和数据下标，一般用在 for 循环当中。

seasons = ['Spring', 'Summer', 'Fall', 'Winter']
e = enumerate(seasons)
print(e)
print(e.__next__())
print(e.__next__())
print(e.__next__())
print(e.__next__())

for i, element in enumerate(seasons):
    print(i, element)