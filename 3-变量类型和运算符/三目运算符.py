#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-07-22 16:20
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 三目运算符
# @Software: PyCharm

a = 32
b = 32
st = "a大于b" if a > b else ("a等于b" if a==b  else  "a不大于b")
# 输出"a大于b"
print(st)

print("a大于b") if a > b else print("a不大于b")
print("a大于b" if a > b else "a不大于b")

def yunsan(num1,num2):
    s =(num1 **2) if num1 is not None else (num2 **2);
    print("%s,%s的乘方：%d"%(num1,num2,s))

yunsan(None,3)