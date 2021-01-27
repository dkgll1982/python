#!/usr/bin/env python 
# -*- coding:utf-8 -*-  
# @Author: suixin 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd  
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2021-01-18 22:52:49 
# @Remark: Life is short, I use python！ 
# @Software: vscode 
# 参考链接：https://blog.csdn.net/pcn01/article/details/106219763/

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule,logging
from ..items import WxappItem
 
class WxappSpiderSpider(CrawlSpider):
    name = 'wxapp'
    allowed_domains = ['wxapp-union.com']
    start_urls = ['http://www.wxapp-union.com/portal.php?mod=list&catid=2&page=1']
    rules = (
        # 匹配文章列表页分页url，follow=True表示爬取完第一页发现还有符合规则的url接着爬取
        Rule(LinkExtractor(allow = r'.+mod=list&catid=2&page=\d'),process_links='check_links'),
        # 匹配文件详情页url
            
        # allow参数没有必要写出要提取的url完整的正则表达式,部分即可,只要能够区别开来。
        # 且最重要的是,即使原网页中写的是相对url,通过LinkExtractor这个类也可以提取中绝对的url,这个类太厉害了。 
        Rule(LinkExtractor(allow = r'.+article-.+\.html'), callback = "parse_detail", follow = False, process_links='check_links'),
    )
    
    #对链接进行过滤处理
    def check_links(self, link):  
        return link
        
    def parse_detail(self, response):
        title = response.xpath('//h1/text()').get()
        authors = response.xpath('//p[@class="authors"]')
        author = authors.xpath('.//a/text()').get()
        pub_time = authors.xpath('.//span/text()').get()
        content = response.xpath('//td[@id="article_content"]//text()').getall()
        content = ''.join(content).strip()
        item = WxappItem(title = title, author = author, pub_time = pub_time, content = content)
        yield item
