
from scrapy.http import HtmlResponse 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.common.exceptions import NoSuchElementException,TimeoutException  
from selenium.webdriver.chrome.options import Options
import time

chrome_option  = Options()
chrome_option.add_argument('--ignore-certificate-errors')  
chrome_option.add_argument('--allow-insecure-localhost') 
chrome_option.add_argument('--disable-infobars')     # 去掉提示：Chrome正收到自动测试软件的控制
chrome_option.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_option.add_experimental_option('useAutomationExtension', False)
chrome_option.add_argument('--start-maximized')      # 最大化运行（全屏窗口）,不设置，取元素会报错

class SeniumSpider(object):
    def __init__(self):
        self.index = 0
        # 声明webdriver对象，可以全局使用
        self.chrome = webdriver.Chrome(chrome_options = chrome_option)   
        #self.url = 'https://antispider1.scrape.center'
        #self.url = 'https://spa2.scrape.center/'
        self.url = 'https://spa6.scrape.center/'
        self.wait = WebDriverWait(self.chrome,3)
    
    #获取电影详细信息
    def getmovie(self):
        movie_list = self.chrome.find_elements_by_css_selector('.m-b-sm')
        for movie in movie_list:
            self.index += 1
            href = movie.find_element_by_xpath("parent::a").get_attribute('href')
            print(f'电影Top-{self.index}的名字：{movie.text},详情链接地址：{href}') 

    def start(self):        
        # 防止被检测到WebDriver而被禁止访问
        self.chrome.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
                    "source": """
                    Object.defineProperty(navigator, 'webdriver', {
                    get: () => undefined
                    })"""
                }) 
        self.chrome.get(self.url)
        time.sleep(3)
        
        #页面滚动到底部
        js = "window.scrollTo(0,document.body.scrollHeight)"
        self.chrome.execute_script(js) 
        time.sleep(1) 
        
        self.getmovie()

        while True:
            try:
                #查找下一页可点击对象
                btn = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'btn-next'))) 
                #点击进入下一页
                btn.click()
                time.sleep(2)
                self.getmovie()
            except:
                break
            
    def close(self):            
        print('爬取完成，关闭浏览器~')
        self.chrome.quit()        
    
if __name__ == "__main__":
    sps = SeniumSpider()
    sps.start()
    sps.close()

