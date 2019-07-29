#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-07-28 17:47
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 使用property函数2
# @Software: PyCharm

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






