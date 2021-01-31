#!/usr/bin/env python 
# -*- coding:utf-8 -*-  
# @Author: suixin 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd  
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2021-01-17 17:28:00 
# @Remark: Life is short, I use python！ 
# @Software: vscode 
# 参考链接：https://blog.csdn.net/u011781521/article/details/70210364?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.control
# 备注：CrawlSpider全站爬取

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from ..items import DoubanBook2Item
import re
import os
import urllib.request
from scrapy.http import HtmlResponse,Request
import time 
 
class BookspiderSpider(CrawlSpider): 
    name = 'books'
    allowed_domains = ['book.douban.com']
    start_urls = ['https://book.douban.com/tag/编程?start=0&type=T']
    rules = (
        # 列表页url
        Rule(LinkExtractor(allow=(r"https://book.douban.com/tag/编程\?start=\d+&type=T"))),
        # 详情页url
        Rule(LinkExtractor(allow=(r"https://book.douban.com/subject/\d+/$")),callback="parse_item")
    ) 
 
    def parse_item(self, response):   
        sel = Selector(response)
        item = DoubanBook2Item() 
        # 类别
        item["tags"] = "编程" 
        # 图书名
        item["name"] = sel.xpath("//div[@id='wrapper']/h1/span/text()").extract()[0].strip()
        # 读者评分
        item["score"] = sel.xpath("//div[@class='rating_self clearfix']/strong/text()").extract()[0].strip()
        # 详情页链接
        item["link"] = response.url  
        try:
            # 内容简介
            contents = sel.xpath("//div[@id='link-report']//div[@class='intro']")[-1].xpath(".//p//text()").extract()
            item["content_description"] = "\n".join(content for content in contents)
        except:
            item["content_description"] = "" 
 
        try:
            # 作者简介
            profiles = sel.xpath("//div[@class='related_info']//div[@class='indent ']//div[@class='intro']")[-1].xpath(".//p//text()").extract()
            item["author_profile"] = "\n".join(profile for profile in profiles)
        except:
            item["author_profile"] = "" 
 
        src = sel.xpath("//div[@id='mainpic']/a/img/@src").extract()[0].strip()
        print("images is url-----------------------------------------: " + src)
        file_name = "%s.jpg" % (item["name"])
        file_path = os.path.join(os.path.abspath(os.path.dirname(os.getcwd())), "img", file_name)
        print("file_name---****************************************-file_path---: " + file_name)
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        urllib.request.install_opener(opener)
        # urlretrieve()方法直接将远程数据下载到本地。
        urllib.request.urlretrieve(src, file_path)
        
        item["images"] = file_path
 
        datas = response.xpath("//div[@id='info']//text()").extract()
        datas = [data.strip() for data in datas]
        datas = [data for data in datas if data != ""] 
 
        for i, data in enumerate(datas):
            print ("index %d " % i, data) 
 
        for data in datas:
            if u"作者" in data:
                if u":" in data:
                    item["author"] = datas[datas.index(data) + 1]
                elif u":" not in data:
                    item["author"] = datas[datas.index(data) + 2]
            elif u"出版社:" in data:
                item["press"] = datas[datas.index(data) + 1]
            elif u"出版年:" in data:
                item["date"] = datas[datas.index(data) + 1]
            elif u"页数:" in data:
                item["page"] = datas[datas.index(data) + 1]
            elif u"定价:" in data:
                item["price"] = datas[datas.index(data) + 1]
            elif u"ISBN:" in data:
                item["ISBN"] = datas[datas.index(data) + 1] 
                
        return item