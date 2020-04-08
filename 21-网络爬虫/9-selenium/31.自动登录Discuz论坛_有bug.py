#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-04-07 21:30:39 
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

class DiscuzSpider():
    def __init__(self):
        super().__init__()
        self.host = 'https://www.discuz.net'
        self.login_url = parse.urljoin(self.host, '/forum.php') 
        self.username = 'dkglll'            #用户名
        self.pwd = 'tggc1234'               #密码
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver,20)
        self.base_dir = r'backup/爬虫/验证码/'
        self.path = ''
        self.headers = {
            "referer":self.login_url, 
            "accept":"image/webp,image/apng,image/*,*/*;q=0.8",
            "sec-fetch-dest":'document', 
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "user_agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
        }

    #登录
    def login(self):
        #加载首页
        self.driver.get(self.login_url)
        
        #点击登录链接
        login_btn = self.driver.find_element_by_css_selector("button.pn.vm")
        login_btn.click()
        
        #延时等待直到弹窗加载完成
        self.wait.until(EC.presence_of_element_located((By.ID,"seccodeverify_cSA")))
        
        #表单输入框(用户名、密码、验证码)
        #注意：每次加载弹窗，id都会变化，但前缀不变，用模糊匹配方式查询
        input_username = self.driver.find_element_by_xpath("//input[starts-with(@id,'username')]")
        input_pwd = self.driver.find_element_by_xpath("//input[starts-with(@id,'password')]") 
        
        #input_username.send_keys(self.username)
        #input_pwd.send_keys(self.pwd)
        
        input_code = self.driver.find_element_by_id("seccodeverify_cSA")  
        code_src = self.driver.find_element_by_xpath("//span[@id='vseccode_cSA']/img[@class='vm']").get_attribute('src')
       
        path = parse.urljoin(self.host,code_src)
        print(path) 
        
        while True:
            # 此处的坑：未解决验证码每次图片请求cookies参数的问题，导致验证码不能识别
            #下载验证码图片(注意此处消息头)     
            response = self.send_request(parse.urljoin(self.host,code_src))
            if response:
                self.path = self.base_dir + 'code.png'
                self.write_content(response.content)
                print('验证码已下载到本地.')
            
            result = ''
            
            #1：人工输入验证码
            while True:
                result = input('请输入验证码：')
                if not result:
                    continue
                else:
                    break                   
        
            #输入验证码
            input_code.send_keys(result) 
            #切换焦点，获取验证码状态       
            input_username.send_keys(Keys.LEFT)
            time.sleep(2) 
            code_state = self.driver.find_element_by_xpath("//span[@id='checkseccodeverify_cSA']/img[@class='vm']").get_attribute('src')
            print(f'获取验证码状态{code_state}')
            #验证码不正确
            if not code_state.find('error') >=0 :
                break
            else:
                print('您输入的验证码不正确,重新获取验证码.')
                input_code.clear()
           
        # #提交
        # submit = self.driver.find_element_by_css_selector("button.pn.pnc")
        # submit.click()
        # time.sleep(1)

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
    discuz = DiscuzSpider()
    discuz.start()