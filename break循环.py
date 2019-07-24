#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-07-23 21:19
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : break循环
# @Software: PyCharm

#如果想达到 break 语句不仅跳出单前所在循环，同时跳出外层循环的目的，可先定义 bool 类型的变量来标志是否需要跳出外层循环，
#然后在内层循环、外层循环中分别使用两条 break 语句来实现。例如如下程序：
exit_flag = False
# 外层循环
for i in range(0, 5) :
    # 内层循环
    for j in range(0, 3 ) :
        print("i的值为: %d, j的值为: %d" % (i, j))
        if j == 1 :
            exit_flag = True
            # 跳出里层循环
            break
    # 如果exit_flag为True，跳出外层循环
    if exit_flag :
        break
