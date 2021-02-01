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
from scrapy.linkextractors import LinkExtractor
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.common.exceptions import NoSuchElementException,TimeoutException  
from ..items import JczlItem

class LoginSpider(scrapy.Spider):
    offset = 0
    limit = 10
    total = 0
    name = 'login'
    allowed_domains = ['huzhou-jczl-cx.spacecig.com']
    start_urls = ['http://huzhou-jczl-cx.spacecig.com/zhzl-frames/main.html']
    #start_urls = ['http://huzhou-jczl-cx.spacecig.com/zhzlbackend/places/placeSafeCheck/pajczkForAdmin?offset=11&limit=10&orderby=&ordertype=&keyword=&departmentId=&placeStaffnum=&safeType=&controlLevel=&isKeyPlace=&placeKeyAttributeNum=&createStartDate=&createEndDate=&visitSit=&checkLevel=&visitStartDate=&visitEndDate=&checkIllegal=&placeAddress=&chargePerson=&chargePersonPhone=&chargePersonCardNum=&placeStatus=&isEvent=&isCheck=&isDishonest=&isPunished=&newCheckLevel=&gkdj=&createUser=&isFirm=&placeTypeAll=']
    api = 'http://huzhou-jczl-cx.spacecig.com/zhzlbackend/places/placeSafeCheck/pajczkForAdmin?offset={}&limit={}&orderby=&ordertype=&keyword=&departmentId=&placeStaffnum=&safeType=&controlLevel=&isKeyPlace=&placeKeyAttributeNum=&createStartDate=&createEndDate=&visitSit=&checkLevel=&visitStartDate=&visitEndDate=&checkIllegal=&placeAddress=&chargePerson=&chargePersonPhone=&chargePersonCardNum=&placeStatus=&isEvent=&isCheck=&isDishonest=&isPunished=&newCheckLevel=&gkdj=&createUser=&isFirm=&placeTypeAll='
    
    #2021/01/31：scrapyd部署时：spider 的init函数 需要改成 __init__(*args,**kwargs)
    def __init__(self,*args,**kwargs):
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
        self.cookies = {}
    
    def parse(self, response): 
        seleniumCookies = self.chrome.get_cookies()   
        # 获取cookie中的name和value,转化成requests可以使用的形式
        for cookie in seleniumCookies:
            self.cookies[cookie['name']] = cookie['value']
            
        print(f"登录cookies：{self.cookies}") 
        print('关闭浏览器！~~~~~~~~~~~~~~~~~~~')
        self.chrome.quit()
        
        #拿到cookies，请求接口
        yield scrapy.Request(url = self.api.format(0,self.limit),callback=self.parse_detail,cookies=self.cookies)
            
    def parse_detail(self, response):  
        result = response.json()   
        self.total = result['data']['total']
        for a in result['data']['rows']:
            item = JczlItem()
            item['id'] = a['id'] 
            item['placeName'] = a['placeName'] 
            item['oldPlaceName'] = a['oldPlaceName'] 
            item['oldPlaceName'] = a['oldPlaceName'] 
            item['placeAddr'] = a['placeAddr'] 
            item['areaName'] = a['areaName'] 
            item['safeType'] = a['safeType'] 
            item['placeTypeName'] = a['placeTypeName']  
            #print(item)
            yield item
        
        if int(self.total) > self.offset:
            self.offset += self.limit
            #拿到cookies，请求接口
            yield scrapy.Request(url = self.api.format(self.offset,self.limit),callback=self.parse_detail,cookies=self.cookies)
            
    def closed(self,spider): 
        # 当爬虫结束之后，执行的方法
        pass