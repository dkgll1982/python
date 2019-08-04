#!/usr/bin/python3
# 文件名: using_sys.py

# 可以为模块指定别名
# 导入整个模块的语法也可一次导入多个模块，多个模块之间用逗号隔开
import sys  as s,os

print('命令行参数如下:')
for i in s.argv:
   print(i)

print('\n\nPython 路径为：', s.path, '\n')
# os模块的sep变量代表平台上的路径分隔符
print(os.sep)

# 导入sys模块的argv成员
# 在程序中通过别名 v 使用 argv 成员，无须使用任何前缀
from sys import argv as v
# 使用导入成员的语法，直接使用成员名访问
print(v[0])
