#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: suixin
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd
# @Site: https://user.qzone.qq.com/350606539/main
# @Date: 2021-01-20 15:13:38
# @Remark: Life is short, I use python！
# @Software: vscode
# 参考链接：https://www.cnblogs.com/ywjfx/p/11089248.html

import scrapy
import re 

class GithubSpider(scrapy.Spider):
    name = 'github'
    allowed_domains = ['github.com']
    # 登录URL
    start_urls = ['https://github.com/login']
    # 表单请求URL
    fromrequest_url = "https://github.com/session"
    
    def parse(self, response):
        authenticity_token = response.xpath("//input[@name='authenticity_token']/@value").extract_first() 
        commit = response.xpath("//input[@name='commit']/@value").extract_first()
        
        #表单请求Form Data
        post_data = dict(
            login = "350606539@qq.com",
            password = "tggcTGGC1234",
            utf8 = '✓',
            authenticity_token = authenticity_token,
            commit = commit,
        )
        # 表单请求
        yield scrapy.FormRequest(url = fromrequest_url,formdata = post_data,callback = self.after_login)

    #表单提交后的处理页面
    def after_login(self, response):
        with open(r"data/myhome.html","w",encoding="utf8") as f:
            f.write(response.body.decode())
        print(re.findall("350606539", response.body.decode()))
