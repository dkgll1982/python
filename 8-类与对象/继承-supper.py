#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-08-16 09:54
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 继承-supper
# @Software: PyCharm

class FooParent(object):
    def __init__(self):
        self.parent = 'I\'m the parent.'
        print('Parent初始化方法')

    def bar(self, message):
        print("%s from Parent" % message)

class FooChild(FooParent):
    def __init__(self):
        # super(FooChild,self) 首先找到 FooChild 的父类（就是类 FooParent），然后把类B的对象 FooChild 转换为类 FooParent 的对象
        super().__init__()
        print('Child初始化方法')

    def bar(self, message):
        super().bar(message)
        print('Child bar fuction')
        print(self.parent)

if __name__ == '__main__':
    fooChild = FooChild()
    fooChild.bar('HelloWorld')