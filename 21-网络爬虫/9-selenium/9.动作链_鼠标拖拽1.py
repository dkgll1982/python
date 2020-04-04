# -*- coding:utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get('file:///E:/100-航天智慧/2-源码库/python/21-网络爬虫/9-selenium/text3.html')
driver.maximize_window()
time.sleep(2)
# 第一个操作:鼠标移动到某个元素
# 为了演示，开始设置标签的颜色淡蓝色，当鼠标移到到该元素时标签颜色变为红色
dragElement = driver.find_element_by_xpath('//*[@id="box1"]')       # 获取被拖拽的元素
targetElement = driver.find_element_by_xpath('//*[@id="area1"]')    # 获取被拖拽到的目标
Action = ActionChains(driver)
'''将【拖拽我吧！】元素拖拽到第一个对话框'''
Action.drag_and_drop(dragElement, targetElement).perform()          # 将【拖拽我吧！】拖到第一个对话框
time.sleep(5)
'''将【拖拽我吧！】元素拖拽到距离当前位置(45,200)，也就是拖拽到第二个对话框'''
'''由于第一次我们已经将元素拖拽到了第一个对话框，所以我们实际的拖拽是从第一个对话框拖拽到第二个对话框'''
Action.drag_and_drop_by_offset(dragElement, 45, 200).perform()
time.sleep(5)
driver.quit()
