#!/usr/bin/env python 
# -*- coding:utf-8 -*-  
# @Author: suixin 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd  
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2021-01-20 16:42:08 
# @Remark: Life is short, I use python！ 
# @Software: vscode 
# 备注：2021/01/20：暂未跑通

import scrapy
import re 
import urllib

class JczlSpider(scrapy.Spider):
    name = 'jczl'
    allowed_domains = ['huzhou-jczl-cx.spacecig.com']
    # 登录URL
    start_urls = ['http://huzhou-jczl-cx.spacecig.com/iam/saml/login']  
    # 表单请求URL
    fromrequest_url = "http://huzhou-jczl-cx.spacecig.com/iam/validate/validForPc"
    headers ={
          "Content-type":"application/json;charset=UTF-8",
          "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36"
      }

    def parse(self, response):         
        # 需要登录的账户和密码
        data = {"userid":"admin", "password":"DFYOPS1RrpdVlu2U"}    
        postdata = urllib.parse.urlencode(data).encode('utf8')

        # 表单请求
        yield scrapy.Request(
            url = self.fromrequest_url,
            headers = self.headers,
            body = postdata,
            callback = self.after_login
        )

    #表单提交后的处理页面
    def after_login(self, response):
        with open(r"data/myhome.html","w",encoding="utf8") as f:
            f.write(response.body.decode())
