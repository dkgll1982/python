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

class Github2Spider(scrapy.Spider):
    name = 'github2'
    allowed_domains = ['github.com']
    # 登录URL
    start_urls = ['https://github.com/login'] 
    
    def parse(self, response):
        authenticity_token = response.xpath("//input[@name='authenticity_token']/@value").extract_first() 
        commit = response.xpath("//input[@name='commit']/@value").extract_first()
        
        #表单请求Form Data
        post_data = dict(
            login = "350606539@qq.com",
            password = "tggcTGGC1234" 
        )
        # 表单请求
        # 只能应用在form标签做的表单登录网站上，只关心输入账号和密码，名称按网页设计的标签名称填写。
        yield scrapy.FormRequest.from_response(
            response,                   #自动的从response中寻找from表单
            formdata = post_data,       #只需要传入字典型登录名和密码，字典的健是input标签中的name属性
            callback = self.after_login
        )

    #表单提交后的处理页面
    def after_login(self, response):
        with open(r"data/myhome2.html","w",encoding="utf8") as f:
            f.write(response.body.decode())
        print(re.findall("350606539", response.body.decode()))
