#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: guojun
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd
# @Site: https://user.qzone.qq.com/350606539/main
# @Date: 2020-04-04 18:13:27
# @Remark: 人生苦短，我用python！

from selenium import webdriver
import time

browser = webdriver.Chrome()
# 1：首先打开一个窗口，跳转到指定页面
browser.get("https://wwww.baidu.com")
# 2：接着开启一个新的选项卡
browser.execute_script('window.open()')
print(browser.window_handles)
time.sleep(2)
# 3：然后切换到新的选项卡
browser.switch_to_window(browser.window_handles[1])
# 4：在新的选项卡跳转到指定页面
browser.get('https://www.taobao.com')
time.sleep(1)
# 5：切换到第一个选项卡
browser.switch_to_window(browser.window_handles[0])
# 6：在第一个选项卡跳转到新的页面
browser.get('https://python.org')

########################
browser.execute_script('window.open()')
browser.switch_to_window(browser.window_handles[2])
browser.get('https://user.qzone.qq.com/350606539/main')

x = 0
while True:
    x = x % 3
    browser.switch_to_window(browser.window_handles[x])
    time.sleep(1)
    x += 1
