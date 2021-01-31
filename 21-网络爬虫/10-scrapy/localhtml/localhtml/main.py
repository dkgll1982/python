#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : guojun
# @Company : 航天神舟智慧系统技术有限公司 
# @Site    : https://user.qzone.qq.com/350606539/main
# @Date    : 2020-08-26 16:05
# @File    : main
# @Software: PyCharm

from scrapy import cmdline
import os

#获取当前目录
path = os.path.dirname(os.path.realpath(__file__))
#设置当前目录为工作目录
os.chdir(path)
cmdline.execute("scrapy crawl local1".split())