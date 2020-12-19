#!/usr/bin/env python 
# -*- coding:utf-8 -*-  
# @Author: suixin 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd  
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-12-14 15:54:55 
# @Remark: Life is short, I use python！import scrapy

import re
import scrapy
from  ..items import Xiaoshuo136BookItem

class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['136book.com']
    start_urls = ['https://www.136book.com/huaqiangu']  #爬取花千骨小说

    def parse(self, response):
        item = Xiaoshuo136BookItem()
	    #提取url
        url_all = response.xpath("//div[@id='book_detail'][2]/ol[@class='clearfix']/li/a/@href").extract() 
        for url_one in url_all: 
            item["url"] = url_one 
            yield scrapy.Request(url = url_one, meta={'item':item}, callback = self.parse1) 

    def parse1(self, response):
        item = response.meta['item']
        item['title'] = response.xpath("//div[@id='main_body']/h1/text()").extract()  
        lis = []
        for i in response.xpath("//*[@id='content']/p/text()").extract():
            #lis.append(re.sub('\s+','',i).strip())
            lis.append(i+'\n')
        # for i in response.xpath("//*[@id='content']/p/text()").extract():
        #     lis.append(re.sub(r"\s+","",i).strip()) 
        item["text"] = lis 
        yield item