#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-08-08 14:29
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 切片
# @Software: PyCharm
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack', 'chen', 'chen2', 'chen3', 'chen4', 'chen5', 'chen6']

#取前三个元素
print(L[:3])

#取第3到第5个数
print(L[2:5])

#后5个数
print(L[-5:])

#从后取倒数第5个数至倒数第3个数
print(L[-5:-2])

#所有数,每两个取1个
print(L[::2])

#取第2到第10个元素,每两个取1个
print(L[1:10:2])

#取倒数第6至倒数第2个元素,每两个取1个
print(L[-6:-1:2])
