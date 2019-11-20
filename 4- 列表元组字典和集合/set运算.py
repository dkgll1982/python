#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-07-23 10:27
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : set运算
# @Software: PyCharm

set1={1,2,3}
set2={3,4,5}
set3=set() 

print("求交集(取两集合公共的元素)：set1 & set2 = ",set1 & set2);
print("求并集(取两集合全部的元素)：set1 | set2 = ",set1 | set2);
print("求差集(取一个集合中另一集合没有的元素)：set1 - set2 = ",set1 - set2);
print("求对称差集(取集合 A 和 B 中不属于 A&B 的元素)：set1  ^ set2 = ",set1 ^ set2);

t = frozenset('bookshop')
t2 = frozenset('My book')

set1.add(t)
set1.add(t2)
#使用 add() 方法添加的元素，只能是数字、字符串、元组或者布尔类型（True 和 False）值，不能添加列表、字典、集合这类可变的数据，否则 Python 解释器会报 TypeError 错误。例如：
#k可以添加不可变集合frozenset
#set3.add(set2)
print(t)
print(set1)
print(type(set3))
print(set1.pop())
print(set1.pop()) 