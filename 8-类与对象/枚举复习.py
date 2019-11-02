#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-11-02 12:16:45 
# @Last Modified by: guojun 
# @Last Modified time: 2019-11-02 12:16:45 
# @Software: vscode 
#参考链接：https://segmentfault.com/a/1190000017327003?utm_source=tag-newest

from enum import Enum,IntEnum, unique
import enum
# 扩展枚举 IntEnum
# IntEnum 是 Enum 的扩展，不同类型的整数枚举也可以相互比较：
class color(IntEnum):
    YELLOW  = 1
    RED     = 2
    GREEN   = 'r3'  #ValueError: invalid literal for int() with base 10: 'r3'
    PINK    = 4
 
# 访问枚举项 
print(color['GREEN'].name)
print(color['GREEN'].value)