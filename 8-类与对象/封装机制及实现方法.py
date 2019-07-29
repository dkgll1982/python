#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-07-28 18:07
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 封装机制及实现方法
# @Software: PyCharm

import  json;

class Fruit:
    def ide(self):
        print('1示范隐藏的hide方法')
    def __hide(self):
        print('2示范隐藏的hide方法')
    def _Fruit__hide(self):
        print('3示范隐藏的hide方法')
    def info(self):
        print("我是一个水果！重%g克" % self.weight)

class Food:
    def taste(self):
        print("不同食物的口感不同")

# 定义Apple类，继承了Fruit和Food类
class Apple(Fruit, Food):
    pass

# 创建Apple对象
a = Apple();
a.weight = 5.6;
# 调用Apple对象的info()方法
a.info();
# 调用Apple对象的taste()方法
a.taste();

#Python 并没有提供真正的隐藏机制，所以 Python 类定义的所有成员默认都是公开的；如果程序希望将 Python 类中的某些成员隐藏起来，那么只要让该成员的名字以双下画线开头即可。
#即使通过这种机制实现了隐藏，其实也依然可以绕过去。
a._Fruit__hide()
a.ide()