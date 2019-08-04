#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-08-13 16:24
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 模块_导入
# @Software: PyCharm
from 模块 import test

test();
help(test)
print(test.__doc__)

print('-'*40)

import print_shape as p
print(p.__doc__)

p.print_triangle(12)
  