#!/usr/bin/env python 
# -*- coding:utf-8 -*-  
# @Author: suixin 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd  
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2021-01-27 15:33:15 
# @Remark: Life is short, I use python！ 
# @Software: vscode 
# 备注：模拟登录基层治理平台

import scrapy
from scrapy import signals
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['huzhou-jczl-cx.spacecig.com']
    start_urls = ['http://huzhou-jczl-cx.spacecig.com/zhzl-frames/main.html']

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(LoginSpider, cls).from_crawler(crawler, *args, **kwargs)
        # 设置不加载图片
        prefs = {
            "profile.managed_default_content_settings.images": 2
        }
        chrome_option  = Options()
        chrome_option.add_experimental_option("prefs", prefs)
        # 声明webdriver对象给LoginSpider，可以全局使用
        spider.chrome = webdriver.Chrome(chrome_options = chrome_option) 
        crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
        return spider 
    
    #传递信号到spider_closed方法，关闭浏览器对象 
    def spider_closed(self,spider):
        print('爬虫结束了~~~')
        spider.chrome.quit()
    
    def parse(self, response):
        cookies = response.request.cookies
        print('返回请求结果：',cookies)
