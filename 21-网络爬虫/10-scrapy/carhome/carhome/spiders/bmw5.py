#参考链接：https://www.jianshu.com/p/9f26b2054dd8

import scrapy
from carhome.items import CarhomeItem

class Bmw5Spider(scrapy.Spider):
    name = 'bmw5'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/65.html#pvareaid=3454438']

    def parse(self, response):
        uiboxes = response.xpath("//div[@class='uibox']")[1:]
        for uibox in uiboxes:
            boxTitle = uibox.xpath(".//div[@class='uibox-title']/a/text()").get()
            urls = uibox.xpath(".//ul/li/a/img/@src").getall()
            urls = list(map(lambda url: response.urljoin(url), urls))
            item = CarhomeItem(boxTitle=boxTitle, image_urls=urls)
            yield item
