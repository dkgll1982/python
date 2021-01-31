#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-08-27 14:15:27 
# 参考链接：https://www.zbpblog.com/blog-96.html

import scrapy
from ..items import DoubanBookItem

class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['douban.com']
    start_urls=['https://book.douban.com/top250']

    def parse(self, response):
        book_list = response.xpath("//tr[@class='item']")
        for li in book_list:
            item = DoubanBookItem()         #这个容器必须放在循环中
            
            item['name'] = li.xpath("td[2]/div[@class='pl2']/a/@title").extract_first()
            item['ratings'] = li.xpath("td[2]/div[2]/span[@class='rating_nums']/text()").extract_first()
            book_info = li.xpath("td[2]/p[1]/text()").extract_first()
            book_info_list = book_info.strip().split(" / ")
            item['author'] = book_info_list[0]
            item['publisher'] = book_info_list[-3]
            item['edition_time'] = book_info_list[-2]
            item['price'] = book_info_list[-1]

            yield item
            
        #下一页
        next_url = response.xpath("//span[@class='next']/a/@href").extract_first()
        if next_url:
            if next_url.find('http') != -1:  
                yield scrapy.Request(url = next_url, callback = self.parse)
