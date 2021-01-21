#!/usr/bin/env python 
# -*- coding:utf-8 -*-  
# @Author: suixin 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd  
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2021-01-19 17:35:59 
# @Remark: Life is short, I use python！ 
# @Software: vscode 
# 备注：本项目参考《精通Scrapy网络爬虫.pdf》

import scrapy
from scrapy.linkextractors import LinkExtractor
from ..items import BookItem

class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    # 书籍列表页面的解析函数 
    def parse(self, response): # 提取书籍列表页面中每本书的链接 
        #在页面含有少量链接时，使用selector来提取信息就可以，但如果链接特别多时，就需要用LinkExtractor来提取。
        le = LinkExtractor(restrict_css='article.product_pod h3') 
        for link in le.extract_links(response): 
            yield scrapy.Request(link.url, callback=self.parse_book) 
        
        # 提取"下一页"的链接 
        le = LinkExtractor(restrict_css='ul.pager li.next') 
        links = le.extract_links(response) 
        if links: 
            next_url = links[0].url 
            yield scrapy.Request(next_url, callback=self.parse) 
            
    # 书籍页面的解析函数 
    def parse_book(self, response): 
        book = BookItem() 
        sel = response.css('div.product_main') 
        book['name'] = sel.xpath('./h1/text()').extract_first() 
        book['price'] = sel.css('p.price_color::text').extract_first() 
        book['review_rating'] = sel.css('p.star-rating::attr(class)').re_first('star-rating ([A-Za-z]+)') 
        sel = response.css('table.table.table-striped') 
        book['upc'] = sel.xpath('(.//tr)[1]/td/text()').extract_first() 
        #re 正则表达式re_first返回其中第一个Selector对象
        book['stock'] = sel.xpath('(.//tr)[last()-1]/td/text()').re_first('\((\d+) available\)') 
        book['review_num'] = sel.xpath('(.//tr)[last()]/td/text()').extract_first() 
        yield book