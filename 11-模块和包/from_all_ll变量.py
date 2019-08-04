#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-08-03 20:56:20 
# @Last Modified by: guojun 
# @Last Modified time: 2019-08-03 20:56:20 
# @Software: vscode 

from _all_变量 import *
hello()
world() 

# t.test() # 会提示找不到test()函数

# 如果确实希望程序使用模块内 __all__ 列表之外的程序单元，有两种解决方法：
# 第一种是使用“import 模块名”来导入模块。在通过这种方式导入模块之后，总可以通过模块名前缀（如果为模块指定了别名，则可以使用模快的别名作为前缀）来调用模块内的成员。
# 第二种是使用“from 模块名 import 程序单元”来导入指定程序单元。在这种方式下，即使想导入的程序单元没有位于 __all__ 列表中，也依然可以导入。
import _all_变量 as t

t.test() 

from _all_变量 import test

test();
