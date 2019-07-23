#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-07-23 18:06
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : zip函数
# @Software: PyCharm

a = [1,2,3]
b = [4,5,6]
c = [4,5,6,7,8]
zipped = zip(a,b)     # 打包为元组的列表
print(list(zipped))
#[(1, 4), (2, 5), (3, 6)]
print(list(zip(a,c)))              # 元素个数与最短的列表一致
#[(1, 4), (2, 5), (3, 6)]
print(list(zip(*zipped)))          # 与 zip 相反，*zipped 可理解为解压，返回二维矩阵式
#[(1, 2, 3), (4, 5, 6)]