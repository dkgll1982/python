#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-04-06 14:58:19 
# @Remark: 人生苦短，我用python！

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pyecharts.charts import Bar,Page
from pyecharts import options as opts
import jieba
import wordcloud
import time
import requests
from urllib import parse as urlparse
from matplotlib import pyplot as plt
import sys
import os 

class DouYuSpider():
    def __init__(self):
        super().__init__()
        self.host = 'https://www.douyu.com'
        self.url = urlparse.urljoin(self.host,'/g_LOL')
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver,50)
        self.all_name = ""     #保存全部主播名称
        self.data = {">200万": 0, ">150万": 0, ">100万": 0, ">50万": 0, ">30万": 0, ">10万": 0, ">1万": 0, "1万以下": 0}    
        self.max_page = 10      #爬取的最大页数    
        self.page = 0          #当前页码

    # 获取文件当前所在的目录，并返回完整文件全路径 
    def realpath(self,filename):
        return os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)

    #发送请求
    def send_request(self):
        self.driver.get(self.url)   
        
        while True: 
            time.sleep(2)
            # 滑动底部
            self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            
            username = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'.DyListCover-intro')))    #用户名称
            fans_num = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'.DyListCover-hot')))      #粉丝数量
            
            for info in zip(username,fans_num):  
                num = info[1].text 
                if "万" in num:
                    num = float(num.replace('万', "")) * 10000
                else:
                    num = int(num)
                    
                if num >= 2000000:
                    self.data[">200万"] = self.data[">200万"] + 1
                elif num >= 1500000 and num < 2000000:
                    self.data[">150万"] = self.data[">150万"] + 1
                elif num >= 1000000 and num < 1500000:
                    self.data[">100万"] = self.data[">100万"] + 1
                elif num >= 500000 and num < 1000000:
                    self.data[">50万"] = self.data[">50万"] + 1
                elif num >= 300000 and num < 500000:
                    self.data[">30万"] = self.data[">30万"] + 1
                elif num >= 100000 and num < 300000:
                    self.data[">10万"] = self.data[">10万"] + 1
                elif num >= 10000 and num < 100000:
                    self.data[">1万"] = self.data[">1万"] + 1
                elif num >= 0 and num < 10000:
                    self.data["1万以下"] = self.data["1万以下"] + 1
                    
                self.all_name += info[0].text
                
            # 获取下一页
            self.page += 1
            if self.page == self.max_page:
                print('爬取页数已达到最大页数{}页限制，终止爬取！'.format(self.page))
                break
        
            print('正在爬取第{}页...'.format(self.page))
                    
            next_page = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.dy-Pagination-next')))
            if next_page.get_attribute('aria-disabled') == 'false':
                next_page.click()       #跳转到下一页
            else:                       #如果爬取到最后一页，退出循环
                print('已经爬取到最后一页，终止爬取！')
                break
            
        # 最后生成表格
        self.create_bar()
        print('创建表格成功！')
        
        # 最后生成词云
        self.create_wordcloud()
        print('创建词云成功！')
        
        time.sleep(5)
        self.driver.close()
         
    #创建表格
    def create_bar(self):
        bar = (
                Bar()
                .add_xaxis(list(self.data.keys()))
                .add_yaxis("斗鱼热度", list(self.data.values()))
                .set_global_opts(title_opts = opts.TitleOpts(title="热度分析", subtitle="斗鱼"))
        )
        bar.render(self.realpath('douyu_hot.html'))
    
    #创建词云
    def create_wordcloud(self):
        words = jieba.lcut(self.all_name)
        fnl_words = [word for word in words if len(word) > 1]  # 去掉单字 
        
        #词云对象
        w = wordcloud.WordCloud(
            width = 1000,
            height = 800, 
            font_path='Fonts/font1.ttf',
            max_words= 80
        )
        
        # 将string变量传入w的generate()方法，给词云输入文字
        w.generate(' '.join(fnl_words))
        w.to_file(self.realpath('douyu_ciyun.png'))
    
    def start(self):
        self.send_request()
    
if __name__ == "__main__":
    dys = DouYuSpider()
    dys.start()