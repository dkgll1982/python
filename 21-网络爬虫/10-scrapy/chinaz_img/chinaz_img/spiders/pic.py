import scrapy
from ..items import ChinazImgItem
#参考链接：https://www.cnblogs.com/xiao-apple36/p/12623211.html

class PicSpider(scrapy.Spider):
    name = 'pic'
    allowed_domains = ['sc.chinaz.com']
    start_urls = ['http://sc.chinaz.com/tupian/']

    def parse(self, response):
        src_list = response.xpath('//div[@id="container"]/div')
        # print(src_list)
        for src_item in src_list:
            # 图片懒加载（当浏览器滑动到图片时src2属性变为src属性）
            # scrapy不会滑动到图片，所以使用src2属性（伪属性）
            src_content = src_item.xpath('./div/a/img/@src2').extract_first()
            print(src_content)
            item = ChinazImgItem()
            item['src'] = response.urljoin(src_content)

            yield item
            
        next_page = response.xpath('//a[@class="nextpage"]') 
        if next_page:
            url = next_page.xpath('@href').get()
            yield scrapy.Request(url = response.urljoin(url),callback = self.parse)
