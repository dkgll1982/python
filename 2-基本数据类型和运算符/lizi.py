#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2018-08-17 11:15:01 
# @Last Modified by: guojun 
# @Last Modified time: 2018-08-17 11:15:01 
# @Software: vscode 

a=12;
b=34;
print(round(a/b,2))
x=round(a/14.0,2)
print('宽比例：%s,高比例：%f'%(x,round(b/86.0,2)))
i = int(input('净利润:'))
arr = [1000000, 600000, 400000, 200000, 100000, 0]
rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
r = 0
for idx in range(0, 6):
    if i > arr[idx]:
        r += float((i - arr[idx])) * rat[idx]
        print(float(i - arr[idx]) * rat[idx])
        i = arr[idx]
print(r)