import scrapy

from scrapy.http import Request
from ..items import MeishiItem

class ZhanSpider(scrapy.Spider):
    name = 'meishi'
    allowed_domains = ['meishij.net']
    url = 'https://www.meishij.net/china-food/caixi/chuancai/'
    start_urls = [url]
    

    def parse(self, response): 
        img_list = response.xpath("//div[@class='listtyle1']/a/img")                                   
        for img in img_list:
            item = MeishiItem()
            item['title'] = img.xpath('@alt').get()
            item['src'] = [img.xpath('@src').get()]
            yield item
            
        #爬取多页    
        for index in range(2,11):
            yield Request(url = f"{self.url}?&page={index}",callback = self.parse)
            