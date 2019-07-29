#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-08-15 14:32
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 使用@property
# @Software: PyCharm

#Python内置的@property装饰器就是负责把一个方法变成属性调用的：
#把一个getter方法变成属性，只需要加上@property就可以了，此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值
class Student(object):
    @property
    def score(self):
        return self._score+3

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
s.score = 60 # OK，实际转化为s.set_score(60)
s.score # OK，实际转化为s.get_score()
s.score = 8

print(s.score);

print('------------------------------------------------------');

class Student2(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth

    @property
    def sex(self,value):
        self._sex = value;

s2 = Student2();
s2.birth = 1982;
#s2.age=13;
s2.age2=12;

s2.sex =234

print(str(s2.age)+'岁')



class Student(object):

    def get_score(self):
         return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
        
#现在，对任意的Student实例进行操作，就不能随心所欲地设置score了：

s = Student()
s.set_score(60) # ok!
s.get_score()
#s.set_score(9999)


