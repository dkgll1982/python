#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: guojun
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd
# @Site: https://user.qzone.qq.com/350606539/main
# @Date: 2020-04-06 19:21:28
# @Remark: 人生苦短，我用python！

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pyecharts.charts import Bar, Page
from pyecharts import options as opts
import jieba
import wordcloud
import time
import requests
from urllib import parse as urlparse
from matplotlib import pyplot as plt
import sys
import os
import re

class DouBanSpider():
    def __init__(self):
        super().__init__()
        self.url = 'https://movie.douban.com/'
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.page = 0       # 当前页码
        self.max_page = 10  # 限制爬取的最大页码
        self.kw = ''
        self.all_name = ""  #保存全部演员名称
        self.data = {'9.5': 0, '9.0': 0, "8.5": 0, "8.0": 0, "7.5": 0, "7.0": 0, "6.5": 0, "6.0": 0,"6.0以下": 0}  # 评分信息

    # 获取文件当前所在的目录，并返回完整文件全路径
    def realpath(self, filename):
        return os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)

    # 发送请求
    def send_request(self):
        self.driver.get(self.url)
        input = self.driver.find_element_by_id('inp-query')
        # 发起搜索
        input.send_keys(self.kw)
        input.send_keys(Keys.ENTER)

        while True:
            time.sleep(2)
            # 滚动到底部
            self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')

            # 获取下一页
            self.page += 1
            if self.page == self.max_page:
                print('爬取页数已达到最大页数{}页限制，终止爬取！'.format(self.page))
                break

            print('正在爬取第{}页...'.format(self.page))

            # 获取电影标题、评分
            div_list = self.driver.find_elements_by_xpath('//div[@class="item-root"]')

            # 首页去掉第一条，因为第一条是查询的描述信息
            div_list = div_list[1:] if self.page == 1 else div_list

            for div in div_list:
                score, pj_num = 0, 0
                title = div.find_element_by_xpath('.//a[@class="title-text"]').text
                try:
                    score = float(div.find_element_by_xpath('.//span[@class="rating_nums"]').text)
                    if score >= 9.5:
                        self.data['9.5'] += 1
                    elif score >= 9.0 and score < 9.5:
                        self.data['9.0'] += 1
                    elif score >= 8.5 and score < 9.0:
                        self.data['8.5'] += 1
                    elif score >= 8.0 and score < 8.5:
                        self.data['8.0'] += 1
                    elif score >= 7.5 and score < 8.0:
                        self.data['7.5'] += 1
                    elif score >= 7.0 and score < 7.5:
                        self.data['7.0'] += 1
                    elif score >= 6.5 and score < 7.0:
                        self.data['6.5'] += 1
                    elif score >= 6.0 and score < 6.5:
                        self.data['6.0'] += 1 
                    else:
                        self.data['6.0以下'] += 1
                except Exception as e:
                    self.data['6.0以下'] += 1

                result = re.search('\d+', div.find_element_by_xpath(".//span[@class='pl']").text)
                if result:
                    pj_num = result.group()
                actor = div.find_element_by_xpath('.//div[@class="meta abstract_2"]').text
                self.all_name += actor
                print("电影：{},评分：{},评价人数：{},演员列表：{}".format(title, score, pj_num, actor))

            # 下一页
            try:
                next_page = self.driver.find_element_by_css_selector('a.next')
                next_page.click()
            except Exception as e:
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

    # 创建表格
    def create_bar(self):
        bar = (
            Bar()
            .add_xaxis(list(self.data.keys()))
            .add_yaxis("电影评分", list(self.data.values()))
            .set_global_opts(title_opts=opts.TitleOpts(title="电影评分", subtitle=self.kw))
        )
        bar.render(self.realpath('move_score.html'))
        
    #创建词云
    def create_wordcloud(self):
        words = jieba.lcut(self.all_name)
        fnl_words = [word for word in words if len(word) > 1]  # 去掉单字 
        
        #词云对象
        w = wordcloud.WordCloud(
            width = 1000,
            height = 800, 
            font_path ='Fonts/font1.ttf',
            max_words = 80
        )
        
        # 将string变量传入w的generate()方法，给词云输入文字
        w.generate(' '.join(fnl_words))
        w.to_file(self.realpath('move_actor.png'))

    def start(self):
        while True:
            self.kw = input('请输入查询关键字:')
            if not self.kw:
                continue
            else:
                break
        self.send_request()


if __name__ == "__main__":
    dbs = DouBanSpider()
    dbs.start()
