from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
#from selenium.webdriver import ActionChains
from lxml import etree
import time
 
#配置Chrome Headless模式
#chrome_options = Options()
#chrome_options.add_argument('--headless')
#chrome_options.add_argument('--disable-gpu')
#指定浏览器
#driver = webdriver.Chrome(chrome_options = chrome_options)
#定义浏览器，为有头模式
driver = webdriver.Chrome()
#将浏览器页面最大化
driver.maximize_window()
 
 
#主程序
if __name__ == "__main__":
    #淘宝登录界面
    url = 'https://login.taobao.com/member/login.jhtml'
    driver.get(url)
    driver.implicitly_wait(10)
    #让程序休眠10秒，在这期间，弹出登录界面之后，你就可以使用你的手机扫码登录淘宝了
    #其实也可以使用活动滑块来验证，但是我总是不成功，所以只能用扫码来验证了
    time.sleep(10)
    #定位索索狂，并将其清除
    driver.find_element_by_id('q').clear()
    #在搜索框内输入“羽绒服'
    driver.find_element_by_id('q').send_keys('羽绒服')
    #休息两秒，免得被发现为爬虫
    time.sleep(2)
    #点击搜索按钮
    driver.find_element_by_xpath('//*[@id="J_TSearchForm"]/div[1]/button').click()
    #休息两秒
    time.sleep(2)
    #driver.find_element_by_xpath('//*[@id="J_relative"]/div[1]/div/ul/li[2]/a').click()
    #点击来源于“ 天猫 ” 按钮
    #driver.find_element_by_xpath('//*[@id="tabFilterMall"]').click()
    #休息两秒
    #time.sleep(2)
    #点击 “ 销量最高按钮 ”
    #driver.find_element_by_xpath('//*[@id="J_relative"]/div[1]/div/ul/li[2]/a').click()
    #休息两秒
    #time.sleep(2)
    #打印当前页面的URL
    #print(driver.current_url)
    # 解析网页
    print(driver.page_source)
    # html = etree.HTML(driver.page_source)
    # # 利用xpath寻找大循环。
    # items = html.xpath('//div[@class="item J_MouserOnverReq  "]')
    # for item in items:
    #     #利用xpath 进行小循环，打印销量排名靠前的店家名称
    #     shop = item.xpath('div[2]/div[3]/div[1]/a/span[2]/text()')[0]
    #     print(shop) 