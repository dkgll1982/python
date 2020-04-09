#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-04-09 13:26:19 
# @Remark: 人生苦短，我用python！

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import requests
from urllib import parse
import re
import random
import string 

class BilibiliSpider():
    def __init__(self):
        super().__init__()
        self.host = 'https://passport.bilibili.com'
        self.login_url = parse.urljoin(self.host, '/login') 
        self.username = '13667226055'       #用户名
        self.pwd = 'tggc1234'               #密码
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver,20)
        self.base_dir = r'backup/爬虫/验证码/'
        self.path = ''
        self.headers = { 
            "user_agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
        }

    #登录
    def login(self):
        #加载首页
        self.driver.get(self.login_url) 
         
        #表单输入框(用户名、密码、验证码)
        #注意：每次加载弹窗，id都会变化，但前缀不变，用模糊匹配方式查询
        input_username = self.driver.find_element_by_id("login-username")
        input_pwd = self.driver.find_element_by_id("login-passwd")
        
        input_username.send_keys(self.username)
        input_pwd.send_keys(self.pwd) 
           
        #提交登录
        submit = self.driver.find_element_by_css_selector("a.btn.btn-login")
        submit.click()
        time.sleep(1)

    #发送请求
    def send_request(self,url):
        response = requests.get(url,headers = self.headers)
        if response.status_code == 200:
            return response
        
    #写入文件    
    def write_content(self,content):
        with open(self.path,'wb') as f:
            f.write(content)
    #注销
    def louout(self): 
        pass
    
    def start(self):
        self.login()

if __name__ == "__main__":
    bilibilis = BilibiliSpider()
    bilibilis.start()