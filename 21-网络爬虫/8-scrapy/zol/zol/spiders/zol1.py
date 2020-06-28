#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-06-28 16:30:09 
# @Remark: 人生苦短，我用python！
# 参考：https://blog.csdn.net/weixin_43497769/article/details/106064419

import scrapy

class Zol1Spider(scrapy.Spider):
    name = 'zol1'
    allowed_domains = ['zol.com.cn']
    start_urls = ['http://desk.zol.com.cn/bizhi/265_1288_2.html']

    def parse(self, response):
        image_url = response.xpath('//img[@id="bigImg"]//@src').extract()
        image_name = response.xpath('string(//h3)').extract_first()
        yield {
            "image_urls": image_url,
            "image_name": image_name
        }
        next_url = response.xpath('//a[@id="pageNext"]/@href').extract_first()
        if next_url.find('.html') != -1:
            yield scrapy.Request(response.urljoin(next_url), callback=self.parse)
