#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-08-21 17:08:29  

import scrapy

class LabSpider(scrapy.Spider):
    name = 'lab2'                                       
    allowed_domains = ['http://lab.scrapyd.cn/'] 
    start_urls  = [ 
        'http://lab.scrapyd.cn/page/1/',
        'http://lab.scrapyd.cn/page/2/'
    ]  
    
    def parse(self, response):
        mingyan = response.css('div.quote')
        for v in mingyan:
            text = v.css('.text::text').extract_first()       # 提取名言
            autor = v.css('.author::text').extract_first()    # 提取作者
            tags = v.css('.tags .tag::text').extract()        # 提取标签
            tags = ','.join(tags)  # 数组转换为字符串
            
            """
            接下来进行写文件操作，每个名人的名言储存在一个txt文档里面
            """
            fileName = '%s-语录.txt' % autor    # 爬取的内容存入文件，文件名为：作者-语录.txt
            f = open(fileName, "a+")            # 追加写入文件
            f.write(text)                       # 写入名言内容
            f.write('\n')                       # 换行
            f.write('标签：'+tags)               # 写入标签
            f.close()                           # 关闭文件操作