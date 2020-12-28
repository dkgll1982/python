#!/usr/bin/env python 
# -*- coding:utf-8 -*-  
# @Author: suixin 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd  
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-12-08 18:51:49 
# @Remark: Life is short, I use python！

import requests
import os,time
from urllib import parse
from lxml import etree

class MzituSpider():
    def __init__(self):
        super().__init__()
        self.host = 'https://www.mzitu.com'
        self.url = parse.urljoin(self.host,'japan/page/{}/')    
        self.headers = {                                    #网页页面的header
            "Host" : "www.mzitu.com",                   
            "Referer": "https://www.mzitu.com/",
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
        }
        self.img_header= {                                  #高清大图的header
            "Host" : "imgpc.iimzt.com",                     #注意与站点不在同一个域，验证发现这里其实也可以不用设置“host”
            "Referer": self.headers['Referer'],
            "User-Agent": self.headers['User-Agent']
        }
        self.base_dir = r'backup\爬虫'
        #保存文件的位置
        self.path = os.path.join(self.base_dir,'妹子图')
        if not os.path.exists(self.path):
            os.makedirs(self.path)
       
    #发送请求    
    def send_request(self,url,headers): 
        response = requests.get(url = url,headers = headers,timeout = 20)
        if response.status_code == 200:
            return response 
        else:
            print('URL：{}，状态码：{}'.format(url,response.status_code))
    
    #解析请求
    def parse_request(self,response):
        html = etree.HTML(response.content)
        img_list = html.xpath("//ul[@id='pins']/li/span/a")
        for img in img_list:
            name = img.xpath("text()")[0].replace('?','').replace(' ','')
            href = parse.urljoin(self.host,img.xpath("@href")[0]) 
            self.parse_detail(name,href) 
    
    #解析详情页
    def parse_detail(self,name,href,index=1):
        res = self.send_request(href,self.headers)                   #爬取详情页  
        if res: 
            detail_html = etree.HTML(res.content) 
            img = detail_html.xpath("//img[@class='blur']/@src")[0]    
             
            img_res = self.send_request(img,self.img_header)         #下载图片,保存到本地
            if img_res:
                img_path = os.path.join(self.path,name)
                if not os.path.exists(img_path):
                    os.mkdir(img_path)
                self.write_content(img_path,index,img_res.content)            
            
            print(f'爬取套图【{name}】第{index}张成功,地址：{img}')  
            time.sleep(0.001)                             #爬取太快会报：429 Too Many Requests (太多请求)的错误
            next_link = detail_html.xpath("//div[@class='pagenavi']//span[starts-with(text(),'下一页')]/parent::*")            
            if len(next_link)>0:                          #存在下一页则继续爬
                index = index + 1
                sub_href = next_link[0].xpath("@href")[0]
                self.parse_detail(name,sub_href,index)  
    
    #保存文件
    def write_content(self,path,name,content):
        with open(f'{path}/{name}.jpg', 'wb') as f: 
            f.write(content)
            
    def start(self): 
        page_count = 50                                   #设置爬取多少页
        for x in range(1,page_count+1): 
            start_url = self.url.format(x)
            print(f'开始爬取的第{x}页地址:{start_url}')
            response = self.send_request(start_url,self.headers)
            if response:
                self.parse_request(response)

if __name__ == "__main__":
    mzts = MzituSpider()
    start = time.time()
    mzts.start()
    end = time.time()
    print('爬取妹子图完成，耗时%.2fs！' % (end-start))