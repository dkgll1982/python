import requests
from selenium import webdriver
from lxml import etree
import time
from selenium.common.exceptions import NoSuchElementException,TimeoutException 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

url = 'http://huzhou-jczl-cx.spacecig.com/zhzl-frames/main.html'
browser = webdriver.Chrome()
browser.get(url)
browser.maximize_window()
 
wait = WebDriverWait(browser,20)

#查该页面有哪些iframe(此处很有用，可以测试出对应的iframe信息，以便切换无误)
iframes = browser.find_elements_by_tag_name("iframe")
# for iframe in iframes:
#     #获取节点ID、位置、标签名和大小
#     print('[id:',iframe.id,
#           ';location:',iframe.location,
#           ';tag_name:',iframe.tag_name,
#           ';size:',iframe.size,
#           ';class',iframe.get_attribute('class'),']'
#     ) 

#打印框架html   
print('outerHTML:',iframes[0].get_attribute('outerHTML'))  # 获取某个元素的html
print('innerHTML:',iframes[0].get_attribute('innerHTML'))  # 获取某个元素的html

print('*'*40)
#打印切换框架前的所有input元素信息
input = browser.find_elements_by_xpath("//input")
for item in input: 
    attrs = browser.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', item)
    print(attrs,' name:',item.get_attribute('name'),' size:',item.size,' class',item.get_attribute('class'),' id',item.get_attribute('id'))

print('*'*40)

#通过上边测试，发现第一个iframe即为我们需要登录的框架子页面
browser.switch_to_frame(iframes[0])

print('-'*40)
#打印框架内部的所有input元素信息
input = browser.find_elements_by_xpath("//input")
for item in input: 
    attrs = browser.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', item)
    print(attrs,' name:',item.get_attribute('name'),' size:',item.size,' class',item.get_attribute('class'),' id',item.get_attribute('id'))

print('-'*40)

try: 
    #用户名
    userid = wait.until(EC.element_to_be_clickable((By.NAME,'userid')))

    print(userid)
    userid.send_keys("admin")
    #密码
    pwd = browser.find_element_by_xpath('//div[@class="textInput paw"]/input')
    pwd.send_keys('DFYOPS1RrpdVlu2U')

    #登录按钮
    btnlogin = browser.find_element_by_class_name('login_btn')
    btnlogin.click()
finally:
    time.sleep(3)   #强制等待3秒    
    print('title:',browser.title,";url:",browser.current_url)  
    
    #进入系统按钮
    btnenter = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'sys_btn')))
    
    #单击进入系统 
    action = ActionChains(browser).click(btnenter)
    action.perform()

    nav_list = {}
    try:
        # 获取导航菜单,只要一个符合条件的元素加载出来就通过:presence_of_element_located
        # 另一个必须所有符合条件的元素都加载出来才行:presence_of_all_elements_located
        menus = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,'nav-text')))
        # 打印导航菜单信息
        for index,item in enumerate(menus,start = 1):
            print(f'导航菜单{index}',
                '[id:',item.id,
                ';location:',item.location,
                ';tag_name:',item.tag_name,
                ';size:',item.size,
                ';class',item.get_attribute('class'),
                ';text',item.text,
                ';href',item.get_attribute('href'),
                ']'
            )
            nav_list[item.text] = item
    finally:
        tag = '人口管理'
        nav_list[tag].click()