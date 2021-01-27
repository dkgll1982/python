#!/usr/bin/env python 
# -*- coding:utf-8 -*-  
# @Author: suixin 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd  
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2021-01-26 21:19:56 
# @Remark: Life is short, I use python！ 
# @Software: vscode 

import scrapy
from scrapy import signals
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class GuaziSpider(scrapy.Spider):
    name = 'guazi'
    allowed_domains = ['guozi.com']
    start_urls = ['https://www.guazi.com/wh/buy']
    
    def __init__(self):
        super().__init__()
        # chrome浏览器的options参数：https://blog.csdn.net/xc_zhou/article/details/82415870
        chrome_options = Options()
        chrome_options.add_argument('--headless')       #使用无头谷歌浏览器模式
        chrome_options.add_argument('--disable-gpu')    #不加载gpu，规避bug
        chrome_options.add_argument('--no-sandbox')     #no-sandbox 取消沙盒模式
        #给GuaziSpider添加webdriver对象
        self.browser = webdriver.Chrome(chrome_options=chrome_options)

    def parse(self, response):
        #print(response.text)
        pass
    
    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(GuaziSpider, cls).from_crawler(crawler, *args, **kwargs)
        
        #在此处添加webdriver对象或者在__init__方法里添加都可以
        #spider.browser = webdriver.Chrome()
        crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
        return spider 

    def spider_closed(self, spider):
        print('爬虫结束了~~~')
        spider.browser.quit()
        spider.logger.info('Spider closed: %s', spider.name)