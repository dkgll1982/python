#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-10-21 22:23:28 
# @Last Modified by: guojun 
# @Last Modified time: 2019-10-21 22:23:28 
# @Software: vscode 

class Score:
    def __init__(self, default=0):
        self._score = default

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Score must be integer')
        if not 0 <= value <= 100:
            raise ValueError('Valid value must be in [0, 100]')

        self._score = value

    def __get__(self, instance, owner):
        return self._score

    def __del__(self):
        del self._score

class Student:
    math = Score()
    chinese = Score()
    english = Score()

    def __init__(self, name='', math=0, chinese=0, english=0):
        self.name = name

        self.math = math
        self.chinese = chinese
        self.english = english

    # def __str__(self):
    #     return "Student类"

    def __repr__(self):
        return "<Student: {}, math:{}, chinese: {}, english:{}>".format(
                self.name, self.math, self.chinese, self.english
            )

# 当把对象作为参数传入print()时，会自动调用对象的__str__方法，但是当__str__方法不存在时，则会调用__repr__方法。
# 所以，如果你只想实现这两个特殊方法中的一个，建议还是选择__repr__方法。            
s = Student('李四',1,1,1)
s.name = '张三'
s.math = 100
s.chinese = 99
s.english = 100
print(s)