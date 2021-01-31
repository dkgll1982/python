#参考链接（传智播客师资库信息爬取）：https://blog.csdn.net/fallwind_of_july/article/details/97246577

import scrapy
from itcastteacher.items import ItcastteacherItem

class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['www.itcast.cn/']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml#ajavaee']

    def parse(self, response):
        node_list = response.xpath("//div[@class='li_txt']")    #爬取的数据内容 
        
        for node in node_list:
            item = ItcastteacherItem()
            
            name = node.xpath("./h3/text()").extract()
            title = node.xpath("./h4/text()").extract()
            info = node.xpath("./p/text()").extract()

            item["name"] = name[0]
            item["title"] = title[0]
            item["info"] = info[0]
            
            #yield到item中，流式写入管道pipelines，源源不断的接受新数据直至无数据为止
            yield item                              
