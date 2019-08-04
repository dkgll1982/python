#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-08-03 21:22:02 
# @Last Modified by: guojun 
# @Last Modified time: 2019-08-03 21:22:02 
# @Software: vscode 

def print_blank_triangle(n):
    '使用星号打印一个空心的三角形'
    if n <= 0:
        raise ValueError('n必须大于0')
    for i in range(n):
        print(' ' * (n - i - 1), end='')
        print('*', end='')
        if i != n - 1:
            print(' ' * (2 * i - 1), end='')
        else:
            print('*' * (2 * i - 1), end='')
        if i != 0:
            print('*')
        else:
            print('')