from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

#2020-05-21：反爬升级，验证不可用

class ZhaopingSelenium():
    def __init__(self):
        self.url = 'https://sou.zhaopin.com/?jl=765&kw=Java%E5%BC%80%E5%8F%91&kt=3' 
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        
    #登录    
    def send_request(self):  
        #请求url
        self.driver.get(self.url) 
        time.sleep(5)
        jobs = self.driver.find_element(By.CLASS_NAME,"contentpile__content__wrapper__item__info__box__jobname__title")
        for job in jobs:
            print(job) 

    def start(self):
        self.send_request()
        # #此处模拟循环登入登出
        # for x in range(4):
        #     self.login()
        #     time.sleep(3)
        #     self.logout()
        #     time.sleep(3)
        self.driver.close()
        
if __name__ == '__main__':
    zp = ZhaopingSelenium()
    zp.start()
    