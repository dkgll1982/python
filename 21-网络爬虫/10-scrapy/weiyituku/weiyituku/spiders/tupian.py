#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-08-29 17:41:30 
# @Remark: 人生苦短，我用python！

import scrapy
from ..items import WeiyitukuItem
from scrapy import Spider
    
page_index = 0    
 
class TupianSpider(scrapy.Spider):
    name = 'tupian'
    allowed_domains = ['www.mmonly.cc']
    #起始链接：唯一图库美女图片
    start_urls = ['https://www.mmonly.cc/mmtp/list_9_38.html']
    
    #解析页面分类图片链接
    def parse(self, response):
        link_list = response.xpath("//div[@class='item_b clearfix']/div[@class='title']/span/a")
        for link in link_list:            
            href = link.xpath('./@href').extract_first()   
            if href:     
                #meta实现scrapy在Request之间传递参数    
                yield scrapy.Request(url = href, 
                                     callback = self.parse_detail, 
                                     meta = { "title" : link.xpath('./text()').extract_first()}               
                                    )
        #下一页
        next_page = response.xpath("//div[@id='pageNum']/a[contains(text(),'下一页')]/@href").extract_first()  
           
        #获取配置文件的参数：self.settings.get("XXXX")
        if next_page and page_index < self.settings.get("MAX_PAGE"):    #限制爬取的页数
            page_index = page_index + 1            
            yield scrapy.Request(url = response.urljoin(next_page),callback = self.parse) 
         
    #解析每一类图片的套图信息
    def parse_detail(self,response): 
        title = response.meta['title']
        item = WeiyitukuItem()
        item['title'] = title
        #获取到h1里的整个文本（含子节点标签的文本）
        item['name'] = response.xpath("string(//div[@class='wrapper clearfix imgtitle']/h1)").extract_first()   
        item['img_url'] = response.xpath("//div[@id='big-pic']/p/a/img/@src").extract_first()   
        yield item       
            
        #套图的下一张
        next_pic = response.xpath("//li[@id='nl']/a/@href").extract_first()
        if next_pic:
            yield scrapy.Request(url = response.urljoin(next_pic),
                                 meta = { "title" :title },
                                 callback = self.parse_detail)
