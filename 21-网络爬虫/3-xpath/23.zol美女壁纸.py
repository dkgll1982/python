#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-08-27 11:08:55 

from lxml import etree
import time
import os
import requests
import urllib 

class BizhiSpider():
    def __init__(self):
        super().__init__()
        self.host = 'http://desk.zol.com.cn/bizhi/'
        self.headers = {
            "user_agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
        }
        self.base_dir = r'backup/image/zol壁纸'
        if not os.path.exists(self.base_dir):
            os.mkdir(self.base_dir)
            
    #返回列表第一条
    def li_first(self,list):
        return list[0] if list else '' 
    
    #发送请求
    def send_request(self, url):
        response = requests.get(url=url, headers=self.headers)
        if response.status_code == 200:
            return response
    
    #解析请求
    def parse_request(self, response):
        html = etree.HTML(response.content)                                                 #初始化生成一个XPath解析对象
        img_url = self.li_first(html.xpath("//img[@id='bigImg']/@src"))                     #图片地址
        img_name = ''.join(html.xpath("//h3//text()")).replace('\r','').replace(
            '\n','').replace('\t','').replace('/','_').replace('（','_').replace('）','')   #图片名称
        img_response = self.send_request(img_url)                                           #发送图片请求 
        self.write_content(img_response,img_name,self.base_dir)                             #下载图片
        #获取下一页的链接地址
        next_url = self.li_first(html.xpath("//a[@id='pageNext']/@href"))
        if next_url.find('.html') != -1:                                                    #最后一页的链接是javascript:;终止爬取
            response = self.send_request(urllib.parse.urljoin(self.host,next_url))
            self.parse_request(response) 
        
    #写入文件    
    def write_content(self, response, name, path):
        print(f'下载《{name}》完成...')
        with open(f'{path}/{name}.jpg', 'wb') as f:
            f.write(response.content)

    def start(self): 
        start_url = '4623_57562_2.html'           #爬取起始页
        self.url = urllib.parse.urljoin(self.host, start_url)
        response = self.send_request(self.url)
        if response:
            self.parse_request(response)

if __name__ == '__main__':
    start = time.time()
    sgs = BizhiSpider()
    sgs.start()
    end = time.time()
    print('爬取桌面壁纸完成，耗时%.2fs！' % (end-start))
