#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-04-01 09:03:19 
# @Remark: 人生苦短，我用python！

from pyquery import PyQuery as pq 
import requests
 
#以下方式存在中文gbk编码问题报错
# doc = pq(filename=r'backup\爬虫\禅道.html')
# print(doc('#companyname'))

with open(r'backup\爬虫\禅道.html',encoding='utf8') as f:
    content = f.read()
doc = pq(content)
print(doc('#companyname'))
