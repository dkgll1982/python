#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-08-08 10:05
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 元组
# @Software: PyCharm


#创建元组 a_typle
a_tuple =("C语言中文网",)
print(type(a_tuple))
print(a_tuple)
#创建字符串 a
a = ("C语言中文网")
print(type(a))
print(a)

#使用tuple()函数创建元组
# 将列表转换成元组
a_list = ['crazyit', 20, -1.2]
a_tuple = tuple(a_list)
print(a_tuple)

# 使用range()函数创建区间（range）对象
a_range = range(1, 5)
print(a_range)
# 将区间转换成元组
b_tuple = tuple(a_range)
print(b_tuple)
# 创建区间时还指定步长
c_tuple = tuple(range(4, 20, 3))
print(c_tuple)

#通过连接多个元组的方式向元组中添加新元素
d_tuple=b_tuple+c_tuple;

print((d_tuple))

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

print(type(x))

print(x.index)
li.sort(key=x.index);
print(li);

print('--------------------')
t=((x,y) for x in range(10) for y in range(10));
#使用元组推导式生成的结果并不是一个元组，而是一个生成器对象（后续会介绍），这一点和列表推导式是不同的。
#运行结果为：<generator object <genexpr> at 0x0000020BAD136620>
print(t)
print(tuple(t))