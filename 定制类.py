#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-08-16 10:32
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 定制类
# @Software: PyCharm

class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        print("隔离")
        return 'Student object (name: %s)' % self.name

    __repr__=__str__;

    def __getattribute__(self, attr):
        if attr == 'score':
            return 99


sto = Student("Michael");

#print(sto)
print(sto.score);

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1                       # 初始化两个计数器a，b
    def __iter__(self):
        return self                                 # 实例本身就是迭代对象，故返回自己
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b    # 计算下一个值
        if self.a > 1999:                           # 退出循环的条件
            raise StopIteration()
        return self.a                               # 返回下一个值
    def __getitem__(self, n):                       # 实现下标访问
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a

print(dir(object))
print(dir(Student))
print(dir(Fib))

for n in Fib():
    print(n)
print(Fib()[123])