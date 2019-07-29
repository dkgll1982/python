#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-07-23 16:54
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 流程控制
# @Software: PyCharm

s = input("请输入一个整数: ")
s = int(s)
if s > 5:
    print("大于5")
elif s < 5:
    # 空语句，相当于占位符
    pass
else:
    print("等于5")

#assert 断言语句和 if 分支有点类似，它用于对一个 bool 表达式进行断言，如果该 bool 表达式为 True，该程序可以继续向下执行；否则程序会引发 AssertionError 错误。
#s_age = input("请输入您的年龄:")
#age = int(s_age)
#assert 20 < age < 80
#print("您输入的年龄在20和80之间")

for x in range(1,10,2):
    print(x)

dict =  {"name":"张三","age":22,"sex":"男","height":176,"edu":"研究生","nation":"汉族"}

for k,v in(dict.items()):
    print("%s:%s"%(k,v))

for k in(dict):
    print("%s:%s"%(k,k))



src_list = [12, 45, 3.4, 12, 'fkit', 45, 3.4, 'fkit', 45, 3.4]
statistics = {}
for ele in src_list:
    # 如果字典中包含ele代表的key
    if ele in statistics.keys():
        # 将ele元素代表出现次数加1
        statistics[ele] += 1
    # 如果字典中不包含ele代表的key，说明该元素还未出现过
    else:
        # 将ele元素代表出现次数设为1
        statistics[ele] = 1
# 遍历dict，打印出各元素的出现次数
for ele, count in statistics.items():
    print("%s的出现次数为:%d" % (ele, count))
