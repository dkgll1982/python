#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-04-03 16:07:54 
# @Remark: 人生苦短，我用python！

from selenium import webdriver
from time import sleep

# 后面是你的浏览器驱动位置，记得前面加r'','r'是防止字符转义的
driver = webdriver.Chrome()
driver.maximize_window()

# 用get打开百度页面
driver.get("http://www.baidu.com")
# 查找页面的“设置”选项，并进行点击
driver.find_elements_by_link_text('设置')[0].click()
sleep(2)
# # 打开设置后找到“搜索设置”选项，设置为每页显示50条
driver.find_elements_by_link_text('搜索设置')[0].click()
sleep(2)

# 选中每页显示50条
m = driver.find_element_by_id('nr')
sleep(2)
m.find_element_by_xpath('//*[@id="nr"]/option[3]').click()
m.find_element_by_xpath('.//option[3]').click()
sleep(2)

# 点击保存设置
driver.find_elements_by_class_name("prefpanelgo")[0].click()
sleep(2)

# 处理弹出的警告页面   确定accept() 和 取消dismiss()
driver.switch_to_alert().accept()
sleep(2)
# 找到百度的输入框，并输入 美女
driver.find_element_by_id('kw').send_keys('美女')
sleep(2)
# 点击搜索按钮
driver.find_element_by_id('su').click()
sleep(2)

#滚动到底部
driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
#driver.execute_script('alert("dkgll,滚动到底部了~~~")')
sleep(2)

#跳转到第4页
for x in range(3):
    a = driver.find_element_by_css_selector("a.n")
    a.click()
    sleep(2)

    #滚动到底部
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    sleep(2)

# 在打开的页面中找到链接包含“美女”，并打开这个页面
#eles = driver.find_elements_by_partial_link_text('美女')
eles = driver.find_elements_by_xpath("//div[@id='content_left']//h3[@class='t']/a")
ele = eles[len(eles)-1]
ele.click() 

sleep(10)
# # 关闭浏览器
driver.quit()