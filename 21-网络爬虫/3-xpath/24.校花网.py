#!/usr/bin/env python 
# -*- coding:utf-8 -*-  
# @Author: suixin 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd  
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-12-07 16:17:47 
# @Remark: Life is short, I use python！

import requests
import os,sys,time
from urllib import parse
from lxml import etree

class XiaoHuaSpider():
    def __init__(self):
        super().__init__()
        self.base_dir = r'backup/image'
        self.host = 'http://www.xiaohuar.com'
        self.url = parse.urljoin(self.host,'daxue/index{}.html')
        self.headers = {
            "Host": "www.xiaohuar.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36"
        }
        #保存文件的位置
        self.path = os.path.join(self.base_dir,'校花网')
        if not os.path.exists(self.path):
            os.mkdir(self.path)
       
    #发送请求    
    def send_request(self,url):
        response = requests.get(url = url,headers=self.headers,timeout=20)
        if response.status_code == 200:
            return response
        else:
            print('URL：{}，状态码：{}'.format(url,response.status_code))
    
    #解析请求
    def parse_request(self,response):
        html = etree.HTML(response.content)
        div_list = html.xpath("//div[@class='card diy-box shadow mb-5']")
        for div in div_list:
            title = div.xpath("div/a/text()")[0].replace('?','').replace(' ','')
            href = parse.urljoin(self.host,div.xpath("div/a/@href")[0])  
            img_url = parse.urljoin(self.host,div.xpath("a/img/@src")[0])   
            img_response = self.send_request(img_url)                  #发送图片请求 
            if img_response:
                self.write_content(self.path,title,img_response.content)   #下载图片
            res = self.send_request(href)                              #爬取详情页
            if res:
                detail_html = etree.HTML(res.content)
                content = ''.join(detail_html.xpath("//div[@class='picture_content']//text()")).replace('\r','').replace('\n','').replace('\t','')
                print(f"title:{title},content:{content}")
    
    #保存文件
    def write_content(self,path,name,content):
        with open(f'{path}/{name}.jpg', 'wb') as f: 
            f.write(content)
            
    def start(self): 
        page_index = 10                             #设置爬取多少页
        for x in range(page_index): 
            start_url = self.url.format('' if x == 0 else f'_{x}')
            print(f'开始爬取的第{x+1}页地址:{start_url}')
            response = self.send_request(start_url)
            if response:
                self.parse_request(response)

if __name__ == "__main__":
    xhs = XiaoHuaSpider()
    start = time.time()
    xhs.start()
    end = time.time()
    print('爬取校花图片完成，耗时%.2fs！' % (end-start))