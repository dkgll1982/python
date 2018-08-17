#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-07-02 15:38
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 枚举
# @Software: PyCharm

from enum import IntEnum, unique
@unique
class my_Enum(IntEnum):
    red=1,
    green=2,
    blue=3,
    what=3,
    yellow=9
#按名字取出枚举的值
print(my_Enum['red'])
print(my_Enum['what'])
#枚举的值返回枚举名字
print(my_Enum(9))
print(my_Enum['red'].name)
print(my_Enum['red'].value)
#可以用for in迭代
for i in my_Enum:
    print(i.name,'->',i.value)