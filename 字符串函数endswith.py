#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-07-22 16:15
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : 字符串函数endswith
# @Software: PyCharm
str = "i love python"
print("1:", str.endswith("n"))
print("2:", str.endswith("python"))
print("3:", str.endswith("e", 0, 6))  # 索引 i love 是否以“n”结尾。
print("4:", str.endswith(""))  # 空字符
print("5:", str[0:6].endswith("n"))  # 只索引 i love
print("6:", str[0:6].endswith("e"))
print("7:", str[0:6].endswith(""))
print("8:", str.endswith(("n", "z")))  # 遍历元组的元素，存在即返回True，否者返回False
print("9:", str.endswith(("k", "m")))

# 元组案例
file = "python.txt"
if file.endswith("txt"):
    print("该文件是文本文件")
elif file.endswith(("AVI", "WMV", "RM")):
    print("该文件为视频文件")
else:
    print("文件格式未知")