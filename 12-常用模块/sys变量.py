#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-08-04 00:09:49 
# @Last Modified by: guojun 
# @Last Modified time: 2019-08-04 00:09:49 
# @Software: vscode 

import sys
# 显示本地字节序的指示符。
print(sys.byteorder)
# 显示Python解释器有关的版权信息
print(sys.copyright)
# 显示Python解释器在磁盘上的存储路径。
print(sys.executable)
# 显示当前系统上保存文件所用的字符集。
print(sys.getfilesystemencoding())
# 显示Python整数支持的最大值
print(sys.maxsize)
# 显示Python解释器所在平台
print(sys.platform)
# 显示当前Python解释器的版本信息。
print(sys.version)
# 返回当前Python解释器的主版本号。
print(sys.winver)

print('-'*40)

#动态修改模块加载路径
import sys
# 动态添加g:\fk_ext路径作为模块加载路径
sys.path.append('E:\\100-航天智慧\\2-源码库\\python\\11-模块和包') 
# 导入fk_package包，实际上就是导入包下__init__.py文件
import fk_package
# 直接使用fk_package前缀即可调用它所包含的模块内的程序单元。
fk_package.print_blank_triangle(5)
im = fk_package.Item(4.5)
print(im)
fk_package.print_multiple_chart(5)