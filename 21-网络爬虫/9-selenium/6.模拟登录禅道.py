from selenium import webdriver
import time

class ZentaoSelenium():
    def __init__(self):
        self.login_url = 'http://192.168.74.112/zentao/user-login.html'
        self.username = "guojun"
        self.pwd = "tggcTGGC!@#$1234"
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        
    #登录    
    def login(self):  
        #请求url
        self.driver.get(self.login_url)
        #发送表单数据
        userid = self.driver.find_element_by_id("account")
        passwd = self.driver.find_element_by_name("password")
        userid.send_keys(self.username)
        passwd.send_keys(self.pwd)
        time.sleep(1)
        #提交
        submit = self.driver.find_element_by_id("submit")
        submit.click()
    
    #注销    
    def logout(self):
        #退出登录
        logout = self.driver.find_element_by_xpath("/html/body[@class='m-my-index']/header[@id='header']/div[@id='topbar']/div[@id='topnav']/a[1]")
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
    