#!/usr/bin/env python 
# -*- coding:utf-8 -*-  
# @Author: suixin 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd  
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-09-03 18:57:08 
# @Remark: Life is short, I use python！
# 参考链接：https://www.jianshu.com/p/7c5d41c61ad2

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders.crawl import Rule, CrawlSpider

# LinkExtrator适用于整站爬取按照定义规则过滤提取链接
class Jianshu_CrawlSpider(CrawlSpider):
    name = 'jianshu_Crawl'
    allowed_domains = ['jianshu.com'] 

    # 起始页
    start_urls = ['https://www.jianshu.com/']
    
    domain = ['beian.gov.cn','shjbzx.cn','218.242.124.22:8081','12377.cn']    
    
    """
        设置各类过滤规则
        allow：这里用的是re过滤，我们其实就是start_urls加上我们这个匹配到的具体链接下的内容。 　  
        LinkExtractor：故名思议就是链接的筛选器，首先筛选出来我们需要爬取的链接。
    　　deny：这个参数跟上面的参数刚好想反，定义我们不想爬取的链接。
    　　follow：默认是false，爬取和start_url符合的url。如果是True的话，就是爬取页面内容所有的以start_urls开头的url。
    　　restrict_xpaths：使用xpath表达式，和allow共同作用过滤链接。还有一个类似的restrict_css 
    　　callback：定义我们拿到可以爬取到的url后，要执行的方法，并传入每个链接的response内容（也就是网页内容）
    """
    
    #link = LinkExtractor(deny_domains = domain)         
    link = LinkExtractor(allow='p/.+')         
    
    # Rule的第一个参数是LinkExtractor
    # 默认的回调函数也不再是parse，而是parse_item   
    rules = [ 
        Rule(link,callback='parse_items')
    ]     
     
    print('开始爬取-----------------')
    
    def parse_items(self, response):
        print('爬取的链接地址：',response.url)  
        item = {}
        return item