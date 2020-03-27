#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-03-25 19:22:43 
# @Remark: 人生苦短，我用python！

from lxml import etree
import re
import time
import os
import sys
import requests
from urllib import parse


class CaiPiaoSpider():
    def __init__(self):
        super().__init__(self)
        self.host = ''
        self.url = ''
        self.base_fir = ''
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36"
        }

    # 发送请求
    def send_request(self, url):
        try:
            response = requests.get(url=url, headers=self.headers)
            if response.status_code == 200:
                return response
        except Exception as e:
            print('URL:{},错误信息:{}'.format(url, e))

    # 解析请求
    def parse_content(self, response):
        html = etree.HTML(response.text)

    # 写入文件
    def write_content(self, content, path):
        with open(path, 'w') as f:
            f.write(content)

    def start(self):
        pass


if __name__ == "__main__":
    start = time.time()
    cps = CaiPiaoSpider()
    cps.start()
    end = time.time()
    print('爬取数据完成，耗时.2fs%'(end - start))
