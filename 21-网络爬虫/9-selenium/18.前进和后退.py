from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("http://www.zhihu.com/explore")
browser.get("http://www.baidu.com") 
browser.get("https://www.taobao.com")

browser.back()
time.sleep(1)
browser.forward()
time.sleep(2)
browser.quit()