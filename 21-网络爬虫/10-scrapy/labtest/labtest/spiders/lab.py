#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-08-21 17:08:29  

import scrapy

class LabSpider(scrapy.Spider):
    name = 'lab'                                       
    allowed_domains = ['http://lab.scrapyd.cn/'] 
    start_urls  = [ 
        'http://lab.scrapyd.cn/page/1/',
        'http://lab.scrapyd.cn/page/2/'
    ]  
    
    def parse(self, response):        
        page = response.url.split("/")[-2]    
        filename = 'mingyan-%s.html' % page   
        with open(filename, 'wb') as f:    
            f.write(response.body)            
        self.log('保存文件: %s' % filename)    
