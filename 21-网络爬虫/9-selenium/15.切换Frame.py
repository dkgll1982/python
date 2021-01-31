from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

browser = webdriver.Chrome()
browser.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
browser.switch_to_frame('iframeResult') #切换到子页面
try:
    logo = browser.find_element_by_class_name('logo')   #子页面无此元素
except NoSuchElementException as e:
    print('No Logo')
browser.switch_to.parent_frame()        #从子页面切换到父页面
logo = browser.find_element_by_class_name('logo')
print(logo)
print(logo.text)