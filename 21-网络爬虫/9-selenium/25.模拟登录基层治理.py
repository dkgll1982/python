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

driver = webdriver.Chrome()
wait = WebDriverWait(driver,30)         #显式等待

driver.maximize_window()                #浏览器窗口最大化
driver.get('http://jczl.giscloud.cx/iam/login.html?ReturnUrl=%2Fzhzl-frames%2Fmain2.html')

#表单输入框
userid = driver.find_element_by_xpath("/html/body/div[@id='app']/div[@class='application--wrap']/div[@class='container login-background fluid fill-height']/div[@class='layout login-head align-center justify-center']/div[@class='flex all']/div[@class='layout row']/div[@class='flex md5']/div[@class='v-tabs login-card lighten-2']/div[@class='v-window']/div[@class='v-window__container']/div[@class='v-window-item'][1]/div[@class='v-card v-sheet theme--light']/div[@class='v-card__text']/div[@class='v-input v-text-field v-text-field--single-line theme--light'][1]/div[@class='v-input__control']//input")
pwd = driver.find_element_by_xpath("//div[@class='v-input v-text-field v-text-field--single-line theme--light'][2]//div[@class='v-input__control']//input")

userid.send_keys("admin")
pwd.send_keys("DFYOPS1RrpdVlu2U")

time.sleep(1)

btn = driver.find_element_by_xpath("/html/body/div[@id='app']/div[@class='application--wrap']/div[@class='container login-background fluid fill-height']/div[@class='layout login-head align-center justify-center']/div[@class='flex all']/div[@class='layout row']/div[@class='flex md5']/div[@class='v-tabs login-card lighten-2']/div[@class='v-window']/div[@class='v-window__container']/div[@class='v-window-item'][1]/div[@class='v-card v-sheet theme--light']/div[@class='v-card__text']/button[@class='text-xs-right v-btn v-btn--block theme--light']")

#点击登录,跳转到首页
btn.click()  

menu = {}
try: 
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'nav-text')))   
    lin_list = driver.find_elements_by_class_name("nav-text")
    for index,item in enumerate(lin_list,start = 1):
       menu[item.text] = item
       print(f"{index}:{item.tag_name},{item.text},{item.get_attribute('href')},{item.get_attribute('class')}")
except TimeoutException:
    print('Time Out')
except NoSuchElementException as e:
    print('No Menu')   
except Exception as e:
    print(e)
 
time.sleep(3)
  
menu["事件管理"].click()    
 
# for handle in driver.window_handles:
#     driver.switch_to_window(handle)

#没有解决定位问题，采用坐标定位
#ActionChainsDriver = ActionChains(driver).move_by_offset(230, 95).click()

#time.sleep(5)
  
#ActionChainsDriver.perform()  

# 关闭浏览器
#driver.quit()