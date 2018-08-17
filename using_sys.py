#!/usr/bin/python3
# 文件名: using_sys.py

import sys 
from support import print_func,func2

print('命令行参数如下:')
for i in sys.argv:
   print(i)

print('\n\nPython 路径为：', sys.path, '\n')

print_func("郭君");

func2(213);

print(dir(func2));