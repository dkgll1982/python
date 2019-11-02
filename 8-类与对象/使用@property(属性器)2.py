#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-07-02 14:00
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : @property
# @Software: PyCharm

class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value*100

s = Student()

s.score = 60         # OK，实际转化为s.set_score(60)
print(s.score)       # OK，实际转化为s.get_score()


class Screen():
    @property
    def width(self):
        return self._width;
    @property
    def height(self):
        return self._height;
    @width.setter
    def width(self,value):
        self._width=value;
    @height.setter
    def height(self,value):
        self._height=value;

    @property
    def resolution(self):
        return  self._height*self._width

s = Screen();
s.width = 1024;
s.height = 768;

print(s.resolution)

class Student(object):
    name="";
    def __init__(self, name):
        self.name = name

stu = Student("张三");
stu2 = Student("张三");
print(stu.__repr__());
print(stu.__getattribute__("name"));
