#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-07-30 17:51:09 
# @Last Modified by: guojun 
# @Last Modified time: 2019-07-30 17:51:09 
# @Software: vscode 

# 检查类型：
# issubclass(cls, class_or_tuple)：检查 cls 是否为后一个类或元组包含的多个类中任意类的子类。
# isinstance(obj, class_or_tuple)：检查 obj 是否为后一个类或元组包含的多个类中任意类的对象。

# 定义一个字符串
hello = "Hello";
# "Hello"是str类的实例，输出True
print('"Hello"是否是str类的实例: ', isinstance(hello, str))
# "Hello"是object类的子类的实例，输出True
print('"Hello"是否是object类的实例: ', isinstance(hello, object))
# str是object类的子类，输出True
print('str是否是object类的子类: ', issubclass(str, object))
# "Hello"不是tuple类及其子类的实例，输出False
print('"Hello"是否是tuple类的实例: ', isinstance(hello, tuple))
# str不是tuple类的子类，输出False
print('str是否是tuple类的子类: ', issubclass(str, tuple))
# 定义一个列表
my_list = [2, 4]
# [2, 4]是list类的实例，输出True
print('[2, 4]是否是list类的实例: ', isinstance(my_list, list))
# [2, 4]是object类的子类的实例，输出True
print('[2, 4]是否是object类及其子类的实例: ', isinstance(my_list, object))
# list是object类的子类，输出True
print('list是否是object类的子类: ', issubclass(list, object))
# [2, 4]不是tuple类及其子类的实例，输出False
print('[2, 4]是否是tuple类及其子类的实例: ', isinstance([2, 4], tuple))
# list不是tuple类的子类，输出False
print('list是否是tuple类的子类: ', issubclass(list, tuple))

print('-'*40)

#issubclass() 和 isinstance() 两个函数的第二个参数都可使用元组
data = (20, 'fkit')
print('data是否为列表或元组: ', isinstance(data, (list, tuple))) # True
# str不是list或者tuple的子类，输出False
print('str是否为list或tuple的子类: ', issubclass(str, (list, tuple)))
# str是list或tuple或object的子类，输出True
print('str是否为list或tuple或object的子类 ', issubclass(str, (list, tuple, object)))

print('-'*40)

#所有类都提供了一个 __bases__ 属性，通过该属性可以查看该类的所有直接父类，该属性返回所有直接父类组成的元组
class A:
    pass
class B:
    pass
class C(A, B):
    pass
class D(C,A, B):
    pass
print('类A的所有父类:', A.__bases__)
print('类B的所有父类:', B.__bases__)
print('类C的所有父类:', C.__bases__)

print('-'*40)

#所有类都提供了一个 __subclasses__() 方法，通过该方法可以查看该类的所有直接子类，该方法返回该类的所有子类组成的列表
print('类A的所有子类:', A.__subclasses__())
print('类B的所有子类:', B.__subclasses__())


print('c是否是a类的子类: ', issubclass(C, A))
print('c是否是B类的子类: ', issubclass(C, B))
print('c是否是A,B类的子类: ', issubclass(C, (A,B)))