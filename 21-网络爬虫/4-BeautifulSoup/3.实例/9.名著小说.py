#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: guojun
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd
# @Site: https://user.qzone.qq.com/350606539/main
# @Date: 2020-03-27 16:59:52
# @Remark: 人生苦短，我用python！

from bs4 import BeautifulSoup, SoupStrainer
import time
import os
import re
import requests
import urllib


class SanGuoSpider():
    def __init__(self):
        super().__init__()
        self.host = 'http://www.shicimingju.com'
        self.headers = {
            "user_agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'
        }
        self.base_dir = r'backup/爬虫/小说'
        if not os.path.exists(self.base_dir):
            os.mkdir(self.base_dir)

    def send_request(self, url):
        response = requests.get(url=url, headers=self.headers)
        if response.status_code == 200:
            return response

    def parse_request(self, response, dir):
        soup = BeautifulSoup(response.text, 'lxml')
        a_list = soup.select('.book-mulu > ul > li')
        for a in a_list:
            url = urllib.parse.urljoin(self.host, a.find('a')['href'])
            res = self.send_request(url)
            if res:
                soup = BeautifulSoup(res.text, 'lxml')
                div = soup.select('div.chapter_content')
                if div:
                    txt = div[0].get_text()
                    self.write_content(dir, a.string, txt)

    def write_content(self, dir, file_name, content):
        path = self.base_dir + '/' + dir
        if not os.path.exists(path):
            os.mkdir(path)
        with open(path+'/%s.txt' % file_name, 'w', encoding='utf-8') as f:
            f.write(content)

    def start(self):
        xiaoshuo = [
            {'key': 'shuihuzhuan', 'name': '水浒传'},
            {'key': 'sanguoyanyi', 'name': '三国演义'},
            {'key': 'xiyouji', 'name': '西游记'},
            {'key': 'hongloumeng', 'name': '红楼梦'},
        ]
        for item in xiaoshuo:
            start = time.time()
            self.url = urllib.parse.urljoin(self.host, '/book/{}.html'.format(item["key"]))
            response = self.send_request(self.url)
            if response:
                self.parse_request(response, item["name"])
                end = time.time()
                print('爬取小说%s完成，耗时%.2fs！' % (item["name"], end-start))


if __name__ == '__main__':
    start = time.time()
    sgs = SanGuoSpider()
    sgs.start()
    end = time.time()
    print('爬取全部小说完成，耗时%.2fs！' % (end-start))
