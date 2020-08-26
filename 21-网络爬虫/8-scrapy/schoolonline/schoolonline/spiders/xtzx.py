#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : guojun
# @Company : 航天神舟智慧系统技术有限公司
# @Site    : https://user.qzone.qq.com/350606539/main
# @Date    : 2020-08-26 16:05
# @File    : main
# @Software: PyCharm
# 参考链接：https://boyinthesun.cn/post/python-scrapy1/

import scrapy
from ..items import SchoolonlineItem

class XtzxSpider(scrapy.Spider):
    name = 'xtzx'
    allowed_domains = ['xuetangx.com']
    start_urls = ['http://www.xuetangx.com/partners']

    def parse(self, response):
        item = SchoolonlineItem()
        # 开课院校
        for each in response.xpath("/html/body/article[1]/section/ul/*"):
            item['type'] = '开课院校'
            item['school'] = each.xpath("a/div[2]/h3/text()").extract()
            item['num'] = each.xpath("a/div[2]/p/text()").extract()
            yield item
        # edX合作院校和伙伴
        for each in response.xpath("/html/body/article[2]/section/ul/*"):
            item['type'] = 'edX合作院校和伙伴'
            item['school'] = each.xpath("a/div[2]/h3/text()").extract()
            item['num'] = each.xpath("a/div[2]/p/text()").extract()
            yield item
