# -*- coding: utf-8 -*-
# 参考链接：https://www.cnblogs.com/CYHISTW/p/11491513.html

import scrapy
from douban.items import DoubanItem

class DoubanSpiderSpider(scrapy.Spider):    
    # 爬虫的名称
    name = 'douban_spider'
    # 爬虫允许抓取的域名 爬取url都属于这个域名
    allowed_domains = ['movie.douban.com']
    # 爬虫抓取数据起始地址,给调度器
    start_urls = ['http://movie.douban.com/top250']

    # 默认的回调函数，负责处理response并返回处理的数据以及跟进的url
    # 该方法以及其他的Request回调函数必须返回一个包含Request或Item的可迭代对象
    def parse(self, response):
        movie_list = response.xpath("//div[@class='article']//ol[@class='grid_view']/li")
        for i_item in movie_list:
            douban_item = DoubanItem()
            douban_item['serial_number'] = i_item.xpath(".//div[@class='item']//em/text()").extract_first()
            douban_item['movie_name'] = i_item.xpath(".//div[@class='info']/div[@class='hd']/a/span[1]/text()").extract_first()
            descs = i_item.xpath(".//div[@class='info']//div[@class='bd']/p[1]/text()").extract()
            i_desc_str = ''
            for i_desc in descs:
                i_desc_str = i_desc_str + "".join(i_desc.split()) 
                
            #赋值
            douban_item['introduce'] = i_desc_str
            douban_item['star'] = i_item.xpath(".//span[@class='rating_num']/text()").extract_first()
            douban_item['evaluate'] = i_item.xpath(".//div[@class='star']//span[4]/text()").extract_first()
            douban_item['describle'] = i_item.xpath(".//p[@class='quote']/span/text()").extract_first()
            #我们需要把获取到的东西yield到douban_item中，否则我们的管道pipelines.py无法接收数据
            yield douban_item
            
        # 解析下一页
        next_link = response.xpath("//span[@class='next']/link/@href").extract()
        # 判断next_linkend是否存在
        if next_link:
            next_link = next_link[0]
            yield scrapy.Request("https://movie.douban.com/top250"+next_link,callback=self.parse)
