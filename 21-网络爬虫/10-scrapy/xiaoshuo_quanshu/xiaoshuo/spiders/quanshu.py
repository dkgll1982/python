#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-08-28 09:20:07 
# @Remark: 人生苦短，我用python！
# 参考链接：https://www.jianshu.com/p/15291df6d1b9
# 测试发现该站点有反爬策略，不要爬取过快、频繁，仅做测试学习用途

import scrapy
from ..items import XiaoshuoItem
import re

class QuanshuSpider(scrapy.Spider):
    name = 'quanshu'
    allowed_domains = ['quanshuwang.com']
    start_urls = [  'http://www.quanshuwang.com/list/1_2.html']   #全书网玄幻魔法类第2页
        
    # 第一步：获取每一本书的URL
    def parse(self, response):
        book_urls = response.xpath('//li/a[@class="l mr10"]/@href').extract()
        for book_url in book_urls:
            yield scrapy.Request(book_url, callback=self.parse_read)

    # 第二步：获取马上阅读按钮的URL，进入章节目录
    def parse_read(self, response):
        read_url = response.xpath('//a[@class="reader"]/@href').extract()[0]
        yield scrapy.Request(read_url, callback=self.parse_chapter)

    # 第三步：获取小说章节的URL
    def parse_chapter(self, response):
        chapter_urls = response.xpath('//div[@class="clearfix dirconone"]/li/a/@href').extract()
        for chapter_url in chapter_urls:
            yield scrapy.Request(chapter_url, callback=self.parse_content)

    # 第四步：获取小说名字,章节的名字和内容
    def parse_content(self, response):
        # 小说名字
        name = response.xpath('//div[@class="main-index"]/a[@class="article_title"]/text()').extract_first()

        result = response.text
        # 小说章节名字
        chapter_name = response.xpath('//strong[@class="l jieqi_title"]/text()').extract_first()
        # 小说章节内容
        chapter_content_reg = r'style5\(\);</script>(.*?)<script type="text/javascript">'
        chapter_content_2 = re.findall(chapter_content_reg, result, re.S)[0]
        chapter_content_1 = chapter_content_2.replace('    ', '')
        chapter_content = chapter_content_1.replace('<br />', '')

        item = XiaoshuoItem()
        item['name'] = name
        item['chapter_name'] = chapter_name
        item['chapter_content'] = chapter_content
        yield item