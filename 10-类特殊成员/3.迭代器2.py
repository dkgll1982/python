#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-07-10 10:19
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 可迭代
# @Software: PyCharm

from collections.abc import Iterable, Iterator, Generator

# 定义一个代表斐波那契数列的迭代器
class Fibs:
    def __init__(self, len):
        self.first = 0
        self.sec = 1
        self.__len = len
    # 定义迭代器所需的__next__方法
    def __next__(self):
        # 如果__len__属性为0，结束迭代
        if self.__len == 0:
            raise StopIteration
        # 完成数列计算：
        self.first, self.sec = self.sec, self.first + self.sec
        # 数列长度减1
        self.__len -= 1
        return self.first
    # 定义__iter__方法，该方法返回迭代器
    def __iter__(self):
        return self
# 创建Fibs对象
fibs = Fibs(10)
# 获取迭代器的下一个元素
print(next(fibs))
# 使用for循环遍历迭代器
for el in fibs:
    print(el, end=' ')

print('')
print('-'*40)

# 程序可使用内置的 iter() 函数将列表、元组等转换成迭代器

# 将列表转换为迭代器
my_iter = iter([2, 'fkit', 4])
# 依次获取迭代器的下一个元素
print(type(my_iter))
print(my_iter.__next__()) # 2
print(my_iter.__next__()) # fkit

print(type(type(my_iter)))
print('对象是否可迭代：',isinstance(my_iter,Iterable))
print('1234是否可迭代：',isinstance(iter('1234'),Iterable))
print('(1,2,3,4)是否可迭代：',isinstance(iter((1,2,3,4)),Iterable))
print('{"name","dsdsdsd"}是否可迭代：',isinstance(iter({"name","dsdsdsd"}),Iterable))
print('[1,2,3,4]是否可迭代：',isinstance([1,2,3,4],Iterable))
