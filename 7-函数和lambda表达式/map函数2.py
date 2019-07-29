#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-07-29 16:02:21 
# @Last Modified by: guojun 
# @Last Modified time: 2019-07-29 16:02:21 
# @Software: vscode 

import multiprocessing
from functools import partial
from functools import reduce

#map(function, iterable, ...) iterable -- 一个或多个序列
r = map(lambda x, y: x +y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10,11])
print(list(r))

print(list(map(lambda x,y:x*y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10,11])))  

ln =reduce(lambda x,y:x+y,[1,2,3,4,5]);
print(ln)

def fn(x, y):
    return x * 10 + y

int2 =reduce(fn,[4,4,5,7,9,2]);
print(int2)
#字符串转数字

str ="23213234343223";

def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

li2 =map(char2num,str)
print(li2)

int3 = reduce(fn,li2)
print(int3)


str = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}['2'];
print(str)