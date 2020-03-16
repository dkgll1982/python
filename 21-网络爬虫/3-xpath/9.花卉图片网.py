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
import re

class FlowerSpider(object):
    def __init__(self):
        super().__init__()
        self.file_path = r'backup/爬虫/花卉信息网'
        self.host = "http://www.fpcn.net"
        self.url = self.host + "/a/caobenhuahui/list_1_{}.html"
        #防爬首先查询cookie、refer，再找其他没有见过的项
        self.headers = { 
            "user_agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'
        }
        if not os.path.exists(self.file_path):
            os.mkdir(self.file_path) 
    
    def send_request(self,url):
        print('当前请求Url:%s'%url)
        return requests.get(url,headers = self.headers)
    
    def parse_request(self,response,page_count): 
        if response.status_code == 200:
            content = response.content
            html = etree.HTML(content)
            a_list = html.xpath("//a[@class='pic']") 
            
            #创建图片子目录
            dir = self.file_path+'/'+str(page_count)
            if not os.path.exists(dir):
                os.mkdir(dir) 
                            
            for index, item in enumerate(a_list, start=1): 
                title = item.xpath(".//img/@alt")       #图片名称
                pic = item.xpath('.//img/@src')         #图片地址
                try:
                    response = self.send_request(self.host+pic[0])       # 发送图片请求 
                    re_str = ''.join(re.findall(r'[\u4e00-\u9fa5]+', title[0])).replace('\n','') #有中文取中文名字，无则取标记名称
                    name = str(index)+'_'+(re_str if re_str else title[0])  
                    self.write_content(response,name,dir) 
                except Exception as e:
                    print(e)
        else:
            print(response.status_code)

    def write_content(self, response, name, path):
        print('正在写入%s' % name)
        with open(path + '/' + name+'.jpg', 'wb') as f:
            f.write(response.content)
    
    def start(self,page_count):
        for i in range(page_count): 
            req = self.send_request(self.url.format(str(i+1)))   #发送请求
            self.parse_request(req,i+1)                          #解析HTML

if __name__ == '__main__':
    page_count = 105
    start = time.time()
    dtl = FlowerSpider()
    dtl.start(page_count)
    end = time.time()
    print('下载图片完成，耗时%.2fs!'%(end-start))
    