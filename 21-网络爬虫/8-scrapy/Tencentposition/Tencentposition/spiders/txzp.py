# -*- coding: utf-8 -*-
# 参考链接：https://www.cnblogs.com/xinyangsdut/p/7628770.html
# 注意：已不能运行，该页面是js渲染的，无法爬取

import scrapy
from ..items import TencentpositionItem
 
class TxzpSpider(scrapy.Spider):
    """
    功能：爬取腾讯社招信息
    """
    # 爬虫名
    name = "tencentPosition"
    # 爬虫作用范围
    allowed_domains = ["tencent.com"]
    url = "https://careers.tencent.com/search.html?index="
    offset = 2
    # 起始url
    start_urls = [url + str(offset)]

    def parse(self, response): 
        print(response.text)
        for each in response.xpath("//div[@class='recruit-list']"): 
            # 初始化模型对象
            item = TencentpositionItem()
            # 职位名称
            item['positionname'] = each.xpath("./a[@class='recruit-list-link']/h4[@class='recruit-title']/text()").extract()[0]
            # 详情连接
            item['positionlink'] = each.xpath("./a[@class='recruit-list-link']/p[@class='recruit-text']/text()").extract()[0]
            # 职位类别
            item['positionType'] = each.xpath("./a[@class='recruit-list-link']/p[@class='recruit-tips']/span[3]/text()").extract()[0]
            # 招聘人数
            item['peopleNum'] =  0
            # 工作地点
            item['workLocation'] = each.xpath("./a[@class='recruit-list-link']/p[@class='recruit-tips']/span[2]/text()").extract()[0]
            # 发布时间
            item['publishTime'] = each.xpath("./a[@class='recruit-list-link']/p[@class='recruit-tips']/span[4]/text()").extract()[0]

            print('------------------------------->',item)
            yield item

        # if self.offset < 1680:
        #     self.offset += 10

        # # 每次处理完一页的数据之后，重新发送下一页页面请求
        # # self.offset自增10，同时拼接为新的url，并调用回调函数self.parse处理Response
        # yield scrapy.Request(self.url + str(self.offset), callback = self.parse)
