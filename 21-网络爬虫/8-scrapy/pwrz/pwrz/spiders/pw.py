#!/usr/bin/env python 
# -*- coding:utf-8 -*-  
# @Author: suixin 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd  
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2021-01-21 16:21:57 
# @Remark: Life is short, I use python！ 
# @Software: vscode

import scrapy
from ..items import PwrzItem

class PwSpider(scrapy.Spider):
    name = 'pw'
    allowed_domains = ['www.jcodecraeer.com']
    start_urls = ['http://www.jcodecraeer.com/plus/list_tid_4.html']

    def parse(self, response):
        li_list = response.css("div.archive-detail")
        for li in li_list:
            item = PwrzItem()
            item["title"] = li.css("h3>a::text").extract_first()
            item["author"] = li.xpath("//li[@class='list-user']/a/span/text()").extract_first()
            item["vnum"] = li.xpath("//li[@class='list-msg']/span[@class='glyphicon-class'][1]/text()").extract_first()
            item["cnum"] = li.xpath("//li[@class='list-msg']/span[@class='glyphicon-class'][2]/text()").extract_first()
            item["time"] = li.xpath("//div[@class='archive-data']/span[@class='glyphicon-class']/text()").extract_first()
            url = response.urljoin(li.css("h3>a::attr(href)").extract_first())
            
            yield scrapy.Request(url=url, callback=self.parse_content, meta={"item": item})

        #下一页
        next_page = response.css("div.pagination li:nth-last-child(3)>a::attr(href)").extract_first()
        if next_page:
            yield scrapy.Request(url = response.urljoin(next_page),callback=self.parse)
    
    #详情页获取内容
    def parse_content(self,response):
        item = response.meta.get('item')
        item['content'] = "".join(response.xpath("//div[@class='arc_body']//text()").extract())
        yield item