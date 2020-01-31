# -*- coding: utf-8 -*-
import scrapy

class BaiduComSpider(scrapy.Spider):
    name = 'baidu.com'
    allowed_domains = ["baidu.com"]
    start_urls = ['http://tieba.baidu.com/f?kw=%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB&ie=utf-8']

    def parse(self, response):
        yield {
            'title': response.xpath('//title/text()').extract_first()
        }