#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-03-24 09:56:27 
# @Remark: 人生苦短，我用python！

import requests
from lxml import etree 
import time 
from urllib import parse
import os
import random

class ZuoWenSpider():
    def __init__(self):
        super().__init__()
        self.host = 'https://www.99zuowen.com' 
        self.url = parse.urljoin(self.host,'/xiaoxuezuowen')
        self.headers = {
            "Content-type":"application/json;charset=UTF-8",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36"
        }
        self.base_dir = r'backup/爬虫/作文'
        if not os.path.exists(self.base_dir):
            os.mkdir(self.base_dir)
            
        # #免费代理    
        # self.proxy_list = [
        #     {"http": "113.121.66.221:9999"},
        #     {"http": "222.189.190.68:9999"},
        #     {"http": "39.108.71.144:9999"},
        #     {"http": "182.35.83.9:9999"},
        # ]  

    #发送请求
    def send_request(self,url):
        #proxy = random.choice(self.proxy_list)
        try:
            response = requests.get(url = url,headers = self.headers,proxies = None)
            if response.status_code == 200: 
                return response
            else:
                print('URL:{},状态码:{}'.format(response.url,response.status_code))
        except Exception as e:
            print(e)
    
    #解析分类
    def parse_request(self,response):
        html =  etree.HTML(response.content)
        a_list = html.xpath("//div[@class='wrapper']/div[@class='main_box main_wu clearfix']/div[@class='col260']/dl[@class='type_list2'][1]/dd/a")
        #注意：reverse方法没有返回值，但是会对列表的元素进行反向排序。不能用 l = a_list.reverse()，返回值一定是None
        a_list.reverse()
        
        for a in a_list:
            time.sleep(10)              #爬太快只有一个后果，IP被禁止访问
            href = a.xpath('./@href')
            title = a.xpath('./text()') 
            
            list_url = parse.urljoin(self.host,href[0]) 
            dir = self.base_dir+'/'+title[0]
            if not os.path.exists(dir):
                os.mkdir(dir)
            #进入列表页
            list_res = self.send_request(list_url) 
            if list_res:
                self.parse_request_list(list_res,title[0])
            print('{}作文全部下载完成！'.format(title))
    
    #解析列表      
    def parse_request_list(self,response,type):
        html =  etree.HTML(response.content)
        a_list = html.xpath("//div[@class='main']/div[@id='left']/div[@class='list']/div[@class='article']//li[@class='lis']")
        for a in a_list:
            href = a.xpath('./h4/a/@href')          #文章链接地址   
            detail_url = parse.urljoin(self.host,href[0])  
            #进入详情页
            detail_res = self.send_request(detail_url) 
            if detail_res:
                self.parse_request_detail(detail_res,type) 
        page_index = html.xpath("//li[@class='thisclass']/text()")
        print('[{}]类别作文第{}页下载完成！'.format(type,page_index[0]))
        
        #下一页的链接地址
        next_href = html.xpath("//div[@class='page']/ul/li[last()-1]/a/@href")  
        if next_href:       #分析页面源码，发现末页没有a标签，此时则会终止请求
            time.sleep(5)
            next_url = parse.urljoin(response.url,next_href[0])  
            next_res = self.send_request(next_url)
            if next_res:
                self.parse_request_list(next_res,type)  #请求下一页
            
    #解析详情页      
    def parse_request_detail(self,response,type):
        html =  etree.HTML(response.content)
        title = html.xpath("//div[@class='main']/div[@id='left']/div[@class='art']/div[@class='text']/div[@class='title']/h1/text()")[0]\
                .replace('"','').replace('\\','').replace('?','')
        content = ''.join(html.xpath("//div[@id='left']/div[@class='art']/div[@class='text']/div[@class='content']/div[1]//p//text()"))
        path = self.base_dir + '/' + type + '/' + title + '.txt'
        self.write_content(path,content)
    
    #写入文件
    def write_content(self,path,content):
        with open(path,'w',encoding='utf8') as f:
            f.write(content)

    def start(self):
        response = self.send_request(self.url)
        if response:
            self.parse_request(response)
        
if __name__ == "__main__":
    print('开始爬取作文...')
    start = time.time()
    zws = ZuoWenSpider()
    zws.start()
    end = time.time()
    print('爬取全部作文完成，耗时%.2fs'%(end-start))