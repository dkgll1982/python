#-*- coding:utf-8 -*-
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.baidu.com")
kw = driver.find_element_by_id('kw')
kw.send_keys('selenium')
kw.send_keys(Keys.ENTER)   #通过回车键来代替鼠标的左键
time.sleep(5)
kw.clear()
kw.send_keys('二次元')
kw.send_keys(Keys.ENTER)   #通过回车键来代替鼠标的左键
time.sleep(5)

driver.quit()