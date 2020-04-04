# -*- coding:utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
# 参考链接：https://www.cnblogs.com/mengyu/p/6901489.html
import sys,os  

path = os.path.join(os.path.dirname(os.path.realpath(__file__)),"text3.html") 
driver = webdriver.Chrome()
driver.get(path)
driver.maximize_window()
time.sleep(3)
# 第一个操作:鼠标移动到某个元素
# 为了演示，开始设置标签的颜色淡蓝色，当鼠标移到到该元素时标签颜色变为红色
dragElement = driver.find_element_by_xpath('//*[@id="box1"]')  # 获取被拖拽的元素
targetElement = driver.find_element_by_xpath('//*[@id="area3"]')  # 获取被拖拽到的目标
Action = ActionChains(driver)
'''将【拖拽我吧！】元素拖拽到第三个对话框'''
# 首先选择元素，按住不放，然后移动元素，最后松开鼠标，完成拖拽
Action.click_and_hold(dragElement).move_to_element(
    targetElement).release().perform()
time.sleep(5)
driver.quit()
