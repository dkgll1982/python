#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-08-03 21:23:27 
# @Last Modified by: guojun 
# @Last Modified time: 2019-08-03 21:23:27 
# @Software: vscode 

# 导入fk_package包，实际上就是导入包下__init__.py文件
import fk_package
# 直接使用fk_package前缀即可调用它所包含的模块内的程序单元。
fk_package.print_blank_triangle(5)
im = fk_package.Item(4.5)
print(im)
fk_package.print_multiple_chart(5)