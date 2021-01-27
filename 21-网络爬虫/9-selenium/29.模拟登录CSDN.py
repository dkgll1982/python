#!/usr/bin/env python 
# -*- coding:utf-8 -*-  
# @Author: suixin 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd  
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2021-01-25 14:15:23 
# @Remark: Life is short, I use python！ 
# @Software: vscode 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import os,time

url = 'https://home.51cto.com/index'
browser = webdriver.Chrome() 
browser.get(url)

browser.maximize_window()

span = browser.find_elements_by_xpath("//div[@class='btn_switch_group']/span")[0]

#动作链：单击“密码登陆”
ActionChainsDriver = ActionChains(browser).click(span)
ActionChainsDriver.perform()   

time.sleep(1)

userid= browser.find_element_by_id('loginform-username')
#用户名
userid.send_keys('dkgll')
pwd= browser.find_element_by_id('loginform-password')
#密码
pwd.send_keys('xxxxxxxx')

#点击“登录”
login = browser.find_element_by_name('login-button')
print(login)
ActionClickHold = ActionChains(browser).click(login)
ActionClickHold.perform()   
