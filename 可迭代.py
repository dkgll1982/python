#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-07-10 10:19
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 可迭代
# @Software: PyCharm

from collections.abc import Iterable, Iterator, Generator

class MyList(object):  # 定义可迭代对象类

    def __init__(self, num):
        self.end = num  # 上边界

    # 返回一个实现了__iter__和__next__的迭代器类的实例
    def __iter__(self):
        return MyListIterator(self.end)


class MyListIterator(object):  # 定义迭代器类

    def __init__(self, end):
        self.data = end  # 上边界
        self.start = 0

    # 返回该对象的迭代器类的实例；因为自己就是迭代器，所以返回self
    def __iter__(self):
        return self

    # 迭代器类必须实现的方法，若是Python2则是next()函数
    def __next__(self):
        while self.start < self.data:
            self.start += 1
            return self.start - 1
        raise StopIteration


if __name__ == '__main__':
    my_list = MyList(5)  # 得到一个可迭代对象
    print(isinstance(my_list, Iterable))  # True
    print(isinstance(my_list, Iterator))  # False
    # 迭代
    for i in my_list:
        print(i)

    my_iterator = iter(my_list)  # 得到一个迭代器
    print(isinstance(my_iterator, Iterable))  # True
    print(isinstance(my_iterator, Iterator))  # True

    # 迭代
    print(next(my_iterator))
    print(next(my_iterator))
    print(next(my_iterator))
    print(next(my_iterator))
    print(next(my_iterator))