# -*- coding: utf-8 -*-
# 参考：https://www.cnblogs.com/xiaozx/p/10776694.html

import scrapy
from xingantupian.items import xingantupianItem

class WzSpider(scrapy.Spider):
    name = 'xingan'
    allowed_domains = ['www.m131.cc']
    start_urls = ['http://www.m131.cc/xinggan/']

    def parse(self, response):
        every_html = response.xpath('//div[@class="main"]/dl//dd')
        for one_html in every_html[0:-1]:
            item = xingantupianItem()
            # 每个图片的链接
            link = one_html.xpath('./a/@href').extract_first()
            # 每个图片的名字
            title = one_html.xpath('./a/img/@alt').extract_first()
            item['title'] = title
            # 进入到每个标题里面
            request = scrapy.Request(url=link, callback=self.parse_one, meta={'item':item})
            yield request

    # 每个人下面的图集
    def parse_one(self, response):
        item = response.meta['item']
        # 找到总页数
        total_page = response.xpath('//div[@class="content-page"]/span[@class="page-ch"]/text()').extract_first()
        num = int(re.findall('(\d+)', total_page)[0])
        # 找到当前页数
        now_num = response.xpath('//div[@class="content-page"]/span[@class="page_now"]/text()').extract_first()
        now_num = int(now_num)
        # 当前页图片的url
        every_pic = response.xpath('//div[@class="content-pic"]/a/img/@src').extract()
        # 当前页的图片url
        item['image_urls'] = every_pic
        # 当前图片的refer
        item['referer'] = response.url
        yield item

        # 如果当前数小于总页数
        if now_num < num:
            if now_num == 1:
                url1 = response.url[0:-5] + '_%d'%(now_num+1) + '.html'
            elif now_num > 1:
                url1 = re.sub('_(\d+)', '_' + str(now_num+1), response.url)
            headers = {
                'referer':self.start_urls[0]
            }
            # 给下一页发送请求
            yield scrapy.Request(url=url1, headers=headers, callback=self.parse_one, meta={'item':item})
