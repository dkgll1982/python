#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from test7 import fub
import math

print('常量 PI 的值近似为：%125.123f。' % math.pi)

import  sys

for x in dir(sys):
    print(' '+x,end =';\r\n')

s = 'Hello, Runoob';
print(repr(s));