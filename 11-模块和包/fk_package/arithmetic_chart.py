#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-08-03 21:22:24 
# @Last Modified by: guojun 
# @Last Modified time: 2019-08-03 21:22:24 
# @Software: vscode 

def print_multiple_chart(n):
    '打印乘法口角表的函数'
    for i in range(n):
        for j in range(i + 1):
            print('%d * %d = %2d' % ((j + 1) , (i + 1) , (j + 1)* (i + 1)), end='  ')
        print('')