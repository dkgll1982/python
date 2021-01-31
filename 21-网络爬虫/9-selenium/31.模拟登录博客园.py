#!/usr/bin/env python 
# -*- coding:utf-8 -*-  
# @Author: suixin 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd  
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2021-01-25 15:21:21 
# @Remark: Life is short, I use python！ 
# @Software: vscode 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

url = 'https://account.cnblogs.com/signin?returnUrl=https:%2F%2Fwww.cnblogs.com%2F'
browser = webdriver.Chrome()
browser.get(url)

#用户名
userid = browser.find_element_by_id('mat-input-0')
#密码
pwd = browser.find_element_by_id('mat-input-1')
userid.send_keys('dkgll')
pwd.send_keys('tggc6496')

#登录按钮
button = browser.find_element_by_xpath("//button[@class='mat-focus-indicator action-button ng-tns-c140-2 mat-flat-button mat-button-base mat-primary']")
button.send_keys(Keys.ENTER)

#目前登录之后会弹出一个九宫格的验证码弹窗，无法直接登录