# coding:utf-8
from selenium import webdriver
import requests
import sys
import time
from lxml import etree
import pickle
import os
# reload(sys)
# sys.setdefaultencoding('utf-8')

class Zhihu:
    def __init__(self,homeurl):
        self.homeurl = homeurl

    def save_session(self,session): #保存session，下次可直接使用，避免再次登录
        with open('session.txt','wb') as f:
            pickle.dump(session, f)
            print("Cookies have been writed.")

    def load_session(self):     #加载session
        with open('session.txt', 'rb') as f:
            s = pickle.load(f)
        return s

    def GetCookies(self):       #初次登录用selenium模拟，并获得cookies
        browser = webdriver.Chrome()
        browser.get("https://www.zhihu.com/signin")
        browser.find_element_by_xpath("//main//div[2]/div[1]/form/div[1]/div[2]/div[1]/input").send_keys("13060882373")
        browser.find_element_by_xpath("//main//div[2]/div[1]/form/div[2]/div/div[1]/input").send_keys("xxxxxx")
        browser.find_element_by_xpath("//main//div[2]/div[1]/form/button").click()
        time.sleep(10)
        cookies = browser.get_cookies()
        browser.quit()
        return cookies

    def get_session(self):  #获取session
        s = requests.Session()
        if not os.path.exists('session.txt'):   #如果没有session，则创建一个，并且保存到文件中
            s.headers.clear()
            for cookie in self.GetCookies():
                s.cookies.set(cookie['name'], cookie['value'])
            self.save_session(s)
        else:                                   #如果已存在session，则直接加载使用
            s = self.load_session()
        return s

    def Crawl(self):    #开始爬取
        s = self.get_session()
        html = s.get(self.homeurl).text
        html_tree = etree.HTML(html)
        items = html_tree.xpath('//main//div[1]/div[2]//div[@class="ContentItem AnswerItem"]/@data-zop')
        for item in items:
            content = eval(item)
            authorName = content['authorName']
            title = content['title']
            print(authorName + "回答了：" + title)

zhihu = Zhihu('https://www.zhihu.com/')
zhihu.Crawl()