#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-08-13 16:08
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 模块
# @Software: PyCharm
' a test module '
__author__ = 'Michael Liao'

import sys
def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!%s'% args[0])
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')


def test2():
    print('子函数!')

if __name__=='__main__':
    test()
else:
    print("不是通过main函数启动的，不会进行初始化！")