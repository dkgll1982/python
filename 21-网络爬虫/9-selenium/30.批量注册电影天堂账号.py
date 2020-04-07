#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-04-07 19:41:52 
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

class BtJiaSpider():
    def __init__(self):
        super().__init__()
        self.host = 'http://www.2btjia.com'
        self.regist_url = parse.urljoin(self.host,'/user-create.htm')   #注册URL
        self.login_url = parse.urljoin(self.host,'/user-login.htm')     #登陆URL
        self.logout_url = parse.urljoin(self.host,'/user-logout.htm')   #注销URL
        self.headers = {
            
        }
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver,30)
        self.driver.maximize_window()
        self.email = ''                 #邮箱
        self.username = ''              #用户名
        self.pwd = ''                   #密码
    
    #生成隨機字符串
    def random_str(self,min,max):
        return ''.join(random.sample(string.ascii_letters + string.digits, random.randint(min,max)))
    
    #生成随机用戶信息
    def set_data(self):
        mail_type = ['qq.com','sina.com','163.com','sohu.com','263.com','139.com','126.com','189.com','hotmail.com','21cn.com','gmail.com','aliyun.com']    
        self.email = self.random_str(5,9) + '@' + mail_type[random.randint(0,11)]
        self.username = self.random_str(8,16)
        self.pwd = self.random_str(8,14) 
        
    #注册
    def regist(self): 
        #请求注册
        self.driver.get(self.regist_url)  
        #元素可见时，再进行后续操作
        self.wait.until(EC.visibility_of_element_located((By.ID,"create_email"))) 
 
        self.set_data()
        
        # #发送表单数据
        input_email = self.driver.find_element(By.ID,"create_email")
        input_username = self.driver.find_element(By.ID,"create_username")
        input_pwd = self.driver.find_element(By.ID,"create_password")
        input_re_pwd = self.driver.find_element(By.ID,"create_password2")
        
        input_email.send_keys(self.email)
        input_username.send_keys(self.username)
        input_pwd.send_keys(self.pwd)
        input_re_pwd.send_keys(self.pwd)
        
        time.sleep(1)
        #提交
        submit = self.driver.find_element(By.ID,"create_submit_ajax")
        submit.click() 
        time.sleep(1)
        
    #登陸    
    def login(self):        
        #请求首页
        self.driver.get(self.login_url)
        #元素可见时，再进行后续操作
        self.wait.until(EC.visibility_of_element_located((By.ID,"login_email"))) 
        
        #发送表单数据
        userid = self.driver.find_element(By.ID,"login_email")
        passwd = self.driver.find_element(By.ID,"login_password")
        userid.send_keys(self.username)
        passwd.send_keys(self.pwd)
        time.sleep(1)
        #提交
        submit = self.driver.find_element(By.ID,"login_submit_ajax")
        submit.click() 
        time.sleep(1)
        
    #注销    
    def logout(self):        
        #请求首页
        self.driver.get(self.logout_url) 
        #元素可见时，再进行后续操作
        self.wait.until(EC.element_to_be_clickable((By.ID,"logout_submit"))) 
        #退出
        out = self.driver.find_element(By.ID,"logout_submit")
        out.click()
        time.sleep(1)
                
    def start(self):
        #批量注册
        for x in range(10):
            try:
                self.regist()
                print(f"账号{x+1}-{self.username}注册成功！")
            except Exception as e:
                pass
            
        self.logout() 
        print(f"账号{self.username}已注销！")
        self.login()
        print(f"账号{self.username}登录成功！")
        
        #滚动到底部
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        time.sleep(10)
        self.driver.quit()
        
if __name__ == "__main__":
    bts = BtJiaSpider()
    bts.start()
    