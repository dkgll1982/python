#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-03-16 18:40:22 
# @Last Modified by: guojun 
# @Last Modified time: 2020-03-16 18:40:22 
# @Software: vscode 

import time
import requests
from lxml import etree
import os  
import re
import cx_Oracle

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

class AnaimalSpider(object):
    def __init__(self):
        super().__init__()  
        self.host = "https://bj.lianjia.com/chengjiao/"
        self.url = self.host + "pg{}/"
        #防爬首先查询cookie、refer，再找其他没有见过的项
        self.headers = { 
            "user_agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'
        } 
        #建表语句
        #   CREATE TABLE "CIGPROXY"."BASE_LJ_HOUSE" 
        #     (	"IMG" VARCHAR2(2000 BYTE), 
        #         "DESCRIPT" VARCHAR2(2000 BYTE), 
        #         "TITLE" VARCHAR2(2000 BYTE), 
        #         "FANGXIANG" VARCHAR2(2000 BYTE), 
        #         "LOUCEN" VARCHAR2(2000 BYTE), 
        #         "CHANQUAN" VARCHAR2(2000 BYTE), 
        #         "JIANJIE" VARCHAR2(2000 BYTE), 
        #         "ZHONGJIE" VARCHAR2(2000 BYTE), 
        #         "DEALDATE" VARCHAR2(2000 BYTE), 
        #         "TOTALPRICE" VARCHAR2(2000 BYTE), 
        #         "UNITPRICE" VARCHAR2(2000 BYTE), 
        #         "CITY" VARCHAR2(200 BYTE)
        #     )
    
    def send_request(self,url):
        return requests.get(url,headers = self.headers)
    
    def parse_request(self,response,cursor): 
        if response.status_code == 200:
            content = response.content
            html = etree.HTML(content) 
            li_list = html.xpath('//ul[@class="listContent"]/li')
            house = {}
            for li in li_list:
                house["img"] = self.first(li.xpath(".//img[@class='lj-lazy']/@data-original"))
                house["descript"] = self.first(li.xpath(".//img[@class='lj-lazy']/@alt"))
                house["title"] = self.first(li.xpath(".//div[@class='title']/a/text()"))
                house["fangxiang"] = self.first(li.xpath(".//div[@class='houseInfo']/text()"))
                house["loucen"] = self.first(li.xpath(".//div[@class='positionInfo']/text()"))
                house["chanquan"] = '|'.join(li.xpath(".//span[@class='dealHouseTxt']/span/text()"))
                house["jianjie"] = '|'.join(li.xpath(".//span[@class='dealCycleTxt']/span/text()"))
                house["zhongjie"] = self.first(li.xpath(".//a[@class='agent_name']/text()"))
                house["dealDate"] = self.first(li.xpath(".//div[@class='dealDate']/text()"))
                house["totalprice"] = self.first(li.xpath(".//div[@class='totalPrice']/span[@class='number']/text()"))+'万'
                house["unitPrice"] = self.first(li.xpath(".//div[@class='unitPrice']/span[@class='number']/text()"))+'元/平'
                
                sql = "insert into BASE_LJ_HOUSE(city,img,descript,title,fangxiang,loucen,chanquan,jianjie,zhongjie,dealDate,totalprice,unitPrice)"\
                      " values('beijing','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
                      house["img"],house["descript"],house["title"],house["fangxiang"],house["loucen"],house["chanquan"],house["jianjie"],
                      house["zhongjie"],house["dealDate"],house["totalprice"],house["unitPrice"])
                      
                cursor.execute(sql)         #插入数据
                
        else:
            print(response.status_code)

    #返回列表第一条
    def first(self,list):
        return list[0] if list else '' 
    
    def start(self,page_count):
        #ORACLE连接参数
        conn = cx_Oracle.connect('cigproxy','cigproxy','localhost/orcl')
        cursor = conn.cursor() 
        
        #cursor.execute("delete from BASE_LJ_HOUSE")            #删除数据
        
        for i in range(1,page_count): 
            req = self.send_request(self.url.format(str(i)))   #发送请求
            self.parse_request(req,cursor)                     #解析HTML 
            conn.commit() 
            print('爬取第{}页数据成功！'.format(i))
            time.sleep(2)  
         
        conn.commit() 
        cursor.close()
        conn.close()   

if __name__ == '__main__':
    page_count = 100
    start = time.time()
    dtl = AnaimalSpider()
    dtl.start(page_count)
    end = time.time()
    print('获取房价信息完成，耗时%.2fs!'%(end-start))
    