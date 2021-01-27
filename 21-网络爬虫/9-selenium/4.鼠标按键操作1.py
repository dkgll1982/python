from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
#常用按键用法：https://www.cnblogs.com/c-x-a/p/8480074.html
# https://www.cnblogs.com/chun-xiaolin001/p/10201211.html

browser = webdriver.Chrome()
browser.get("https://www.taobao.com")

htmlElem = browser.find_element_by_tag_name('html')
while True:
    htmlElem.send_keys(Keys.END)        # scrolls to bottom 
    time.sleep(3)

htmlElem.send_keys(Keys.HOME)       # scrolls to bottom  