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
        self.max_page = 100
        self.city = 'wh'    #wh:武汉，bj:北京
        self.host = "https://"+self.city+".sofang.com/new/area/"
        self.url = self.host + "bl{}?"
        self.page_num = 100
        #防爬首先查询cookie、refer，再找其他没有见过的项
        self.headers = { 
            "cookie":'uniqueName=1613eefacba1d74c56f84206fc181a6d; UM_distinctid=170e71fc6b95eb-05751ca57af9ce-4313f6a-144000-170e71fc6ba4d5; codeNum=eyJpdiI6Im1MRjh5SGlJVDNFajRaSktDanI3clE9PSIsInZhbHVlIjoiY3R1TGpQVXpsaHA2Zm1TUkI0dlljZUZFS25nbVJIY2pSM3lPRDlpWUErR2VjUENvbTlieWRFR2pTNElkeFBsZyIsIm1hYyI6ImY5Zjc2NTVkNDAwMGUyOGMzMDU2YmE4M2ZhODRhZDEwYTZiY2FiMGYyMjY4YTUyMDUzMzgyNWQ4OGIyNTUzYjMifQ%3D%3D; Hm_lvt_d2801fc638056c1aac7e8008f41cf828=1584425885; CNZZDATA1262285598=283037522-1584423373-%7C1584766743; XSRF-TOKEN=eyJpdiI6InM2UkgyR05sWmJ4dFNHbDlRTEFrUlE9PSIsInZhbHVlIjoiXC9qSjJOSEd6U3RTRDNnVTZ5TlhuNnVUam53VUNLajl5N3JHdTlmYW1JTndHcjhEWWtwQW50YjZGTWI2aEpDcnd6clk1YkIzQkhCUjVpRDBzaW9kdnV3PT0iLCJtYWMiOiIzM2ZkYjQwYjQyNTQ0MmM4MzliNWZmMWQyZjhiMDUzNDNhZTNiZDYzZjczMTdiNDQ5YmQ2YTQ1NjVjODdmYWZiIn0%3D; www_sofang_session=eyJpdiI6IkNJV1wveEdtcWFWZnpUUlwvMjZyemQ5Zz09IiwidmFsdWUiOiI4WnhIWFZJbGEyY29ROSt3ejczM2FESG5uRU1uazZQYXFGYlMweGlyeW5aMWkxTkFLRHluMGZGV2YwVkxHNTg2aEpSaU8zUWpJRWZVZFBrZVpCTmk3dz09IiwibWFjIjoiMjRiMzcxYTk3ZjUyMTk0Mzk1MTE3NDNlOTVmY2QzMjFjZjQ1MWM4YWY1YWQ4Y2Q4NmM5OWRjYzc5Nzc4ODFhOSJ9; cityid=eyJpdiI6Ik9KclZzSDQzOHdoMzlxUk9jaDMrTVE9PSIsInZhbHVlIjoiTE1PczJZbU1cL0lyTnYxY3F1dWlkYXc9PSIsIm1hYyI6IjA0YmM4NzlhZmJhZGZhMGMxYjZmOTE2YjNhZDNlZDQ2MjkwZDY4MDM5YTQ4NWZmNWExZDFlM2U1ZWUwYTlhYmMifQ%3D%3D; city=eyJpdiI6IjlKNTRxa0liY1M2SnNWWHlPRWR2emc9PSIsInZhbHVlIjoiNU9cL2lRWlNYVzUxZE16TDBjMDA1WnNMSzZMNkw3MkI2Y1wvelNGZ0dOMStSUU1ZVjlIMk1UR2czdlMwTE9INEp6VkxjTlh1dytJMWlEbHBzXC9zcXQ5SEhVOHJuMGgrS0cxNFE2SWxTaEFGQzdpa28zSllWNE1uRDA2MXdYWGZOWThXNkZVck93a01ONVFHazBCZTVZa2x0ejlpdndjWFpua2VVcE1tRG54aGVudHVVOFB1bGprSWllNEtYR3RVcXhUVFBPSXJPVkdVREdwaHRURjE3cXdIVFFoZEw1dUx5QmtobzI5VTFIbUxTRzdSc2orcDJ0elcybFNXbUk2WGYxUXZMVG02cFF0TnhVVFpyZ3QwTjFJTTZ2bjBJXC9kMis5MVdCNlBSNGxQUHQ0PSIsIm1hYyI6IjVkMWM1OTIzOTIzOGE5MTY1NjY1OGFhMTgzNTQyMGE0NDk3MTE4OTAxNjVjMjY0MGFiZTUzYWI2Yjc2ZjEzZjUifQ%3D%3D; citypy=eyJpdiI6IkttVEZHalVZdDlaT0JOXC9iOXRLbWFBPT0iLCJ2YWx1ZSI6IkVFN3FRVHcyVEFKb2QyRVdtbkg1MkE9PSIsIm1hYyI6ImExNjQxMWM4MDMxM2RiYjhlZGYzZDQyMWM4N2NiODFiOTQ5MGE2NjIwMTc3NjU2YzU3YzMzOTNlZDEwYmE3MWEifQ%3D%3D',
            "referer":'https://wh.sofang.com/new/area',
            "user_agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'
        } 
        #建表语句
        # CREATE TABLE BASE_SF_HOUSE
        # (
        #     city  varchar2(200),
        #     IMG  varchar2(2030),
        #     title  varchar2(200),
        #     quyu varchar2(200),
        #     address varchar2(200),
        #     type varchar2(200),
        #     wuyefei varchar2(200),
        #     unit_price varchar2(200)
        # )
    
    def send_request(self,url):
        return requests.get(url,headers = self.headers)
    
    def parse_request(self,response,cursor,pagenum): 
        if response.status_code == 200: 
            content = response.content
            html = etree.HTML(content) 
            if pagenum == 1: 
                self.page_num = int(html.xpath('//div[@class="page_nav"]//a[last()]/@alt')[-1:][0])  #取页码
            li_list = html.xpath('//div[contains(@class,"list_free")]/dl') 
            house = {}
            for li in li_list:
                house["img"] = self.first(li.xpath(".//dt//img/@src"))
                house["title"] = self.first(li.xpath(".//dd[@class='house_msg']//a[1]/text()"))
                house["quyu"] = self.first(li.xpath(".//dd[@class='house_msg']//span[@class='build_sq']/span[1]/text()"))
                house["address"] = self.first(li.xpath(".//dd[@class='house_msg']//span[@class='address']/text()"))
                house["type"] = self.first(li.xpath(".//dd[@class='house_msg']//p[@class='type clearfix']/span[1]/text()")) 
                house["wuyefei"] = self.first(li.xpath(".//dd[@class='house_msg']//p[@class='type clearfix']/span[3]/text()")) 
                house["unit_price"] = self.first(li.xpath(".//dd[@class='house_price']//span[@class='font']/text()")) 
                #print(house)     
                sql = "insert into BASE_SF_HOUSE(city,img,title,quyu,address,type,wuyefei,unit_price)"\
                    " values('{}','{}','{}','{}','{}','{}','{}','{}')".format(self.city,house["img"],house["title"],
                    house["quyu"],house["address"],house["type"],house["wuyefei"],house["unit_price"])
                      
                cursor.execute(sql)         #插入数据
                
        else:
            print(response.status_code)

    #返回列表第一条
    def first(self,list):
        return list[0].replace('\r\n','').strip() if list else '' 
    
    def start(self):
        #ORACLE连接参数
        conn = cx_Oracle.connect('cigproxy','cigproxy','localhost/orcl')
        cursor = conn.cursor() 
        
        cursor.execute("delete from BASE_SF_HOUSE where city='{}'".format(self.city))            #删除数据
        
        for i in range(1,self.max_page):  
            if i > self.page_num:break
            req = self.send_request(self.url.format(str(i)))     #发送请求
            self.parse_request(req,cursor,i)                     #解析HTML 
            conn.commit() 
            print('爬取第{}/{}页数据成功！'.format(i,self.page_num))
            time.sleep(2)  
         
        conn.commit() 
        cursor.close()
        conn.close()   

if __name__ == '__main__':
    start = time.time()
    dtl = AnaimalSpider()
    dtl.start()
    end = time.time()
    print('获取房价信息完成，耗时%.2fs!'%(end-start))
    