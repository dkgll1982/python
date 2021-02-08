#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-05-14 20:44:07 
# @Remark: 人生苦短，我用python！
# 参考链接：Python3 爬虫实战 — 58同城武汉出租房【加密字体对抗】:https://cloud.tencent.com/developer/article/1611414

import base64
from io import BytesIO
from PIL import Image,ImageDraw,ImageFont

from lxml import etree
from fontTools.ttLib import TTFont
from urllib import parse
import time,os,sys,requests,re

class city58spider():
    def __init__(self):
        super().__init__()
        self.host = 'https://changxing.58.com'
        self.first_url = '/chuzu/?PGTID=0d100000-0034-2f5f-8be2-3bd3947635b4&ClickID=2'
        self.other_url = '/chuzu/pn{}/?PGTID=0d100000-0034-2f5f-8be2-3bd3947635b4&ClickID=2'
        self.url = parse.urljoin(self.host,self.first_url)
        self.base_dir = r'backup/爬虫/58city/'
        self.font_path = os.path.join(self.base_dir,'font/textwoff.woff')
        self.headers = {   
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        }
        
    def send_request(self,url):
        response = requests.get(url = url,headers = self.headers)  
        response.encoding='utf8' 
        if response.status_code== 200:
            return response
        else:
            print('URL：{}，状态码：{}'.format(url,response.status_code))
            
    def parse_content(self,response):
        content = response.text
        html = etree.HTML(content)
        list = html.xpath("//li[@class='house-cell']")
        
        #首先获取字体文件
        #括号是转义字符，可以用'\)'代替
        partten = re.compile("base64,(.*?)'\)")
        base64_string = re.findall(partten,content)  
        #self.download_font(base64_string[0])        
        #将base64编码的字体字符串解码成二进制编码
        bin_data = base64.decodebytes(base64_string[0].encode())
        cmap = self.get_font(bin_data)
        
        print(cmap)
        #获取价格，此处或是乱码，但用正则取出来的转义的字符
        pattern1 = re.compile(f'<b class="strongbox">(.*?);</b>元', re.S) 
        for ind,li in enumerate(list,start=0):
            title = ''.join(li.xpath(".//div[@class='des']/h2/a[@class='strongbox']/text()")).replace('\n','').replace(' ','')
            street = ''.join(li.xpath(".//div[@class='des']/p[@class='infor']/a[1]/text()"))
            area = ''.join(li.xpath(".//div[@class='des']/p[@class='infor']/a[2]/text()"))
            price = li.xpath(".//div[@class='list-li-right']/div[@class='money']/b[@class='strongbox']/text()")[0]
             
            price = re.findall(pattern1, content)[ind] 
            result = self.parse_font(cmap,price)
            print(f'标题：{title}，商圈：{street}，小区：{area},价格：{result}') 
    
    #下载字体文件    
    def download_font(self,base64_string:str):
        #将base64编码的字体字符串解码成二进制编码
        bin_data = base64.decodebytes(base64_string.encode())
        with open(self.font_path,'wb') as f:
            f.write(bin_data) 
            
     #发起字体请求
    def get_font(self,content): 
        font = TTFont(BytesIO(content))          #获取字体
        cmap = font.getBestCmap()                #获取字体name和code的对照关系
        newdict = {}
        for i in cmap:
            pat = re.compile(r'(\d+)')
            values = int (re.search(pat,cmap[i])[1]) - 1
            keys = hex(i)
            newdict[keys] = values
        font.close() 
        return newdict 
    
     #解析字体
    def parse_font(self,cmap,content): 
        result = ''
        for item in content.split(';'):
            var = cmap["0%s"%item[2:]]
            result += str(var)
        return result

    def start(self):
        for x in range(1,10):
            if x > 1: 
                self.url = parse.urljoin(self.host,self.other_url.format(x))
            response = self.send_request(self.url)
            if response:
                self.parse_content(response)
            time.sleep(3)

if __name__ == "__main__":
    city58s = city58spider()
    city58s.start()