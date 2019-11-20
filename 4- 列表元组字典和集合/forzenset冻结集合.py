#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-11-09 14:07:57 
# @Last Modified by: guojun 
# @Last Modified time: 2019-11-09 14:07:57 
# @Software: vscode 

x = frozenset([1,3,5])
y = frozenset([5,7,9]) 
z = x | y


print('{}和{}的交集:{}'.format(x,y,x&y))
print('{}和{}的并集:{}'.format(x,y,x|y)) 
print('{}相对{}的差集:{}'.format(x,y,x-y)) 
print('{}相对{}的差集:{}'.format(y,x,y-x)) 
print('{}相对{}的对称差集:{}'.format(x,y,x.symmetric_difference(y))) 
print('{}相对{}的对称差集:{}'.format(x,y,x^y)) 
print('{}是{}的超集:{}'.format(z,x,z.issuperset(x)))
print('{}是{}的超集:{}'.format(z,y,z.issuperset(y)))
print('{}是{}的子集:{}'.format(x,z,x.issubset(z)))
print('{}是{}的子集:{}'.format(y,z,y.issubset(z)))

# intersection_update() 方法不同于 intersection() 方法，因为 intersection() 方法是返回一个新的集合，
# 而 intersection_update() 方法是在原始的集合上移除不重叠的元素。
# 语法
# intersection_update() 方法语法： 
# set.intersection_update(set1, set2 ... etc)
# 参数
# set1 -- 必需，要查找相同元素的集合
# set2 -- 可选，其他要查找相同元素的集合，可以多个，多个使用逗号 , 隔开
# 返回值
# 无。 
#实例
# 返回一个新集合，该集合的元素既包含在集合 x 又包含在集合 y 中： 
# 实例 1
x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "apple"}
 
x.intersection_update(y) 
 
print(x) 

#计算多个集合的并集： 
#实例 1
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}
 
x.intersection_update(y, z)
 
print(x)

x = {1,3,5}
y = {5,7,9}
x.intersection_update(y) 
print(x)

print('-'*40)

x = {1,3,5}
y = {5,7,9}
x.update(y)
print(x)

print('+'*40)

x = {1,3,5}
y = {5,7,9}
z = frozenset([4,5,6,9])
x.difference_update(y) 
print(x)

y.update(z)
print(y)