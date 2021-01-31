#!/usr/bin/env python 
# -*- coding:utf-8 -*-  
# @Author: suixin 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd  
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2021-01-27 23:40:55 
# @Remark: Life is short, I use python！ 
# @Software: vscode 

import scrapy
from scrapy import signals
from scrapy.linkextractors import LinkExtractor
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.common.exceptions import NoSuchElementException,TimeoutException  
from ..items import Antispider1ScrapyItem
import time,os

class AntiSpider(scrapy.Spider):
    name = 'antispider1-1'

    start_urls = ['https://antispider1.scrape.center/']
                
    def __init__(self):
        # 浏览器实例化的操作只会被执行一次
        chrome_option  = Options()
        
        #chrome_option.add_argument('--headless')            # 无头，服务器上线时可加上，测试时可见比较好
        chrome_option.add_argument('--ignore-certificate-errors')  
        chrome_option.add_argument('--allow-insecure-localhost') 
        chrome_option.add_argument('--disable-infobars')     # 去掉提示：Chrome正收到自动测试软件的控制
        chrome_option.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_option.add_experimental_option('useAutomationExtension', False)
        chrome_option.add_argument('--start-maximized')      # 最大化运行（全屏窗口）,不设置，取元素会报错
        
        # 声明webdriver对象，可以全局使用
        self.chrome = webdriver.Chrome(chrome_options = chrome_option)    
        # 解决Webdriver Forbidden.反爬问题      
        self.chrome.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
            Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
            })"""
        })   
        
    def parse(self, response):
        # file_path = r'data'
        # if not os.path.exists(file_path):       # 判断是否存在该文件夹
        #     os.mkdir(file_path)                 # 不存在的话就创建一个
        # with open(os.path.join(file_path,'html.txt'),'w') as f:     #保存页面源码，测试用
        #     f.write(response.text)
            
        result = response.xpath('//div[@class="el-card item m-t is-hover-shadow"]')
        for a in result:
            item = Antispider1ScrapyItem()
            item['title'] = a.xpath('.//h2[@class="m-b-sm"]/text()').get()
            item['fraction'] = a.xpath('.//p[@class="score m-t-md m-b-n-sm"]/text()').get().strip()
            item['country'] = a.xpath('.//div[@class="m-v-sm info"]/span[1]/text()').get()
            item['time'] = a.xpath('.//div[@class="m-v-sm info"]/span[3]/text()').get()
            item['date'] = a.xpath('.//div[@class="m-v-sm info"][2]/span/text()').get()
            url = a.xpath('.//a[@class="name"]/@href').get()
            print('本次爬取的链接：',response.urljoin(url))
            yield scrapy.Request(url=response.urljoin(url),
                                 callback=self.parse_person,
                                 meta={'item': item} 
                                )
            
            #爬取下一页,此处写的不太好，应该判断
            for x in range(2,10):
                yield scrapy.Request(url = self.start_urls[0]+f'page/{x}',callback=self.parse)
            
    #获取详情页数据
    def parse_person(self, response):
        item = response.meta['item']
        print(item)
        item['director'] = response.xpath('//div[@class="directors el-row"]//p[@class="name text-center m-b-none m-t-xs"]/text()').get()
        yield item

    def closed(self,spider): 
        # 当爬虫结束之后，调用关闭浏览器方法
        print('爬虫整体结束，关闭浏览器！~~~~~~~~~~~~~~~~~~~')
        self.chrome.quit()