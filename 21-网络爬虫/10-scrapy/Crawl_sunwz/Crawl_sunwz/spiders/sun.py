#!/usr/bin/env python 
# -*- coding:utf-8 -*-  
# @Author: suixin 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd  
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2021-01-18 22:37:24 
# @Remark: Life is short, I use python！ 
# @Software: vscode 
# 参考链接：https://www.cnblogs.com/xiao-apple36/p/12640260.html
# 下面的案例注意使用了两个item类，因为数据不在同一页面获取，而CrawlSpider不可以请求传参，所以将不同页面的数据使用了两item类收集。

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import SunproItem,DetailproItem

# 爬取sun网站中的编号,标题,内容
class SunSpider(CrawlSpider):
    name = 'sun'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/political/index/politicsNewest?id=1&page=1']

    link = LinkExtractor(allow=r'id=1&page=\d+')                    # 标题链接提取器 根据指定规则(allow)指定提取
    # http://wz.sun0769.com/political/politics/index?id = 449762
    link_detail = LinkExtractor(allow=r'/politics/index\?id=\d+')   # 详情页链接提取器 根据指定规则(allow)指定提取
    rules = (
        # 规则解析器：将链接提取器提取到的链接进行指定规则(callback)解析操作
        Rule(link, callback='parse_item', follow=True),
        # follow=True 链接提取器循环提取 
        Rule(link_detail, callback='parse_detail')
    )

    def parse_item(self, response):
        news_list = response.xpath('//ul[@class="title-state-ul"]/li')
        for new_item in news_list:
            new_num = new_item.xpath('./span[@class="state1"]/text()').extract_first()
            new_title = new_item.xpath('./span[@class="state3"]/a/text()').extract_first()
            item = SunproItem()
            item['new_num'] = new_num
            item['new_title'] = new_title 
            yield item

    def parse_detail(self, response):
        """
         新闻内容
        :param response:
        :return:
        """ 
        detail_item = DetailproItem()
        news_content = response.xpath('//div[@class="details-box"]/pre/text()').extract_first()
        detail_item['new_content'] = news_content 
        yield detail_item