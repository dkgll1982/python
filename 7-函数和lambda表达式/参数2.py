#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-07-24 20:44
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 参数2
# @Software: PyCharm

def test(name, message):
    print("用户是: ", name)
    print("欢迎消息: ", message)
my_list = ['孙悟空', '欢迎来C语言中文网']
test(*my_list)
print('-'*40)
def foo(name, *nums):
    print("name参数: ", name)
    print("nums参数: ", nums)
my_tuple = (1, 2, 3)
str='fkit'
# 使用逆向收集，将my_tuple元组的元素传给nums参数
foo('fkit', *str)
foo('fkit', *my_tuple)
foo(*my_tuple)
print('-'*40)
foo(my_tuple,my_tuple)

print('-'*40)
def bar(book, price, desc):
    print(book, "VIP价格是:", price)
    print('描述信息', desc)
    return 1,2
my_dict = {'price': 159, 'book': 'C语言中文网', 'desc': '这是一个精美而实用的网站'}
# 按逆向收集的方式将my_dict的多个key-value传给bar()函数
re,re2 = bar(**my_dict)

print(re)
print(re2)