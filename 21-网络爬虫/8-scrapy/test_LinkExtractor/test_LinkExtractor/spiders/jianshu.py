#!/usr/bin/env python 
# -*- coding:utf-8 -*-  
# @Author: suixin 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd  
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-09-03 18:57:08 
# @Remark: Life is short, I use python！
# 参考链接：https://www.jianshu.com/p/7c5d41c61ad2

import scrapy
from scrapy.linkextractors import LinkExtractor

# LinkExtrator适用于整站爬取按照定义规则过滤提取链接
class JianshuSpider(scrapy.Spider):
    name = 'jianshu'
    allowed_domains = ['jianshu.com'] 

    # 起始页
    start_urls = ['https://www.jianshu.com/']
     
    # 此处发现进不来，报“Rule without any user agent to enforce it on”或者“referer：none”需要设置heder    
    def parse(self, response):
        print('开始爬取-----------------')
        
        # rextract_links方法依据创建对象描述的提取规则在Response对象所包含的页面中提取链接，
        # 并返回一个列表，列表中每个元素都是一个Link对象，即提取到的一个链接。
        #link = LinkExtractor(restrict_xpaths='//ul[@class="note-list"]/li')
        
        pattern = 'https://www.jianshu.com/p/.+'
        
        #allow：接收一个正则表达式或一个正则表达式列表，提取绝对url于正则表达式匹配的链接，如果该参数为空，默认全部提取。        
        #link = LinkExtractor(allow=pattern)        
        
        # deny：接收一个正则表达式或一个正则表达式列表，
        # 与allow相反，排除绝对url于正则表达式匹配的链接，换句话说，就是凡是跟正则表达式能匹配上的全部不提取。
        #link = LinkExtractor(deny=pattern)     
           
        # allow_domains：接收一个域名或一个域名列表，提取到指定域的链接。
        domain = ['beian.gov.cn','shjbzx.cn','218.242.124.22:8081','12377.cn']
        #link = LinkExtractor(allow_domains = domain)      
        
        # deny_domains：和allow_doains相反，拒绝一个域名或一个域名列表，提取除被deny掉的所有匹配url。 
        #link = LinkExtractor(deny_domains = domain)      
        
        #restrict_css：和restrict_xpaths使用一样，只是使用规则不一样。
        link = LinkExtractor(restrict_css='ul.note-list > li')
        
        links = link.extract_links(response)
        if links:
            for index,link_one in enumerate(links,start=1):
                print(f"请求链接{index}:{link_one}")
