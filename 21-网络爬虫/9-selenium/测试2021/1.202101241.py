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

#声明浏览器对象初始化
browser = webdriver.Chrome()

try:
    # 访问页面
    browser.get('http://www.baidu.com')
    #查找节点
    input = browser.find_element_by_id('kw')
    #节点交互
    input.send_keys('基金')
    #节点交互
    input.send_keys(Keys.ENTER)
    #显示等待
    wait = WebDriverWait(browser,5)    
    wait.until(EC.presence_of_element_located((By.ID,'content_left')))
    #打印当前的URL
    print(browser.current_url)
    #打印cookies
    print(browser.get_cookies())
    #打印页面源码
    print(browser.page_source)

finally:
    #关闭浏览器对象
    browser.close()