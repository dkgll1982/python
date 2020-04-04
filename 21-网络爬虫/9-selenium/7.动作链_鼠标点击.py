#-*- coding:utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.get('file:///E:/100-航天智慧/2-源码库/python/21-网络爬虫/9-selenium/demo_clicks.html')
driver.maximize_window()
# 首先我们需要获取到要操作的元素，然后再次进行操作
doubleButtonElement = driver.find_element_by_xpath('/html/body/form/input[2]')   #获取双击按钮元素
buttonElement = driver.find_element_by_xpath('/html/body/form/input[3]')         #获取单击按钮元素
rightButtonElement = driver.find_element_by_xpath('/html/body/form/input[4]')    #获取右击按钮元素
clickHoldElement = driver.find_element_by_xpath('/html/body/form/input[5]')      #获取按住不放按钮元素
'''内容开始的时候我们也介绍说明，当调用perform()方法时才会执行鼠标操作'''
#双击操作
ActionDoubleClick= ActionChains(driver).double_click(doubleButtonElement)
ActionDoubleClick.perform() 
time.sleep(3)
# 单击操作
ActionClick = ActionChains(driver).click(buttonElement)
ActionClick.perform()
time.sleep(3)
# 右击操作
ActionContextClick = ActionChains(driver).context_click(rightButtonElement)
ActionContextClick.perform()
time.sleep(3)
#按住不放左键
ActionClickHold = ActionChains(driver).click_and_hold(clickHoldElement)
ActionClickHold.perform()
time.sleep(3)
driver.quit()