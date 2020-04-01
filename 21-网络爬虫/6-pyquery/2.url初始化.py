#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-04-01 09:03:19 
# @Remark: 人生苦短，我用python！

from pyquery import PyQuery as pq 
import requests

doc = pq(url='http://www.sina.com')
print(doc('title'))

#与下边功能一样
doc = pq(requests.get('https://www.baidu.com').content.decode('utf8'))
print(doc('title'))

re = requests.get('https://www.baidu.com')
re.encoding = 'utf8'
doc = pq(re.text)
print(doc('title'))