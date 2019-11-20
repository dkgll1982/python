#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-11-09 14:42:09 
# @Last Modified by: guojun 
# @Last Modified time: 2019-11-09 14:42:09 
# @Software: vscode 
# 参考链接：https://www.cnblogs.com/gpd-Amos/p/8998059.html （python函数中把列表(list)当参数时的"入坑"与"出坑"）
# 当列表，字典作为函数参数时，地址不会发生改变，如果调用时传递了新的参数，则使用新的参数，如果没有传递则使用默认的列表作为参数。
# list并不在函数调用结束后就释放资源。当它作为函数参数时，相当于全局变量，在函数预处理时就已经分配了内存空间。

#1） 深拷贝： 
#M=[A,b,a,c] 
#N=M[:] 
#2） 浅拷贝： 
#N=M

def updatelist(source,target):
    while source:
        temp = source.pop()
        print('源表随机移除元素：',temp)
        target.append(temp)

l1 = [1,2,3,4,5]
l2 = []

print('浅复制移除前：源表-{}，目标表{}'.format(l1,l2))
updatelist(l1,l2)
print('浅复制移除后：源表-{}，目标表{}\r\n'.format(l1,l2))

l1 = [1,2,3,4,5]
l2 = []
print('深复制移除后：源表-{}，目标表{}'.format(l1,l2))
updatelist(l1.copy(),l2.copy())
print('深复制移除后：源表-{}，目标表{}'.format(l1,l2))

l3 = l1
l4 = l1.copy()
print(id(l1),id(l3),id(l4))

l5,l6=1,1
l6 = 4
print(l5,id(l5),id(l6))