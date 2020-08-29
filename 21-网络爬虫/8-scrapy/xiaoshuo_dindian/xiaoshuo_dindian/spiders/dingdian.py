#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-08-29 18:55:47 
# @Remark: 人生苦短，我用python！
# 参考链接1：https://blog.csdn.net/mmayanshuo/article/details/79229551?utm_source=blogxgwz3
# 参考链接2：https://www.cnblogs.com/yuxuanlian/p/10000968.html

import scrapy
from ..items import XiaoshuoDindianItem

class DingdianSpider(scrapy.Spider):
    name = 'dingdian'
    allowed_domains = ['23us.com']
    start_urls = ['http://23us.com/']

    def parse(self, response):
        pass
