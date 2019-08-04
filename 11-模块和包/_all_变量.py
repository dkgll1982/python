#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-08-03 20:38:51 
# @Last Modified by: guojun 
# @Last Modified time: 2019-08-03 20:38:51 
# @Software: vscode 

'测试__all__变量的模块'


def hello():
    print("Hello, Python")
def world():
    print("Pyhton World is funny")
def test():
    print('--test--')

# 定义__all__变量，指定默认只导入hello和world两个程序单元
__all__ = ['hello', 'world']

import string

print(string.__all__)
print(string.__file__)