#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-05-02 13:16:59 
# @Remark: 人生苦短，我用python！

from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
from fontTools.ttLib import TTFont
from io import BytesIO,StringIO
from lxml import etree
from urllib import parse
import time,os,sys,requests,re,random

class QiDianSpider():
    def __init__(self):
        super().__init__()
        self.host = 'https://www.qidian.com'
        self.url = parse.urljoin(self.host,'all?orderId=&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=0&page=')
        self.page_count = 5
        self.base_dir = r'backup/爬虫/小说'
        self.headers = {   
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        }
    
    def send_request(self,url):
        response = requests.get(url,headers = self.headers)       
        response.encoding='utf8' 
        if response.status_code == 200:
            return response
        else:
            print('URL：{}，状态码：{}'.format(url,response.status_code))
    
    def parse_content(self,response): 
        text = response.text
        html = etree.HTML(text)
        li_list = html.xpath("//ul[@class='all-img-list cf']//li")
        results = []
            
        #获取字体
        pattern = re.compile(r"<style>.*?font-family:(.*?);", re.S) 
        font_name = re.findall(pattern, text)[0].lstrip()
        font_url = 'https://qidian.gtimg.com/qd_anti_spider/' + font_name + '.ttf'                              #字体链接    
        
        #获取文字数
        pattern1 = re.compile(f'<span.*?class="{font_name}">(.*?)</span>', re.S)
        nums = re.findall(pattern1, text)                                                                     #小说字数
            
        for index,li in enumerate(li_list):
            title = li.xpath("./div[@class='book-mid-info']/h4/a/text()")                                       #标题
            author = li.xpath("./div[@class='book-mid-info']/p[@class='author']/a[@class='name'][1]/text()")    #作者
            state = li.xpath("./div[@class='book-mid-info']/p[@class='author']/span/text()")                    #小说状态
            src = li.xpath("./div[@class='book-img-box']/a/img/@src")                                           #图片地址
            description = li.xpath("./div[@class='book-mid-info']/p[@class='intro']/text()")                    #简述 
            results.append(
                {
                    "title":title[0],
                    "author":author[0],
                    "state":state[0],
                    "src":src[0],
                    "description":description[0].replace('\r','').strip (' '),
                    "num":nums[index][:-1],
                    "font_url":font_url
                }
            )
        return results
    
    #发起字体请求
    def get_font(self,url):
        response = requests.get(url)
        font = TTFont(BytesIO(response.content)) #获取字体
        cmap = font.getBestCmap()                #获取字体name和code的对照关系
        font.close() 
        return cmap
    
    #解析字体
    def parse_font(self,cmap,content):
        word_map = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7',
                'eight': '8', 'nine': '9', 'period': '.'}
    
        result = ''
        for item in content.split(';'):
            key = cmap[int(item[2:])]
            result += word_map[key]
        return result

    def write_content(self,path,content):
        with open(path,'a+') as f:
            f.write(content)
        
    def start(self):
        with ThreadPoolExecutor(max_workers = 20) as pool:
            url_list = [] 
            for x in range(1,self.page_count):
                url_list.append(self.url+str(x))
            future = pool.map(self.send_request,url_list)           #多线程并行请求多页数据
            for ind,response in enumerate(future,start=1):
                results = self.parse_content(response)              #返回请求后的结果进行解析
                font_urls = [i['font_url'] for i in results]
                cmap = pool.map(self.get_font,font_urls)            #获取每一条数据对应的字体信息
                for index,c in enumerate(cmap):
                    num = self.parse_font(c,results[index]["num"])  #解析每一条字体，提取信息
                    results[index]["num"] = num
                print(f'爬取第{ind}页成功!')
                path = os.path.join(self.base_dir,'起点.txt')
                self.write_content(path,str(results))
            
if __name__ == "__main__":
    qds = QiDianSpider()
    qds.start()