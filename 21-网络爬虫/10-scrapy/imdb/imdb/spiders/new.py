#!/usr/bin/env python 
# -*- coding:utf-8 -*-  
# @Author: suixin 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd  
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2021-01-11 15:52:57 
# @Remark: Life is short, I use python！ 
# @Software: vscode 
# 参考链接：https://blog.csdn.net/yancey_blog/article/details/53890884

from scrapy.spiders import CrawlSpider, Request, Rule
from ..items import ImdbItem
from scrapy.linkextractors import LinkExtractor 

class ImdbSpider(CrawlSpider):
    name = 'new'
    allowed_domains = ['www.imdb.cn']
    rules = (
        Rule(LinkExtractor(allow=r"/title/tt\d+$"), callback="parse_imdb", follow=True),
    )

    def start_requests(self):
        pages = []
        for i in range(1, 14616):
            url = "http://www.imdb.cn/nowplaying/" + str(i)
            yield Request(url=url, callback=self.parse)

    def parse_imdb(self, response):
        item = ImdbItem()
        item['url'] = response.url
        item['title'] = "".join(response.xpath('//*[@class="fk-3"]/div[@class="hdd"]/h3/text()').extract())
        pass
