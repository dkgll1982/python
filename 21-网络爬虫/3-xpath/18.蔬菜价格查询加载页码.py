#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-03-20 15:36:19 
# @Last Modified by: guojun 
# @Last Modified time: 2020-03-20 15:36:19 
# @Software: vscode 

import lxml
import requests
from requests import HTTPError
import time
import os
import cx_Oracle
import json

def json_append(file_name,key,json_data,pageNum):  
    with open(file_name,'a+',encoding="utf-8") as f: 
        # 因为是追加方式打开，默认偏移量再最后面，我们调整到开头
        f.seek(0)                       
        data = {} 
        # 判断是否为空且是第一次讀取json 
        if f.read() !='' and pageNum != 0: 
            f.seek(0)
            data = json.load(f)  
            if data[key]:  
                data[key][len(data[key]):len(data[key])] = json_data[key]
            else: 
                data[key] = json_data[key] 
        else:
            data = json_data  
        #print('{}添加后的值：{}'.format(key,data))
            
        # 设置文件当前位置 0代表开始处 其实有两个参数 offset,whence （whence常用有三个参数0，1，2；0 代表从文件开头开始算起，1 代表从当前位置开始算起，2 代表从文件末尾算起。）
        f.seek(0)                       
        # 如果操作成功，则返回新的文件位置，如果操作失败，则函数返回 -1。
        # 从开头截断，截断文件为size个字符，无参代表 从当前位置截断，截断之后后面的所有字符都被删除
        f.truncate()                    
        json.dump(data,f,indent=2,ensure_ascii=False)
        
class ShuCaiSpider():
    def __init__(self):
        self.url = 'http://www.cncyms.cn/pages.php'
        self.headers = {
            "user_agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
        }
        #查询的蔬菜品名
        self.pname = '黄瓜'
        #根据页码自动加载,本例暂定加载最多100页
        self.max_pagesize = 150
    
    def send_request(self,pageNum=0):
        form_data={
            "pageNum": pageNum,
            "pname": self.pname,        #为空查询所有蔬菜
            "reltime": "蔬菜"
        }
        req = None
        try:
            #连接超时时间10s
            req = requests.post(self.url,data=form_data,headers=self.headers,timeout=10) 
        except Exception as e:
            print('爬取第{}页{}价格失败，原因：{}'.format(pageNum,self.pname,e)) 
        return req
    
    def parse_request(self, response, pageNum = 0):
        if response.status_code == 200:
            json_content = response.json()
            self.write_content(json_content,pageNum)
            return json_content["totalPage"]
        else:
            print(response.status_code)
            return 0
    
    def write_content(self,json_content,pageNum):
        file_name = r'backup\爬虫\蔬菜网\price_{}.json'.format(self.pname)
        key = 'list' 
        json_append(file_name,key,json_content,pageNum)

    def start(self,pagenum):
        #首次获取页码
        req = self.send_request()
        if req:
            num = self.parse_request(req)
            print('爬取第1页{}价格成功！'.format(self.pname))
            num = self.max_pagesize if num > self.max_pagesize else num
            for x in range(1,num):
                req = self.send_request(x)
                if req:
                    self.parse_request(req,x)
                    print('爬取第{}/{}页{}价格成功！'.format(x+1,num,self.pname))
            

if __name__ == '__main__':
    start = time.time()
    scs = ShuCaiSpider()
    scs.start(10)
    end = time.time()
    
    print('爬取%s数据完成，耗时%.2fs!'%(scs.pname,end-start))

    