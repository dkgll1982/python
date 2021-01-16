#!/usr/bin/env python 
# -*- coding:utf-8 -*-  
# @Author: suixin 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd  
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2021-01-11 14:17:51 
# @Remark: Life is short, I use python！ 
# @Software: vscode 

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import ZolBizhi2Item
 
# CrawlSpider是爬取那些具有一定规则网站的常用的爬虫，它基于Spider并有一些独特属性 
class ZoldeskSpider(CrawlSpider):
    name = 'zoldesk'
    # allowed_domains = ['desk.zol.com.cn']
    start_urls = ['http://desk.zol.com.cn/fengjing/1920x1080/']
    front_url = "http://desk.zol.com.cn"
    num = 1
 
    rules = (
        # 1.解决翻页
        Rule(LinkExtractor(allow=r'/fengjing/1920x1080/[0-1]?[0-9]?.html'), callback='parse_album', follow=True),
        # 2.进入各个图库的每一张图片页
        Rule(LinkExtractor(allow=r'/bizhi/d+_d+_d+.html', restrict_xpaths=("//div[@class='main']/ul[@class='pic-list2  clearfix']/li", "//div[@class='photo-list-box']")), follow=True),
        # 3.点击各个图片1920*1080按钮，获得html
        Rule(LinkExtractor(allow=r'/showpic/1920x1080_d+_d+.html'), callback = 'get_img', follow=True),
    )
    
    def parse_album(self, response): 
        # 备注：（2021/1/11）该方法缺少定义，需要进行补充        
        item = ZolBizhi2Item()
        images= response.xpath("//a[@class='pic']/img")
        for img in images: 
            item['image_urls'] = [img.xpath("@src").get()]
            item['image_title'] = img.xpath("@title").get()
            yield item
    
    def get_img(self, response):
        item = ZolBizhi2Item()
        item['image_urls'] = response.xpath("//body/img[1]/@src").extract_first()
        item['image_title'] = str(self.num)
        self.num += 1
        yield item