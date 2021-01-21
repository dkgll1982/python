#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: suixin
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd
# @Site: https://user.qzone.qq.com/350606539/main
# @Date: 2021-01-20 15:13:38
# @Remark: Life is short, I use python！
# @Software: vscode
# 参考链接（scrapy模拟登录github和51cto）：https://blog.51cto.com/haoyonghui/2140888

import scrapy
from scrapy.http import Request
from scrapy import FormRequest

class Github3Spider(scrapy.Spider):
    name = 'github3'
    allowed_domains = ['github.com']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://github.com/',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    start_urls = ['https://github.com/758109577']

    def start_requests(self):
        urls = ['https://github.com/login']
        for url in urls:
            yield Request(url, meta={'cookiejar': 1}, callback=self.github_login)

    def github_login(self, response):
        # 首先获取authenticity_token,这里可以借助scrapy shell ”url“来获取页面
        # 然后从源码中获取到authenticity_token的值
        authenticity_token = response.xpath("//input[@name='authenticity_token']/@value").extract_first()
        self.logger.info('authenticity_token=' + authenticity_token)

        data = {
            'utf8': '✓',
            'authenticity_token': authenticity_token,
            'login': "350606539@qq.com",
            'password': 'tggcTGGC1234'
        } 
        # url可以从fiddler抓取中获取,dont_click作用是如果是True，表单数据将被提交，而不需要单击任何元素。
        return FormRequest.from_response(
            response,
            url='https://github.com/session',
            meta={'cookiejar': response.meta['cookiejar']},
            headers=self.headers,
            formdata=data,
            callback=self.github_after,
            dont_click=True,
        )

    def github_after(self, response):
        with open(r"data/myhome3.html","w",encoding="utf8") as f:
            f.write(response.body.decode())
        # 获取登录页面主页中的字符串'dkgll'
        list = response.xpath("//div[@class='width-full text-bold']/a/@href").extract()
        # 如果含有字符串，则打印日志说明登录成功
        if 'dkgll1982' in list[0]:
            self.logger.info('我已经登录成功了，这是我获取的关键字：dkgll1982')

        for url in self.start_urls:
            yield Request(url=url, callback=self.show)

    def show(self, response):
        print("############################")
        list = response.xpath("//span[@class='p-nickname vcard-username d-block']/text()").extract()
        if '758109577' in list:
            print(list)
            print("############################")
        else:
            print("失败")
