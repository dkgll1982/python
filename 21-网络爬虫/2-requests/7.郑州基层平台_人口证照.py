#!/usr/bin/env python 
# -*- coding:utf-8 -*-  
# @Author: suixin 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd  
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-12-01 15:08:14 
# @Remark: Life is short, I use python！

import requests 
import json
from urllib import parse
import math 
from threading import Thread
import time 
import cx_Oracle
import time,datetime
import hashlib
import os
from concurrent.futures import ThreadPoolExecutor
import threading
from DBUtils.PooledDB import PooledDB

class ApiSpider(object):    
    def __init__(self): 
        super().__init__()
        self.index = 984
        #接口编码 
        self.api_code = 'zfw_zz_rkxx'                
        self.host = 'http://172.17.217.98:8086/CSB/zzubShareService/zfw'
        self.token_url = parse.urljoin(self.host,f'?_api_name=token&_api_version=1.0.0') 
        os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
        user='cigproxy'
        password='cigproxy'
        host='172.17.217.17'
        port='15227'
        sid='xe'
        dsn = cx_Oracle.makedsn(host,port,sid)
        #连接池
        self.pool = PooledDB(cx_Oracle,
                             mincached = 20,
                             blocking = True,
                             user = user,
                             password = password,
                             dsn = dsn)        
    
    #获取token
    def get_token(self):  
        headers = { 
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
            'Content-Length': '40',
            'ContentType': 'application/x-www-form-urlencoded',
            # 密钥 
            'Authorization': 'Basic YTE1NzAzZjEtMGVhYy00OTAzLWEwNTktZWM1YjcyOTM1NTIwOkEyVjVZVEUxTlpBWlpKRVRNR1ZIWVkwME9UQVpMV0VXTlRLVFpXTTFZSkNZT1RNMU5USVc='
        }
        
        data = {
            "grant_type":'client_credentials',
            "scope":"service"   
        }
        response = requests.post(url = self.token_url, headers = headers, data = data)       
        if response.status_code == 200:
            try:         
                return response.json()
            except Exception as e: 
                print('JSON解析错误：{}'.format(e))     
        else:
            print('URL：{}，状态码：{}'.format(self.token_url, response.status_code)) 
            
    #分页查询数据        
    def get_pagedata(self,token):      
        # 密钥 
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
            'ContentType': 'application/x-www-form-urlencoded',  
            'Authorization': "bearer b5430db3-507a-418c-8a33-49ec3f9569b5"
        }         
        params = {
            '_api_name': self.api_code,
            '_api_version': '1.0.0' 
        }
        
        while True:                                
            self.index += 1
            print(f"正在获取第{self.index}页数据...")           
            params["page"] = self.index 
            response = requests.get(url = self.host,params = params, headers = headers)   
            if response.status_code == 200:
                try:         
                    res_data = response.json()
                    if res_data: 
                        data = res_data["value"]    #返回的是一个List
                        if data:                    #不为空则表示分页数据存在，否则表示已取完  
                            #return data
                            li =[{"type_id":'zfw_zz_rkxx',"card_num":row['zfw_z_1_sfzh'],"body":str(row)} for row in data] 
                            self.save_data(li)               
                        else:
                            print(f"当前第{self.index}页已经是最后一页！")
                            break
                    time.sleep(0.1)                 #爬取慢一点，防止接口崩溃
                    
                except Exception as e: 
                    print('JSON解析错误：{}'.format(e))     
            else:
                print('URL：{}，状态码：{}'.format(self.host, response.status_code))                   
    
    #保存数据
    def save_data(self,data):
        try: 
            conn = self.pool.connection()
            cursor = conn.cursor()      
            #多个字典(绑定变量)
            #params = [{"a":'100',"b":"200","c":300,"type":'test'},{"a":'1100',"b":"2200","c":3300,"type":'test'}]   
            sql = 'INSERT INTO BASE_SPT_XTDJ_TB(type_id,para1,body) values(:type_id,:card_num,:body)'
            cursor.executemany(sql,data)   
            conn.commit()
            cursor.close()
            conn.close() 
            print(f"保存第{self.index}页数据成功...")
        except Exception as e:
            print("数据库插入错误！",e)
        
    def start(self):    
        # res = self.get_token() 
        # if res:
        #     token = res["access_token"]
        #     print(f"第一步获取access_token：{token}")
        self.get_pagedata(None)
               
if __name__=='__main__':  
    start = time.time()
    
    api = ApiSpider()
    api.start()
    
    end = time.time() 
    print("获取接口数据完成！！！""总耗时：%0.2fs"%(end -start)); 
    