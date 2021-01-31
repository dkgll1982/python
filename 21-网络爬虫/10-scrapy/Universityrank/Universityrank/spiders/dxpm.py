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
from ..items import UniversityrankItem

class DxpmSpider(scrapy.Spider):
    name = 'dxpm'
    allowed_domains = ['university-list.net']
    start_url = 'https://www.university-list.net/paiming/dx-{}.html'
    
    def start_requests(self):
        for index in range(160001,160013):            
            yield scrapy.Request(url = self.start_url.format(index),callback=self.parse)

    def parse(self, response):
        item = UniversityrankItem()
        table = response.xpath("//table/tbody/tr")
        # 大学列表
        for tr in table:
            item['rank'] = tr.xpath("td[1]/text()").extract()[0]
            item['school'] = tr.xpath("td[2]/text()").extract()[0]
            item['area'] = tr.xpath("td[3]/text()").extract()[0]
            item['score'] = tr.xpath("td[4]/text()").extract()[0]
            yield item