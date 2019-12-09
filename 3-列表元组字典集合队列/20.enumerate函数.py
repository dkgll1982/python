#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-10-20 09:33:26 
# @Last Modified by: guojun 
# @Last Modified time: 2019-10-20 09:33:26 
# @Software: vscode 

seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(list(enumerate(seasons)))
print(list(enumerate(seasons, start=11,)))                       # 下标从 11 开始

print('*'*40)

seasons = 'SpringSummerFallWinter'
print(list(enumerate(seasons)))

print('*'*40)

seasons = ('Spring', 'Summer', 'Fall', 'Winter')
print(list(enumerate(seasons)))

print('*'*40)

r = [('红色','red'), ('绿色','green'), ('蓝色', 'blue')]
print(list(enumerate(r)))

print('*'*40)

dict ={'绿色':'green','红色':'red','蓝色': 'blue'}

li = list(enumerate((key,dict[key]) for key in dict))
li.sort(reverse=True)
print(li)

print('*'*40)

print(sorted(list(enumerate((key,dict[key]) for key in dict)),reverse=True))

print('*'*40)

f = frozenset({1:2, 'a':2, 'c':3})  #无序的，不重复
print(list(enumerate(f)))

