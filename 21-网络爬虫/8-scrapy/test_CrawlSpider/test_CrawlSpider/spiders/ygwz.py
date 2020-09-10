#!/usr/bin/env python 
# -*- coding:utf-8 -*-  
# @Author: suixin 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd  
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-09-03 20:13:38 
# @Remark: Life is short, I use python！
# 参考链接：https://blog.csdn.net/kingx3/article/details/108329847

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import TestCrawlspiderItem
import time

class YgwzSpider(CrawlSpider):
    name = 'ygwz'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/html/top/report.shtml']
    
    # rules是Rule的集合，每个rule规则同时执行。另外，如果发现web服务器有反爬虫机制如返回一个假的url，
    # 则可以使用Rule里面的参数process_links调用一个自编函数来处理url后返回一个真的url
    rules = (
        # 每个url都有一个独一无二的指纹，每个爬虫项目都有一个去重队列
        # Rule里面没有回调函数，则默认对匹配的链接要跟进，就是对匹配的链接在进行请求获取响应后对响应里面匹配的链接继续跟进，
        # 只不过没有回调函数对响应数据进行处理
        # Rule(LinkExtractor(allow="page="))如果设置为follow=False,则不会跟进，只显示当前页面匹配的链接。
        # 如设置为follow=True，则会对每个匹配的链接发送请求获取响应进而从每个响应里面再次匹配跟进，直至没有。
        # python递归深度默认为不超过1000，否则会报异常
        Rule(LinkExtractor(allow = "page=")),    
        Rule(LinkExtractor(allow = 'http://wz.sun0769.com/html/question/\d+/\d+.shtml'),callback = 'parse_item')
    )
    
    def parse_item(self, response):
        print(response.url)
        item = DongguanItem()
        item['url'] = response.url
        item['title'] = response.xpath('//div[@class="pagecenter p3"]//strong/text()').extract()[0]
        item['number'] = response.xpath('//div[@class="pagecenter p3"]//strong/text()').extract()[0].split(' ')[-1].split(':')[-1]
        # 对帖子里面有图片的处理，发现没有图片时则没有class="contentext"的div标签，以此作为标准获取帖子内容
        if len(response.xpath('//div[@class="contentext"]')) == 0:
            item['content'] = ''.join(response.xpath('//div[@class="c1 text14_2"]/text()').extract())
        else:
            item['content'] = ''.join(response.xpath('//div[@class="contentext"]/text()').extract())
        yield item