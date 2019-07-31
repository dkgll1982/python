#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-07-02 15:38
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 枚举
# @Software: PyCharm

from enum import IntEnum, unique
import enum
try:
    @unique
    #加上@unique入股go枚举值重复会抛出异常
    class my_Enum(IntEnum):
        red=1,
        green=1,
        blue=3,
        what=5,
        yellow=9
except Exception:
    print("定义错误");
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

print('-'*40)

Season = enum.Enum('Season', ('SPRING', 'SUMMER', 'FALL', 'WINTER'))
# 直接访问指定枚举
print(Season.SPRING)
# 访问枚举成员的变量名
print(Season.SPRING.name)
# 访问枚举成员的值
print(Season.SPRING.value)
# 根据枚举变量名访问枚举对象
print(Season['SUMMER']) # Season.SUMMER
# 根据枚举值访问枚举对象
print(Season(3)) # Season.FALL
print('-'*40)

for index, item in Season.__members__.items():
    print(index,'=>',item,',',item.value);
    