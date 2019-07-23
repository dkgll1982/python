#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-07-22 17:37
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 列表常用方法
# @Software: PyCharm

r = range(1, 10)
print(type(r))
c_list = list(r)
# 指定step为2，被赋值的元素有4个，因此用于赋值的列表也必须有4个元素
c_list[2: 9: 2] = ['a', 'b', 'c', 'd']
print(c_list) # [1, 2, 'a', 4, 'b', 6, 'c', 8, 'd']

a_list = [2, 30, 'a', [5, 30], 30]
# 计算列表中30的出现次数
print(a_list.count(30))
# 计算列表中[5, 30]的出现次数
print(a_list.count([5, 30]))

a_list2 = [2, 30, 'a', 'b', 'crazyit', 30]
# 定位元素30的出现位置
print(a_list2.index(30))
# 从索引2处开始、定位元素30的出现位置
print(a_list2.index(30, 2))
# 从索引2处到索引4处之间定位元素30的出现位置，因为找不到该元素，会引发 ValueError 错误

l = list(range(10,1,-2))

print(l);
l.insert(1,3)
l.sort(reverse=True);
print(l)

#在 Python 中，元组通常都是使用一对小括号将所有元素括起来的，但小括号不是必须的，只要将各元素用逗号隔开，Python 就会将其视为元组
a_tuple = "C语言中文网","http://c.biancheng.net"
print(a_tuple)