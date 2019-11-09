#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-11-08 22:26:30 
# @Last Modified by: guojun 
# @Last Modified time: 2019-11-08 22:26:30 
# @Software: vscode 

#导入sympy
from sympy import *

#定义变量
x = Symbol('x')
y = Symbol('y')
print(solve([x + 1 - y,-1 * x + 1 - y],[x,y]))

print(solve([x*x-4],[x]))

l = [x**x for x in range(1,10)]
print(l)
m = [[x,y] for x in range(1,10) for y in range(1,5) if y!=x]
print(m)