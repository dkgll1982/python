# -*- coding: utf-8 -*-
# 参考链接：https://blog.csdn.net/qq_41151659/article/details/102779714

import scrapy
from pyquery import PyQuery 
from scrapy.http import Request
from city58.items import City58Item

class City58TestSpider(scrapy.Spider):
    name = 'city58_test'
    allowed_domains = ['58.com']
    start_urls = ['http://bj.58.com/chuzu/']

    def parse(self, response):
        jpy = PyQuery(response.text)
        li_list = jpy('li.house-cell').items()
        for it in li_list:
            a_tag = it('div.des > h2 > a')
            item = City58Item()
            item['name'] = a_tag.text()
            item['url'] = a_tag.attr('href')
            item['price'] = it('div.money > b').text()
            
            #使用response.follow方法把“/chuzu/pn2/”这个相对路径转换为绝对路径，并回调parse()函数
            test_request = response.follow('/chuzu/pn2/', callback=self.parse)   
            test_request2 = Request('http://bj.58.com/chuzu/pn3/',
                                    callback=self.parse,
                                    errback=self.error_back,    #调用异常函数
                                    cookies={},                 #cookie设为空
                                    headers={},                 #headers设为空
                                    priority=10
                                    )
            test_request3 = Request('http://58.com',
                                    callback=self.parse,
                                    errback=self.error_back,    #调用异常函数
                                    priority=10,                #优先级设为10
                                    meta={'dont_redirect': True}#不用重定向
                                    )
            test_request4 = Request('http://58.com',
                                    callback=self.parse,
                                    errback=self.error_back,
                                    priority=10,
                                    # meta={'dont_redirect': True}
                                    dont_filter=True            #对url不过滤
                                    )
            yield item
            yield test_request
            yield test_request2
            yield test_request3
            yield test_request4

    def error_back(self, e):
        _ = self
        print(e)  #打印异常信息
