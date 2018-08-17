#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-07-16 17:55
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 列表生成式
# @Software: PyCharm

L = []
for x in range(1, 11):
    L.append(x * x)
print(L)

m = [x*y for x in range(1,11) if x%2==0 for y in range(1,11) if y%3==0]
2,4,6,8,10
3,6,9

print(m)

#列出磁盘目录文件
import os
o = [d for d in os.listdir('E:\\100-航天智慧\\1-文档库\\1-CIG聚合服务\\数据资源\\Data')];

print(o)

d = {'x': 'A', 'y': 'B', 'z': 'C' }
print([k + '=' + v for k, v in d.items()]);

L = ['Hello', 'World', 'IBM', 'Apple']

#Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
l = [ "第" + str(key+1) + "个元素值:" + val.lower() for key,val in enumerate(L)]
print(l)