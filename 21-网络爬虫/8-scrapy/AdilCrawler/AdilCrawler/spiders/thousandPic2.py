# -*- coding: utf-8 -*-
import scrapy
from AdilCrawler.items import AdilcrawlerItem

# 导入 ItemLoader 功能类
from scrapy.loader import ItemLoader
# optimize  优化
# 爬虫项目优化

class thousandpic2Spider(scrapy.Spider):
    name = 'thousandPic2'                        #爬虫名称
    allowed_domains = ['www.58pic.com']
    start_urls = ['http://www.58pic.com/c/']

    def parse(self, response): 
        '''
        查看页面元素
         /html/body/div[4]/div[3]/div/a/p[2]/span/span[2]/text()
          因为页面中 有多张图，而图是以 /html/body/div[4]/div[3]/div[i]  其中i  为变量 作为区分的 ，所以为了获取当前页面所有的图
          这里 不写 i 程序会遍历 该 路径下的所有 图片。
        '''

        # 使用功能类 itemLoader,以取代 看起来杂乱的 extract() 和 xpath() ，优化如下
        i = ItemLoader(item = AdilcrawlerItem(),response = response )
        
        # author 作者
        i.add_xpath("author","//span[@class='usernameColor']/text()")
        # theme  主题
        i.add_xpath("theme","//span[@class='fl info-h1']/text()")  

        return i.load_item()