#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-08-08 10:05
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 元组
# @Software: PyCharm

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

print(L[0][2])
print(L[1][2])
print(L[2][2])
print(L[:2])

#print(list(range(len(input("你的名字：")))));

sum=0
for x in range(0,3,2):
    sum+=x;
print(sum)

x = input("请输入：");

li = list(set(x));

print(type(li))

li.sort(key=x.index);
print (li);