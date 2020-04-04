from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()
try:
    browser.get('https://www.taobao.com')
    input1 = browser.find_element_by_id('q')
    input2 = browser.find_element_by_css_selector('#q')
    input3 = browser.find_element_by_xpath("//*[@id='q']") 
    print(input1,'\r\n',input2,'\r\n',input3) 
finally:
    browser.close()