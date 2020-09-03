#!/usr/bin/env python 
# -*- coding:utf-8 -*-  
# @Author: suixin 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd  
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-09-03 20:13:38 
# @Remark: Life is short, I use python！
# 参考链接：https://blog.csdn.net/kingx3/article/details/108364168

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class YgwzSpider(CrawlSpider):
    name = 'ygwz'
    allowed_domains = ['sun0769.com']
    start_urls = ['http://wz.sun0769.com/political/index/politicsNewest?id=1']
    
    rules = (
        Rule(LinkExtractor(allow=r'wz.sun0769.com/political/index/politicsNewest\?id=\d+'),follow=True),
        Rule(LinkExtractor(
            allow=r'wz.sun0769.com/political/politics/index\?id=\d+'), callback='parse_item',follow=True),
    )

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        item['content'] = response.xpath('//div[@class="details-box"]/pre/text()').extract_first()
        print(item)
        return item