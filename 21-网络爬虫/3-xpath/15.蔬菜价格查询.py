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
import time
import os
import cx_Oracle
import json

def json_append(file_name,key,json_data):  
    with open(file_name,'a+',encoding="utf-8") as f:
        # 因为是追加方式打开，默认偏移量再最后面，我们调整到开头
        f.seek(0)                       
        # 判断是否为空，如果为空的话创建一个新的字典格式 
        if f.read() =='':              
            data = {}
        else:
            f.seek(0)
            data = json.load(f) 
        if data:
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
    
    def send_request(self,pageNum):
        form_data={
            "pageNum": pageNum,
            "pname": '',
            "reltime": "蔬菜"
        }
        return requests.post(self.url,data=form_data,headers=self.headers) 
    
    def parse_request(self, response):
        if response.status_code == 200:
            json_content = response.json()
            self.write_content(json_content)
        else:
            print(response.status_code)
    
    def write_content(self,json_content):
        file_name = r'backup\爬虫\蔬菜网\price.json'
        key = 'list' 
        json_append(file_name,key,json_content)

    def start(self,pagenum):
        for x in range(1,pagenum):
            req = self.send_request(x)
            self.parse_request(req)
            print('爬取第{}页数据完成！'.format(x))

if __name__ == '__main__':
    start = time.time()
    scs = ShuCaiSpider()
    scs.start(10)
    end = time.time()
    
    print('爬取数据完成，耗时%.2fs!'%(end-start))

    