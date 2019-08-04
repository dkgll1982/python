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
# 导入fk_package包下的print_shape模块，
# 实际上就是导入fk_package目录下的print_shape.py
import fk_package.print_shape
# 实际上就是导入fk_package包（模块）导入print_shape模块
from fk_package import billing
# 导入fk_package包下的arithmetic_chart模块，
# 实际上就是导入fk_package目录下的arithmetic_chart.py
import fk_package.arithmetic_chart
fk_package.print_shape.print_blank_triangle(5)
im = billing.Item(4.5)
print(im)
fk_package.arithmetic_chart.print_multiple_chart(5)