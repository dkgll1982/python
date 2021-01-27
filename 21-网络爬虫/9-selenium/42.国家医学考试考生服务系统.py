#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-04-07 21:30:39 
# @Remark: 人生苦短，我用python！
# 参考链接：http://www.45fan.com/article.php?aid=20020931613053929325085707

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time
import requests
from urllib import parse
import re
import random
import string 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from PIL import Image
from ydmhttp import YDMHttp  # 导入上面整理好的云打码接口
import getCardId

class KaoShiSpider():
    def __init__(self):
        super().__init__()
        self.host = 'http://www2.nmec.org.cn'
        self.regist_url = parse.urljoin(self.host, 'wangbao/nme/sp/root/account/signup.html')  
        #注意：无界面模式、有界面模式的截图位置不一样,需要分别处理 
        self.hasBrowser = False
        self.driver = self.ChromeDriverBrowser() if self.hasBrowser else self.ChromeDriverNOBrowser()
 
        self.wait = WebDriverWait(self.driver,20)
        self.base_dir = r'backup/爬虫/验证码/'
        self.full_img = self.base_dir+'full.png'
        self.code_img = self.base_dir+'ma_code.png'
        self.headers = { 
            "referer":'http://www2.nmec.org.cn/wangbao/nme/sp/root/account/signup.html',
            "user_agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
        }
        
    # 无界面模式
    def ChromeDriverNOBrowser(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        driverChrome = webdriver.Chrome(executable_path=r"D:\Programing\Python\chromedriver",chrome_options=chrome_options)
        return driverChrome
    
    # 有界面的就简单了
    def ChromeDriverBrowser(self):
        driverChrome = webdriver.Chrome(executable_path=r"D:\Programing\Python\chromedriver")
        return driverChrome 

    #生成随机字符串
    def random_str(self,min,max):
        return random.choice('abcdefghijklmnopqrstuvwxyz')+''.join(random.sample(string.ascii_letters + string.digits, random.randint(min,max)))
    
    #生成随机用戶信息
    def set_data(self):
        mail_type = ['qq.com','sina.com','163.com','sohu.com','263.com','139.com','126.com','189.com','hotmail.com','21cn.com','gmail.com','aliyun.com']    
        self.email = self.random_str(5,9) + '@' + mail_type[random.randint(0,11)]
        self.username = self.random_str(8,16)
        self.pwd = self.random_str(8,14) 
        
    #注册
    def regist(self): 
        self.driver.get(self.regist_url)       
        self.get_img()              
        #表单输入框(用户名、密码、验证码) 
        input_username = self.driver.find_element_by_id("Edit:SP_User.0$UserName")
        input_name = self.driver.find_element_by_id("Edit:SP_User.0$Name")
        select_cardcode = Select(self.driver.find_element_by_id("Edit:SP_User.0$Certificate_TypeID"))
        input_card = self.driver.find_element_by_id("Edit:SP_User.0$Certificate_No")
        input_birthdate = self.driver.find_element_by_id("Edit:SP_User.0$Birthday")
        select_nation = Select(self.driver.find_element_by_id("Edit:SP_User.0$Nationality"))  
        input_pwd  = self.driver.find_element_by_id("Edit:SP_User.0$Passwd")
        input_repwd  = self.driver.find_element_by_id("Edit:SP_User.0$Passwd_Confirm")
        input_question = self.driver.find_element_by_id("Edit:SP_User.0$PasswdQuestion")
        input_answer = self.driver.find_element_by_id("Edit:SP_User.0$PasswdAnswer")
        input_email = self.driver.find_element_by_id("Edit:SP_User.0$Email")
        #验证码输入框
        input_captcha = self.driver.find_element_by_id("Captcha") 
        
        input_username.send_keys(self.random_str(8,16))
        input_name.send_keys('张鑫旭')
        select_cardcode.select_by_index("1") 
        input_card.send_keys(getCardId.generate_ID())
        input_birthdate.send_keys('1988-11-18')
        select_nation.select_by_index("1") 
        input_pwd.send_keys('zhangsan123456789')
        input_repwd.send_keys('zhangsan123456789')
        input_question.send_keys('zhangsan123456789')
        input_answer.send_keys('zhangsran123456789')
        input_email.send_keys('DFGF2DGD@SINA.COM')  
        
        # 1：人工输入验证码 
        #input_captcha.send_keys(input('请输入验证码：'))    
        
        # 2：云打码 
        # 使用云打码识别图片验证码
        ydm = YDMHttp(filename = self.code_img, codetype = 1004, timeout = 10)
        cid, code_text = ydm.decode()
        # 以f开头表示在字符串内支持大括号内的python 表达式
        print(f'验证码识别结果：{code_text}') 
        input_captcha.send_keys(code_text)    
        
        time.sleep(5)
        
        # 提交
        self.driver.find_element_by_id('T_Submit').click()

    #截取验证码图片
    def get_img(self):
        # 能否在5s内找到验证码元素，能才继续
        if WebDriverWait(self.driver,5).until(lambda the_driver:the_driver.find_element_by_id("CaptchaImg"), "查找不到该元素"):
            # 对于一次截屏无法到截到验证码的情况，需要滚动一段距离，然后验证码的y坐标也应该减去这段距离
            scroll = 500
            js = "document.documentElement.scrollTop='%s'" %scroll
            self.driver.execute_script(js)
            # 截下该网站的图片
            self.driver.get_screenshot_as_file(self.full_img)
            # 获得这个图片元素
            img_ele = self.driver.find_element_by_id("CaptchaImg")
            
            # 得到该元素左上角的 x，y 坐标和右下角的 x，y 坐标            
            if self.hasBrowser:
                left = img_ele.location.get('x') + 65
                upper = img_ele.location.get('y') - 500+120
                right = left + img_ele.size.get('width')+25
                lower = upper + img_ele.size.get('height')+20
            else:
                left = img_ele.location.get('x')
                upper = img_ele.location.get('y') - 500 
                right = left + img_ele.size.get('width') + 10
                lower = upper + img_ele.size.get('height')
            
            # 打开之前的截图
            img = Image.open(self.full_img)
            # 对截图进行裁剪，裁剪的范围为之前验证的左上角至右下角范围
            new_img = img.crop((left, upper, right, lower))
            # 裁剪完成之后保存到指定路径
            new_img.save(self.code_img)
            
            time.sleep(2) 
        else:
            print("找不到验证码元素")   

    #发送请求
    def send_request(self,url):
        response = requests.get(url,headers = self.headers)
        if response.status_code == 200:
            return response
        
    #写入文件    
    def write_content(self,content):
        with open(self.path,'wb') as f:
            f.write(content)
    #注销
    def louout(self): 
        pass
    
    def start(self):
        for x in range(5):
            self.regist()
            time.sleep(1)

if __name__ == "__main__":
    kss = KaoShiSpider()
    kss.start()