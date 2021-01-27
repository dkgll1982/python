#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-04-25 17:18:07 
# @Remark: 人生苦短，我用python！

from queue import Queue
import requests
import time
import sys
import os
from threading import Thread
import re
import random
import uuid 

# 生产者
class product(Thread):
    def __init__(self,name,params_queue,data_queue):
        super().__init__()
        self.url = "https://search.jiayuan.com/v2/search_v2.php"
        self.headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        }
        self.name = name
        self.params_queue = params_queue
        self.data_queue = data_queue
        
    def run(self):
        while True:
            if not self.params_queue.empty():
                parames = self.params_queue.get()
                #传入的是post参数
                if isinstance(parames,dict):
                    response = requests.post(url = self.url,headers = self.headers,data=parames)
                    self.data_queue.put(response.text)
                #传入的图片的URL地址
                else:
                    response = requests.get(parames,headers = self.headers)
                    self.data_queue.put((response.content,parames.split('/')[-1]))
                    print("%s——图片地址:%s"%(self.name,parames))
                time.sleep(0.2)
            else:
                self.data_queue.put('stop')
                break 

# 消费者
class custom(Thread):
    def __init__(self,name,params_queue,data_queue):
        super().__init__()
        self.name = name
        self.params_queue = params_queue
        self.data_queue = data_queue
        self.base_dir = r'backup\爬虫\世纪佳缘'
        
    def run(self):
        while True:
            if not self.data_queue.empty():
                data = self.data_queue.get()
                if data == 'stop':
                    break
                #获取到的是接口请求返回的文本
                if isinstance(data,str): 
                    pattern = re.compile(r'"image":.*?"(.*?)",', re.S)
                    #解析图片url地址
                    url_list = re.findall(pattern,data)
                    for url in url_list:
                        self.params_queue.put(url.replace('\\',''))
                #获取到的请求的图片的二进制数据
                else: 
                    self.wtite_content(os.path.join(self.base_dir,data[1]),data[0],'wb')
                    print("%s——下载图片%s完成！"%(self.name,data[1]))
                time.sleep(0.1)
    #写入文件
    def wtite_content(self,path,content,mode = 'w'):
        with open(path,mode) as f:
            f.write(content) 

class JiaYuanSpider():
    def __init__(self):
        super().__init__()
        self.params_queue = Queue()     #请求的参数
        self.data_queue = Queue()       #返回的数据
     
    def start(self):
        for i in range(10):
            form_data = {
                "sex":"f",
                "key":"",
                "stc":"1:42,2:20.28,23:1",
                "sn":"default",
                "sv":"1",
                "p":str(i),
                "f":"",
                "listStyle":"bigPhoto",
                "pri_uid":"0",
                "jsversion":"v5",
            }
            self.params_queue.put(form_data)
        
        for x in range(5):    
            pro = product(f'爬虫{x}号',self.params_queue,self.data_queue)
            pro.start()
        
        for x in range(5):
            cus = custom(f'解析{x}号',self.params_queue,self.data_queue) 
            cus.start()
        pro.join()
        cus.join()
            
if __name__ == "__main__": 
    start = time.time()
    jys = JiaYuanSpider()
    jys.start()
    end = time.time()
    print("爬取耗时%.2fs"%(end-start))