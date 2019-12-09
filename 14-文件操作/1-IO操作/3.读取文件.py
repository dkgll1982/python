#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-08-04 13:53:22 
# @Last Modified by: guojun 
# @Last Modified time: 2019-08-04 13:53:22 
# @Software: vscode 
import codecs

file = r"backup\\note.txt"; 
#指定使用utf-8 字符集读取文件内容
f = codecs.open(file, 'r', 'GBK', buffering=True)
while True:
    #每次读取一个字符
    ch = f.read(1)
    #如果没有读取到数据，则跳出循环
    if not ch : break
    #输出ch
    print (ch, end='')
f.close()