#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-08-29 18:58:31 
# @Remark: 人生苦短，我用python！
# 参考链接1：https://blog.csdn.net/qq_42543264/article/details/88715113

import scrapy
from ..items import XiaoshuoBiqugeItem

class BiqugeSpider(scrapy.Spider):
    name = 'biquge'
    allowed_domains = ['biqukan.cc']
    start_urls = ['http://biqukan.cc/']

    def parse(self, response):
        pass
