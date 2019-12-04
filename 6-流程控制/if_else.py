#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: guojun
# @Company: 航天神舟智慧系统技术有限公司
# @Site: https://user.qzone.qq.com/350606539/main
# @Date: 2018-08-16 15:48:33
# @Last Modified by: guojun
# @Last Modified time: 2018-08-16 15:48:33
# @Software: vscode

age = int(input("请输入你家狗狗的年龄: "))
print("")
if age < 0:
    print("你是在逗我吧!")
    age = 100
elif age == 1:
    print("相当于 14 岁的人。")
elif age == 2:
    print("相当于 22 岁的人。")
elif age > 2 and age < 20:
    human = 22 + (age - 2)*5
    print("对应人类年龄: ", human)
else:
    print("活了"+str(age)+"岁，已经成仙了吧! ")
print('你修改了年龄:%s'%age)
# 退出提示
input("点击 enter 键退出")
