from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

browser = webdriver.Chrome()
try:
    browser.get('https://www.taobao.com')
    lis = browser.find_elements_by_css_selector('.service-bd li')
    for index,item in enumerate(lis,start=1):
        print('第{}个节点：{}'.format(index,item))
    time.sleep(5)
finally:
    browser.close()