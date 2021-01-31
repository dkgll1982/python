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

import os,time
#移除Selenium中的 window.navigator.webdriver：https://www.cnblogs.com/presleyren/p/12936553.html

url = 'https://home.51cto.com/index'

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
