#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-03-15 17:25:36 
# @Last Modified by: guojun 
# @Last Modified time: 2020-03-15 17:25:36 
# @Software: vscode 

import time
import requests
from lxml import etree
import os  

class DouTuLaSpider(object):
    def __init__(self):
        super().__init__() 
        self.file_path = r'backup/爬虫/斗图啦'
        self.url = "http://www.doutula.com/article/list/?page="
        #防爬首先查询cookie、refer，再找其他没有见过的项
        self.headers = {
            "Referer":self.url+"5",
            "cookie":'__cfduid=d7d72f8b03192fac40e2387e6bb314e0b1584268107; XSRF-TOKEN=eyJpdiI6InZ6R1FrN21YdVF1VTNxOWtzNWQyTWc9PSIsInZhbHVlIjoiVHRRSDBwSTJWRU56ck5DVXRSdGxwUld6VktwTnRiSjhrNHdUMmhzOXBVeEM0K3Rma011UkNaV0dJYk9XbXBZTCIsIm1hYyI6IjQwNGNhZjRjNTcyN2U2MzA2NjU4OWM1ZWYwZjUwNmYwNmMyZjMzM2Q1NTA2OWE5N2VjMTM3MzkxYmJjNzEzOGYifQ%3D%3D; doutula_session=eyJpdiI6IklPUDAzK3FjVTFxSEFFMVwvWHZoa3VBPT0iLCJ2YWx1ZSI6IkNrdkdcL2JBRldQZmNBeCtzRVwvM1c4cllcL083ZDFFNEZkVVRaVTV1TFdUZnhPS1ljNVE3b1FWaEJ0MmZuTm5DbkUiLCJtYWMiOiIyOTA3OTk3NmIyNDA4MjA5NDg5ZTA5NTg1NzE0MWI1NDg2NWVlOWRjZmMxNGNkYmNlZmIzYzk5YmRlYzM5ZTczIn0%3D; UM_distinctid=170df6ec42c5c9-02dc0cb085ca95-4e470b28-144000-170df6ec42d547; CNZZDATA1256911977=550298460-1584266568-%7C1584266568; _ga=GA1.2.1517288126.1584296543; _gid=GA1.2.1280536584.1584296543; _gat=1; __gads=ID=b28edca797508a5f:T=1584268109:S=ALNI_MbdtdHF4vRksWgyq_fFhCOCtCL0dg; _agep=1584296545; _agfp=3ae1c753496f665026fe74125b4fa10f; _agtk=2d6a9b030a2ac15953f8d75d9835ed88',
            "user_agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'
        }
        if not os.path.exists(self.file_path):
            os.mkdir(self.file_path) 
    
    def send_request(self,url):
        print('当前请求Url:%s'%url)
        return requests.get(url,headers = self.headers)
    
    def parse_request(self,response): 
        if response.status_code == 200:
            content = response.text
            html = etree.HTML(content)
            a_list = html.xpath("//a[@class='list-group-item random_list']") 
            for item in a_list:
                #要注意/和//的区别，其中/用于获取直接子节点，//用于获取子孙节点
                title = item.xpath("./div[1]/text()")       #套图目录名称
                pic_list = item.xpath('.//img/@data-backup')   
                if title: 
                    full_path = self.file_path+'\\'+title[0]
                    try:
                        if not os.path.exists(full_path):
                            os.mkdir(full_path) 
                        # enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，
                        # 同时列出数据和数据下标，一般用在 for 循环当中， enumerate() 方法的语法:
                        # enumerate(sequence, [start=0])
                        for index, pic in enumerate(pic_list, start=1):
                            response = self.send_request(pic)       # 发送图片请求 
                            name = str(index) + "_" + pic[-20:]     # 图片名字
                            self.write_content(response,name,full_path) 
                    except Exception as e:
                        print(e)
        else:
            time.sleep(5)
            print(response.status_code)

    def write_content(self, response, name, path):
        time.sleep(0.2)
        print('正在写入%s' % name)
        with open(path + '/' + name, 'wb') as f:
            f.write(response.content)
    
    def start(self,page_count):
        for i in range(2,page_count): 
            req = self.send_request(self.url+str(i))          #发送请求
            self.parse_request(req)                           #解析HTML

if __name__ == '__main__':
    page_count = 20
    start = time.time()
    dtl = DouTuLaSpider()
    dtl.start(page_count)
    end = time.time()
    print('下载图片完成，耗时%.2fs!'%(end-start))
    