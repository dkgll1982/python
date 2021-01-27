#!/usr/bin/env python 
# -*- coding:utf-8 -*-  
# @Author: suixin 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd  
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2021-01-24 17:59:16 
# @Remark: Life is short, I use python！ 
# @Software: vscode 

from selenium import webdriver
from selenium.webdriver.common.by import  By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
import time

#声明浏览器对象初始化
browser = webdriver.Chrome()

try:
    # 访问页面
    browser.get('http://www.baidu.com')
     
    #搜索框 
    input = browser.find_element_by_id('kw')
    input.send_keys('美女')
    #"百度一下"按钮
    button = browser.find_element_by_id('su')
    #声明动作链对象
    action = ActionChains(browser)
    
    action.click(button)
    action.perform()
    
    #登录按钮
    login_btn = browser.find_element_by_xpath("//div[@id='u']/a[@class='lb']")
    
    time.sleep(3)
    #点击登录
    login_btn.send_keys(Keys.ENTER)
    
    time.sleep(10)
finally:
    #关闭浏览器对象
    browser.close()