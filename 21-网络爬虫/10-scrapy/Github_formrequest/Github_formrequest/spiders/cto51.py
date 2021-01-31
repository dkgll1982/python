#!/usr/bin/env python 
# -*- coding:utf-8 -*-  
# @Author: suixin 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd  
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2021-01-20 20:48:20 
# @Remark: Life is short, I use python！ 
# @Software: vscode 
# 参考链接（scrapy模拟登录github和51cto）：https://blog.51cto.com/haoyonghui/2140888
# 备注：暂未测试

import scrapy
from scrapy.http import FormRequest,Request
from ..items import CtoItem

class Login2Spider(scrapy.Spider):
    name = 'login2'
    allowed_domains = ['51cto.com']
    #start_urls = ['http://51cto.com/']

    def start_requests(self):
        urls = ['http://home.51cto.com/index']
        for url in urls:
            yield Request(url,callback=self.cto_login,meta={'cookiejar':1})

    def cto_login(self,response):
        csrf = response.xpath("//input[@name='_csrf']/@value").extract_first()
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language':'zh-CN,zh;q=0.9',
            'Accept-Encoding':'gzip, deflate',
            'Referer':'http://www.51cto.com/',
            'Content-Type':'text/html; charset=UTF-8'
        }
        self.logger.info("获取csrf值为 %s" % csrf)
        yield FormRequest.from_response(response,url='https://blog.51cto.com/haoyonghui?type=1',headers=headers,meta={'cookiejar': response.meta['cookiejar']},formdata={
            'LoginForm[username]':'aaaaaaa@qq.com',
            'LoginForm[password]':'xxxxxx',
            'LoginForm[rememberMe]':'0',
            '_csrf': csrf,
            },callback=self.after_login,dont_click=True,
        )

    def after_login(self,response):
        item = CtoItem()
        #item = {}
        resps = response.css('ul.artical-list li')
        for resp in resps:
            # 写入item字段中
            item['title_url'] = resp.css("a.tit::attr(href)").extract_first()
            item['title'] = resp.css("a.tit::text").extract_first().strip()
            # fullname的格式为“[名称]（链接）”之所以这样是因为
            # markdown语法里这个表示链接的意思，点击名称直接打开链接内容
            item['fullname'] = '[' + item['title'] + ']' + '(' + item['title_url'] + ')'
            # 此处logger也是调试使用
            print("###################")
            self.logger.info("title url的值为：%s , title的值为%s" % (item['title_url'], item['title']))
            yield item

        # 下一页内容获取
        next_page = response.css('li.next a::attr(href)').extract_first()
        # self.logger.info("下一页链接为：%s" % next_page)
        if next_page is not None:
            yield Request(next_page, callback=self.after_login)

    #def parse(self, response):
        #pass