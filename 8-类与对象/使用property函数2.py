#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-07-28 17:47
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 使用property函数2
# @Software: PyCharm

import  math

# -*- coding: utf-8 -*-
class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @width.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height

s = Screen()
s.width = 10
s.height = 100

#s.resolution=2;

print(s.resolution)

print('{0} and {1}'.format('spam', 'eggs'))

print(max([1,2,3]))

import random
print(random.choice(['apple', 'pear', 'banana']))

import statistics
data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
print(statistics.mean([x for x in range(1,11)]))

a = 2
c = 100
c = a + b
print(b)


