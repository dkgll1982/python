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
from selenium.webdriver.chrome.options import Options
import requests

import os,time
#移除Selenium中的 window.navigator.webdriver：https://www.cnblogs.com/presleyren/p/12936553.html

url = 'https://passport.csdn.net/login?code=public'
user_url ='https://i.csdn.net/#/user-center/profile'

options = webdriver.ChromeOptions()
options.add_argument('--disable-infobars')      # 去掉提示：Chrome正收到自动测试软件的控制
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--start-maximized')       # 最大化运行（全屏窗口）,不设置，取元素会报错

browser = webdriver.Chrome(options=options)

browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
  "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})
 
browser.get(url)  

#此处是有个登录选项的，我们需要先进行选择，此处选择'账号密码登录',接下来会弹出登陆输入框
a = browser.find_element_by_xpath("//div[@class='main-select']/ul/li[2]/a")
if a.text == '账号密码登录': 
  ActionClickHold = ActionChains(browser).click(a)
  ActionClickHold.perform()   

time.sleep(2)

userid= browser.find_element_by_id('all')
#用户名
userid.send_keys('dkgll')
pwd= browser.find_element_by_id('password-number')
#密码
pwd.send_keys('tggc123456789')

#点击“登录”
#在定位的class含有空格的复合类的解决办法:用CSS属性大法，就可以搞定：class=可以支持空格
login = browser.find_element_by_css_selector("[class='btn btn-primary']")

ActionClickHold = ActionChains(browser).click(login)
ActionClickHold.perform()   

#-----------------------------------------------------------------
#完成手工登录,再获取cookie
cookie = browser.get_cookies()
#print(cookie)

cookies = {}
# 获取cookie中的name和value,转化成requests可以使用的形式
for cookie in cookie:
    cookies[cookie['name']] = cookie['value']
#print(cookies)
#------------------------------------------------------------------

#鼠标移动到个人中心
with open(r'csdn.html','w',encoding='utf8') as f:
  f.write(browser.page_source)
  
a = browser.find_element_by_id("toolbar-remind")  
a.click()