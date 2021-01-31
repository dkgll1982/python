#!/usr/bin/env python 
# -*- coding:utf-8 -*-  
# @Author: suixin 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd  
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2021-01-18 11:04:37 
# @Remark: Life is short, I use python！ 
# @Software: vscode 
# 备注：演示爬取四季植物网的草本植物类信息

import scrapy
from scrapy.http import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import CrawlSjwzItem

class SjwzSpider(CrawlSpider):
    name = 'Sjwz' 
    allowed_domains = ['sjwz.cn']
    host = "https://www.sjwz.cn/caoben"
    start_urls = ['https://www.sjwz.cn/caoben/p1.html']
    # 自动生成的文件不需要改东西，只需要添加rules文件里面Rule角色就可以
    # 每一页匹配规则
    Link = LinkExtractor(allow=(r"sjwz.cn/caoben/p\d+.html"))
    # 详情页匹配规则
    Link_detail = LinkExtractor(allow=(r"sjwz.cn/caoben/\w+/"))
    rules = (
        # 没有回调函数，说明follow是True
        Rule(Link, callback='parse_item',follow=True),
        # 有回调函数，说明follow是False
        #Rule(Link_detail, callback='parse_detail'),
    ) 
    
    def parse_item(self, response):
        li_list = response.xpath("//div[@class='main-images-list clearfix']/ul/li")
        for li in li_list:
            item = CrawlSjwzItem()
            # 所在索引页
            item["pindex"] = response.url.split('/')[-1].replace('.html','')
            # 植物名称
            item['name'] = li.xpath('./a/p/text()').get()
            # 植物介绍
            item['image'] = response.urljoin(li.xpath('./a/img/@src').get())    
                  
            url = response.urljoin(li.xpath('./a/@href').get())
            yield Request(url = url,callback = self.parse_detail,meta ={"item":item})        
    
    def parse_detail(self, response):
        item = response.meta['item']  
        item["link"] = response.url
        # 植物介绍
        item['content'] = response.xpath("//div[@class='special-text']/p/text()").get()
        return item
