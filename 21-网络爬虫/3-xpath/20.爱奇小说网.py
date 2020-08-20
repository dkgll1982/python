#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-08-20 15:47:16 
# @Remark: 人生苦短，我用python！
# 此文章需要今日头条购买

from lxml import etree
import time
import os
import re
import requests
import urllib 

class XiyoujiSpider():
    def __init__(self):
        super().__init__()
        self.host = 'https://www.ai7wu.com/0/160/'
        self.headers = {
            "user_agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
        }
        self.base_dir = r'backup/爬虫/小说'
        if not os.path.exists(self.base_dir):
            os.mkdir(self.base_dir)
    #返回列表第一条
    def first(self,list):
        return list[0] if list else '' 
    
    def send_request(self, url):
        response = requests.get(url=url, headers=self.headers)
        if response.status_code == 200:
            return response

    def parse_request(self, response):
        html = etree.HTML(response.content)
        dd_list = html.xpath("//div[@id='list']/dl/dd")
        for dd in dd_list: 
            url = urllib.parse.urljoin(self.host, self.first(dd.xpath(".//a/@href")))  
            res = self.send_request(url)
            if res:
                cont = etree.HTML(res.content)
                title = cont.xpath("//div[@class='bookname']/h1/text()")[0]
                details = "".join(cont.xpath("//div[@id='content']//text()")).replace('\n','').replace(
                    '精彩阅读·尽在·爱^奇书屋（www.ai7wu.com）','').replace('class"gcimgcation"','').replace(
                    '【爱奇小说 www.ai7wu.com】<首发、域名、请记住','').replace(
                    '手机看书，尽在·爱^奇书屋手机版M.ai7wu.Com','').replace(
                    '~⑧~1~ωωω.ai\7w*u.còм <首发、域名、请记住','').replace(
                    'あ爱7^书屋ヤ','')
                if title: 
                    self.write_content('', '西游天殇', title + details + '\n','a')
                    print(f'提取第{title}章节内容完成...')

    def write_content(self, dir, file_name, content,write_mode = 'w'):
        path = self.base_dir + '/' + dir
        if not os.path.exists(path):
            os.mkdir(path)
        with open(path+'/%s.txt' % file_name, write_mode, encoding='utf-8') as f:
            f.write(content)

    def start(self): 
        #self.url = urllib.parse.urljoin(self.host, '/book/{}.html'.format(item["key"]))
        response = self.send_request(self.host)
        if response:
            self.parse_request(response)

if __name__ == '__main__':
    start = time.time()
    sgs = XiyoujiSpider()
    sgs.start()
    end = time.time()
    print('爬取小说完成，耗时%.2fs！' % (end-start))
