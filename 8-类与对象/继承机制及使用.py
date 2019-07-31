#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-07-28 20:09
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 继承机制及使用
# @Software: PyCharm

class Item:
    def info (self):
        print("Item中方法:", '这是一个商品')
class Product:
    def info (self):
        print("Product中方法:", '这是一个工业产品')
class Mouse(Item, Product): # ①
#class Mouse(Product, Item): # ①
    pass
    # 重写info方法
#    def info (self):
#        print("Product中方法:", '这是一个军工产品')
m = Mouse()
m.info()
print('-'*40)

class BaseClass:
    def foo (self):
        print('父类中定义的foo方法',self)
class SubClass(BaseClass):
    # 重写父类的foo方法
    def foo (self):
        print('子类重写父类中的foo方法')
    def bar (self):
        print('执行bar方法')
        # 直接执行foo方法，将会调用子类重写之后的foo()方法
        self.foo()
        # 使用类名调用实例方法（未绑定方法）调用父类被重写的方法
        BaseClass.foo(self)
sc = SubClass()
sc.bar()

b = BaseClass();
b.foo()


