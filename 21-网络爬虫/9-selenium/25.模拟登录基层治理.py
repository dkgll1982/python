import requests
from selenium import webdriver
from lxml import etree
import time
from selenium.common.exceptions import NoSuchElementException,TimeoutException 

driver = webdriver.Chrome()
driver.maximize_window()    #浏览器窗口最大化
driver.get('http://jczl.giscloud.cx/iam/login.html?ReturnUrl=%2Fzhzl-frames%2Fmain2.html')

#表单输入框
userid = driver.find_element_by_xpath("/html/body/div[@id='app']/div[@class='application--wrap']/div[@class='container login-background fluid fill-height']/div[@class='layout login-head align-center justify-center']/div[@class='flex all']/div[@class='layout row']/div[@class='flex md5']/div[@class='v-tabs login-card lighten-2']/div[@class='v-window']/div[@class='v-window__container']/div[@class='v-window-item'][1]/div[@class='v-card v-sheet theme--light']/div[@class='v-card__text']/div[@class='v-input v-text-field v-text-field--single-line theme--light'][1]/div[@class='v-input__control']//input")
pwd = driver.find_element_by_xpath("//div[@class='v-input v-text-field v-text-field--single-line theme--light'][2]//div[@class='v-input__control']//input")

userid.send_keys("admin")
pwd.send_keys("DFYOPS1RrpdVlu2U")

time.sleep(1)

btn = driver.find_element_by_xpath("/html/body/div[@id='app']/div[@class='application--wrap']/div[@class='container login-background fluid fill-height']/div[@class='layout login-head align-center justify-center']/div[@class='flex all']/div[@class='layout row']/div[@class='flex md5']/div[@class='v-tabs login-card lighten-2']/div[@class='v-window']/div[@class='v-window__container']/div[@class='v-window-item'][1]/div[@class='v-card v-sheet theme--light']/div[@class='v-card__text']/button[@class='text-xs-right v-btn v-btn--block theme--light']")
#点击登录
btn.click()

print('-'*40)

#跳转到首页  
try:
    title = driver.find_element_by_xpath('/html')
    print('title:',title.text)
except TimeoutException:
    print('Time Out')
except NoSuchElementException as e:
    print('No Logo')   
except Exception as e:
    print(e)
    
print('-'*40)
#driver.switch_to.parent_frame()        #从子页面切换到父页面
#logo = driver.find_element_by_class_name("/html/body/div[@id='main']/div[@id='main']/header/div[@class='top-menu']/div[@class='tm-wrap']/ul/li[3]/i[@class='iconSize glyphiconfont icon-glyphicons-cig-people']")

# logo = browser.find_element_by_class_name("/html/body/div[@id='main']/div[@id='main']/header/div[@class='top-menu']/div[@class='tm-wrap']/ul/li[3]/i[@class='iconSize glyphiconfont icon-glyphicons-cig-people']")
# print(logo.text)


# for handle in driver.window_handles:
#     driver.switch_to_window(handle)


# 关闭浏览器
#driver.quit()