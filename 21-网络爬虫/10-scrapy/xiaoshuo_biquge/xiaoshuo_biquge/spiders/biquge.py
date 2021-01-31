#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-08-29 18:58:31 
# @Remark: 人生苦短，我用python！
# 参考链接1：https://blog.csdn.net/qq_42543264/article/details/88715113

import scrapy
from ..items import XiaoshuoBiqugeItem

class BiqugeSpider(scrapy.Spider):
    name = 'biquge'
    allowed_domains = ['xbiquge.la']
    start_urls = ['http://www.xbiquge.la/xiaoshuodaquan/']

    #解析主页全部小说，获取小说链接
    def parse(self, response):
        #主页所有小说的链接
        home_url = response.xpath("//div[@id='main']//ul//a/@href").extract()
        for home in home_url:
            url = home
            yield scrapy.Request(url=url, callback=self.parse2)
    
    #解析每一部小说的详细信息        
    def parse2(self, response):
        # item = XiaoshuoBiqugeItem()
        two_detail = response.xpath("//div[@id='wrapper']")
        for two in two_detail:
            # 获取小说名称
            title = two.xpath(".//div[@class='box_con']//div[@id='info']/h1/text()").extract_first()
            # print('###############################################')
            # print(title)
            # 获取小说作者
            author = two.xpath(".//div[@class='box_con']//div[@id='info']/p/text()").extract_first()
            # print('+++++++++++++++++++++++++++++++++++')
            # print(author_list)
            # 获取小说类型
            type = two.xpath(".//div[@class='con_top']/a[2]/text()").extract_first()
            # print(type)
            # 获取小说简介
            intro = two.xpath(".//div[@id='intro']/p[2]/text()").extract_first()
            # print(intro)
            # 获取小说封面
            cover = two.xpath(".//div[@id='sidebar']/div[@id='fmimg']/img/@src").extract_first()
            # print(image)
            # 获取小说最后更新时间
            turnover_time = two.xpath(".//div[@id='info']/p[3]/text()").extract_first()
            # print(turnover_time)
            # 获取小说章节目录
            section_title = two.xpath(".//div[@class='box_con']//dl//a/text()").extract()
 
            # item['title'] = title
            # item['author'] = author
            # item['type'] = type
            # item['intro'] = intro
            # item['cover'] = cover
            # yield item
            # 获取小说章节目录url
            section_url = two.xpath(".//div[@class='box_con']//dl//a/@href").extract()
            for section in section_url:
                url = 'http://www.xbiquge.la' + section
                yield scrapy.Request(url=url, callback=self.parse3)
    
    #获取每一章节的小说内容            
    def parse3(self, response):
            item = XiaoshuoBiqugeItem()
            # 获取每一章节目录名称
            section_title = response.xpath("//div[@class='box_con']/div[@class='bookname']/h1/text()").extract_first()
            item['section_title'] = section_title
            # 获取每一章节的章节内容
            section_lists = response.xpath("//div[@class='box_con']/div[@id='content']/text()").extract()
            # 设置一个空的字符串进行数据拼接
            section__ = ''
            for section_ in section_lists:
                section__ += section_
                section = re.sub(r"[\s+\.\!\/_,$%^*(+\"\')]+|[+——?【】？~@#￥%……&*]+|\\n+|\\r+|(\\xa0)+|(\\u3000)+|\\t", "", str(section__))
            item['section'] = section    
            return item