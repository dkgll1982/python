#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-08-02 11:58:20 
# @Last Modified by: guojun 
# @Last Modified time: 2019-08-02 11:58:20 
# @Software: vscode 


#一个简单的测试模块: fkmodule'
print("this is fk_module")
name = 'fkit'
def hello():
    print("Hello, Python")
#接下来，在相同的路径下定义如下程序来使用该模块：

import fk_module
print("================")
# 打印fk_module的类型
print(type(fk_module))
print(fk_module)

from fk_module import name, hello
print("================")
print(name)
print(hello)
# 打印fk_module
print(fk_module)