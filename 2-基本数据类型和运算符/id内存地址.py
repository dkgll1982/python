#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-01-06 14:18:52 
# @Last Modified by: guojun 
# @Last Modified time: 2020-01-06 14:18:52 
# @Software: vscode 
from copy import *
a=[1,2,3,[4,5,6]]
b=a
c=copy(a)
d=deepcopy(a)
print(id(1),id(2),id(3),id(4))
print(id(1),id(2),id(3),id(4))
print(a,"a的内存地址",id(a))
print(b,"b的内存地址",id(b))
print(c,"c的内存地址",id(c))
print(d,"d的内存地址",id(d))
print("<-------------------------------------->")
print("            a[0]的内存地址",id(a[0]))
print("    copy所得c[0]的内存地址",id(c[0]))
print("deepcopy所得d[0]的内存地址",id(d[0]))
print("            a[3]的内存地址",id(a[3]))
print("    copy所得c[3]的内存地址",id(c[3]))
print("deepcopy所得d[3]的内存地址",id(d[3]))
print("            a[3][0]的内存地址",id(a[3][0]))
print("    copy所得c[3][0]的内存地址",id(c[3][0]))
print("deepcopy所得d[3][0]的内存地址",id(d[3][0]))
print("<------------------------------------->")
a.append(7)
print(a,"执行a.append(7)后a的内存地址",id(a))
print(b,"执行a.append(7)后b的内存地址",id(b))
print(c,"执行a.append(7)后c的内存地址",id(c))
print(d,"执行a.append(7)后d的内存地址",id(d))
a[3][0]=23
print(b)
print(c)
print(d)
print("<-------------------------------------->")
print("            a[0]的内存地址",id(a[0]))
print("    copy所得c[0]的内存地址",id(c[0]))
print("deepcopy所得d[0]的内存地址",id(d[0]))
print("            a[3]的内存地址",id(a[3]))
print("    copy所得c[3]的内存地址",id(c[3]))
print("deepcopy所得d[3]的内存地址",id(d[3]))
print("            a[3][0]的内存地址",id(a[3][0]))
print("    copy所得c[3][0]的内存地址",id(c[3][0]))
print("deepcopy所得d[3][0]的内存地址",id(d[3][0]))
print("<------------------------------------->")
