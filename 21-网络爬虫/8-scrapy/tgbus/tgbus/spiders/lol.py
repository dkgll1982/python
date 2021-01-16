import scrapy
from ..items import TgbusItem 
#爬取巴士lol的英雄美图：https://www.cnblogs.com/xiaozx/p/10776694.html

class LolSpider(scrapy.Spider):
    name = 'lol'
    allowed_domains = ['lol.tgbus.com']
    start_urls = ['http://lol.tgbus.com/tu/yxmt/']

    def parse(self, response):
        li_list = response.xpath('//div[@class="list cf mb30"]/ul//li')
        for one_li in li_list:
            item = TgbusItem()
            item['image_urls'] =one_li.xpath('./a/img/@src').extract()
            yield item
