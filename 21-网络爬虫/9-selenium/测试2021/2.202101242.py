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
import time

#声明浏览器对象初始化
browser = webdriver.Chrome()

try:
    # 访问页面
    browser.get('http://www.baidu.com')
     
    input1 = browser.find_element_by_id('lg')
    input2 = browser.find_element_by_css_selector('div#lg')
    input3 = browser.find_element_by_xpath("//div[@id='lg']") 
    input4 = browser.find_element_by_name('mp')
    input5 = browser.find_element_by_class_name('main') 
    print(input1,'\r\n',input2,'\r\n',input3,'\r\n',input4,'\r\n',input5,'\r\n',input5.get_attribute('class'),'\r\n',input5.text) 
    
    #browser.execute_script("window.alert('这是一个测试Alert弹窗');")   
    time.sleep(1)
    browser.execute_script('window.open("http://www.taobao.com")')

finally:
    #关闭浏览器对象
    browser.close()