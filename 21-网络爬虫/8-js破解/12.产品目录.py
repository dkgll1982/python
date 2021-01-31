#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-04-16 11:19:01 
# @Remark: 人生苦短，我用python！

import requests
import time
from urllib import parse
import random
import execjs
import sys
import os    

class MuLuSpider():
    def __init__(self):
        super().__init__() 
        self.url = 'http://www.300600900.cn/'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
        }
        self.path = r'backup/爬虫/cpml.html'
        
        with open(self.realpath('product.js'),encoding='utf-8') as f:
            jsdata = f.read() 
        ctx = execjs.compile(jsdata)
        #获取cookie
        self.cookie = ctx.eval('cookie')
        #获取重定向页面
        self.security_verify_data = ctx.eval('security_verify_data')
 
    def realpath(self,filename):
        return os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)
        
    def send_request(self):
        session = requests.session() 
        response = session.get(url = self.url,headers = self.headers)
        
        for item in self.cookie.split(';'):
            if "=" in item: 
                key,value = item.split('=')
                #把计算的cookie加入进来
                session.cookies.set(key,value) 
        #要去访问的页面
        full_ull = self.url + self.security_verify_data
        session.get(url = full_ull,headers = self.headers)
        
        #跳转到首页
        response = session.get(url = self.url,headers = self.headers)
        
        print(session.cookies)
        if response.status_code == 200:
            return response
        else:
            print(response.status_code)

    def write_content(self,content,path):
        with open(path,'wb') as f:
            f.write(content)
            
    def start(self):
        response = self.send_request()
        if response:
            self.write_content(response.content,self.path)
            
if __name__ == "__main__":
    mls = MuLuSpider()
    mls.start()