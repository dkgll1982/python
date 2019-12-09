#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-07-16 17:55
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 列表生成式
# @Software: PyCharm

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(s):
    return s[1];

L1 = sorted(L,  key=by_name,reverse=True)

print(L1);

L = []
for x in range(1, 11):
    L.append((x,x * x))
print(L)

# append() 方法传递列表或者元组，此方法也只会将其视为一个元素，直接添加到列表中，从而形成包含列表和元组的新列表
L2 = []
for x in range(1, 11):
    L2.insert(0,x * x)
print(L2)

print(L2[1::2]);
del L2[::2]

#remove() 方法会删除第一个和指定值相同的元素，如果找不到该元素，该方法将会引发 ValueError 错误。
L2.remove(49)
print(L2);
L2.clear()

print(L2);

#如果希望不将被追加的列表或元组当成一个整体，而是只追加列表中的元素，则可使用列表提供的 extend() 方法。
L3 = []
for x in range(1, 11):
    L3.extend((x,x * x))
print(L3)

m = [x*y for x in range(1,11) if x%2==0 for y in range(1,11) if y%3==0]

print(m)

#毕达哥拉斯三元组
m3 = [(x,y,z) for x in range(1,30) for y in range(x,30)  for z in range(y,30) if x*x+y*y==z*z]
print(m3);

#列出磁盘目录文件
import os
o = [d for d in os.listdir('.')];

print(o)

d = {'x': 'A', 'y': 'B', 'z': 'C' }
print([k + '=' + v for k, v in d.items()]);

L = ['Hello', 'World', 'IBM', 'Apple']

#Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
l = [ "第" + str(key+1) + "个元素值:" + val.lower() for key,val in enumerate(L)]
print(l)

