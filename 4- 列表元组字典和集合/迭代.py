#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-08-08 14:41
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 迭代
# @Software: PyCharm

L = [1,2,3,4,5,6,1,2,34,64,0,23423,-3,4444345,121,-546,23424,2342342];

min, max = 0, 0;
for x in L:
    if min>x:
        min=x;
    if max<x:
        max=x;

print("max=",max);
print("min=",min);

d = {'a': 1, 'b': 2, 'c': 3}

for x in d:
    print("%s=%d" % (x,d[x]));

for key,val in d.items():
    print("%s=%d" % (key,val));
