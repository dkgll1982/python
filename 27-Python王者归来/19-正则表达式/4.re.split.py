#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-11-14 09:51:50 
# @Last Modified by: guojun 
# @Last Modified time: 2019-11-14 09:51:50 
# @Software: vscode 
import re

#使用括号捕获分组的适合，默认保留分割符  
p = re.compile(r'(\W+)')
#.split(string[, maxsplit=0]),默认maxsplit=0表示全部分割
print(p.split('This is a test, short and sweet, of split().'))
print(p.split('This is a test, short and sweet, of split().',0))
print(p.split('This is a test, short and sweet, of split().',1))
print(p.split('This is a test, short and sweet, of split().',2))
print(p.split('This is a test, short and sweet, of split().',3))
print(p.split('This is a test, short and sweet, of split().',4))
print(p.split('This is a test, short and sweet, of split().',5))
print(p.split('This is a test, short and sweet, of split().',6))
print(p.split('This is a test, short and sweet, of split().',7))
print(p.split('This is a test, short and sweet, of split().',8))
print(p.split('This is a test, short and sweet, of split().',9))
print(p.split('This is a test, short and sweet, of split().',100))