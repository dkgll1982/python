#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-03-29 15:39:23 
# @Remark: 人生苦短，我用python！

import requests
from urllib import parse
import re
from lxml import etree
import os
import time
import cx_Oracle
import json
import copy

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

class CarSpider():
    def __init__(self):
        super().__init__()
        self.host = 'https://www.autohome.com.cn'
        self.url = parse.urljoin(self.host,'/all/{}/#liststart')
        self.comment_url='https://reply.autohome.com.cn/api/getData_ReplyCounts.ashx'   #获取评论数的URL
        self.base_dir = r'backup/爬虫/汽车之家'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36', 
        } 
        self.params ={
            "appid": "1",
            "dateType": "jsonp" 
        }
        if not os.path.exists(self.base_dir):
            os.mkdir(self.base_dir)
        #ORACLE连接参数
        self.conn = cx_Oracle.connect('cigproxy','cigproxy','localhost/orcl')
        self.cursor = self.conn.cursor() 
        #建表语句
        # create table base_CAR_INFO
        # (
        #     objid varchar2(20),
        #     title varchar2(200),
        #     pub_time  varchar2(200),
        #     liulan_num varchar2(200),
        #     c_num varchar2(200),
        #     descript varchar2(2000)
        # )
        
    #发送请求
    def send_request(self,url,params = None):
        response = requests.get(url = url,headers = self.headers,params = params)
        if response.status_code == 200:
            return response
        else:
            print('URL：{}，状态码：{}'.format(url,response.status_code))
    
    #解析请求
    def parse_content(self,response):
        html = etree.HTML(response.content)
        li_list = html.xpath('//div[@id="auto-channel-lazyload-article"]/ul//li') 
        dict,para = [],{}
        for li in li_list:
            #获取文章ID，特殊属性注意需要用小写表示，可能是bug
            objid = li.xpath(".//em[contains(@data-class,'icon12-infor')]/@data-articleid")
            if objid:
                para["objid"] = objid[0]                                                     #文章ID
                para["title"] = li.xpath('.//h3/text()')[0]                                  #标题
                para["pub_time"] = li.xpath('.//span[@class="fn-left"]/text()')[0]           #发表时间
                para["liulan_num"] = li.xpath('.//span[@class="fn-right"]/em[1]/text()')[0]  #浏览量
                para["descript"] = li.xpath('.//p/text()')[0]                                #文章描述
                self.params["objids"] = objid[0]
                comment_response = self.send_request(self.comment_url,params = self.params)  #获取评论数
                para["c_num"] = "0"
                if comment_response:
                    result = json.loads(comment_response.text.replace('\'','"').replace('(','').replace(')',''))  
                    para["c_num"] = result["commentlist"][0]["replycount"]                   #评论数
                dict.append(copy.deepcopy(para))
        self.insert_records(dict)      
        self.conn.commit()           
    
    # 执行添加记录的SQL    
    def insert_records(self,params):
        sql = """INSERT INTO base_CAR_INFO(objid,title,pub_time,liulan_num,c_num,descript) 
                 SELECT :objid,:title,:pub_time,:liulan_num,:c_num,:descript FROM DUAL"""
        self.cursor.executemany(sql,params) 
    
    def start(self):
        for x in range(1,101):
            response = self.send_request(self.url.format(x))
            if response:
                self.parse_content(response)
            time.sleep(1)
            print('第{}页文章爬取完成！'.format(x))
        
        print('全部文章爬取完成！')
        self.cursor.close()
        self.conn.close()      
            
if __name__ == "__main__":
    start = time.time()
    cars = CarSpider()
    cars.start()
    end = time.time()
    print('爬取汽车之家文章完成，耗时%.2fs'%(end-start))