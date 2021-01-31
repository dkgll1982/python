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

class CsdnSpider(scrapy.Spider):
    name = 'login' 
    start_urls = ['https://passport.csdn.net/login?code=public']

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
        seleniumCookies = self.chrome.get_cookies()                
        cookies = {}
        # 获取cookie中的name和value,转化成requests可以使用的形式
        for cookie in seleniumCookies:
            cookies[cookie['name']] = cookie['value']
            
        print(f"seleniumCookies = {cookies}") 

    def closed(self,spider): 
        # 当爬虫结束之后，调用关闭浏览器方法
        print('爬虫整体结束，关闭浏览器！~~~~~~~~~~~~~~~~~~~')
        #self.chrome.quit()