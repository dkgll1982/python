# -*- coding: utf-8 -*-
# 參考：https://www.cnblogs.com/Kctrina/p/9523553.html
# 参考：https://blog.csdn.net/qq_24076135/article/details/78319055
 
import scrapy
from lxml import etree
import requests
from image699pic.items import Img699PicItem 
from urllib import parse

class A699picSpider(scrapy.Spider):
    name = 'a699pic'
    allowed_domains = ['699pic.com']
    start_urls = ['http://699pic.com/image/1/']
    headers = {
        'host': '699pic.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
    }

    def parse(self, response):
        divs = response.xpath("//div[@class='special-list clearfix']/div")[0:4]
        for div in divs:
            category = div.xpath("./a[@class='special-list-title']//text()").get().strip()
            url = div.xpath("./a[@class='special-list-title']/@href").get().strip()
            url = parse.urljoin('http:',url)
            image_urls = self.parse_url(url)    
            item = Img699PicItem(category = category, image_urls = image_urls)
            yield item

    def parse_url(self, url):
        response = requests.get(url =  url, headers = self.headers)
        htmlElement = etree.HTML(response.text)
        image_urls = [parse.urljoin('http:',item) 
                      for item in htmlElement.xpath("//div[@class='imgshow clearfix']//div[@class='list']/a/img/@src")]
        return image_urls
