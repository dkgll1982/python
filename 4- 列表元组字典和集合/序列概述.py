#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-07-22 16:30
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 序列概述
# @Software: PyCharm

#序列类型包括字符串、列表、元组、集合和字典，这些序列支持以下几种通用的操作，但比较特殊的是，集合和字典不支持索引、切片、相加和相乘操作。
#字符串也是一种常见的序列，它也可以直接通过索引访问字符串内的字符。
str2='中华人民共和国公民';
#取索引区间为[0,2]之间（不包括索引2处的字符）的字符串
print(str2[:2])
#隔 1 个字符取一个字符，区间是整个字符串
print(str2[::2])

print("我"+"是"+str2)

print("我"+"是"+(str2+' ')*3)

list=[None];
print(type(list))
list2=list*5
print(list*5);
for i in range(len(list2)):
    list2[i]=str(i);
print(list2);

for i in range(len(str2)):
    print(str2[i]+"\t");


str="c.biancheng.net"
#找出最大的字符
print(max(str))
#找出最小的字符
print(min(str))
#对字符串中的元素进行排序
print(sorted(str))