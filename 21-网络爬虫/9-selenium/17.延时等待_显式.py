from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome() 
browser.get('https://www.taobao.com')
wait = WebDriverWait(browser,20)
input = wait.until(EC.presence_of_element_located((By.ID,'q')))
#延时等待条件(可点击的节点)
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.tbh-search')))
print(input,button)
