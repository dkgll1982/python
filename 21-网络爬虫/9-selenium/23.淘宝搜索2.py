from selenium import webdriver
import time
 
browser = webdriver.Chrome()
 
browser.get("http://www.taobao.com")
input_first = browser.find_element_by_id("q")
input_second = browser.find_element_by_css_selector("#q")
input_third = browser.find_element_by_xpath('//*[@id="q"]')
print('1-->：',input_first)
print('2-->：',input_second)
print('3-->：',input_third)
input_first.send_keys('书籍')
time.sleep(2)
button = browser.find_element_by_class_name('btn-search')
button.click()
browser.close()