from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#By是selenium中内置的一个class，在这个class中有各种方法来定位元素
#By所支持的定位器的分类：
# CLASS_NAME = 'class name'
# CSS_SELECTOR = 'css selector'
# ID = 'id'
# LINK_TEXT = 'link text'
# NAME = 'name'
# PARTIAL_LINK_TEXT = 'partial link text'
# TAG_NAME = 'tag name'
# XPATH = 'xpath'

class ZentaoSelenium():
    def __init__(self):
        login_url = 'http://192.168.74.112/zentao/user-login.html'
        username = "guojun"
        pwd = "tggcTGGC!@#$1234"
        driver = webdriver.Chrome()
        driver.maximize_window()
        
    #登录    
    def login(self):  
        #请求url
        self.driver.get(self.login_url)
        #发送表单数据
        userid = self.driver.find_element(By.ID,"account")
        passwd = self.driver.find_element(By.NAME,"password")
        userid.send_keys(self.username)
        passwd.send_keys(self.pwd)
        time.sleep(1)
        #提交
        submit = self.driver.find_element(By.ID,"submit")
        submit.click()
    
    #注销    
    def logout(self):
        #退出登录
        logout = self.driver.find_element(By.XPATH,"/html/body[@class='m-my-index']/header[@id='header']/div[@id='topbar']/div[@id='topnav']/a[1]")
        logout.click()

    def start(self):
        #此处模拟循环登入登出
        for x in range(4):
            self.login()
            time.sleep(3)
            self.logout()
            time.sleep(3)
        self.driver.close()
        
if __name__ == '__main__':
    zentao = ZentaoSelenium()
    zentao.start()
    