#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-03-27 15:19:36 
# @Remark: 人生苦短，我用python！

import cx_Oracle
import os
import urllib.request 
from 坐标转换 import bd09_to_wgs84,bdapi 
import threading,time

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

class ZuoBiaoZhuanHuan():
    def __init__(self,city):
        super().__init__()
        self.city = city
        # 数据库连接配置
        self.dbconfig = {
            "西咸新区":('cigproxy','cigproxy','136.2.34.65:15226/xe'),
            "沣西新城":('cigproxy','cigproxy','136.2.34.65:15299/xe'),
            "沣东新城":('cigproxy','cigproxy','136.2.34.65:15227/xe'),
            "秦汉新城":('cigproxy','cigproxy','136.2.34.65:15233/xe'),
            "空港新城":('cigproxy','cigproxy','136.2.34.65:15231/xe'),
            "泾河新城":('cigproxy','cigproxy','136.2.34.65:15229/xe')
        }
        self.conn = cx_Oracle.connect(*self.dbconfig[city])
        self.cursor = self.conn.cursor() 
        self.tb_name = 'zz_place_common'         #表名
        self.addr_col = 'PLACE_ADDR'        #地址列名
        self.location_col = 'remark'          #坐标列名
        #百度ak,sk
        self.ak = "LKnE67ysMkrG0LHwyG2GHPlc00LtMfSW"
        self.sk = "3hPe7iy3Ydq003v6wYbKn6pq7sHgGCRj"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36"
        } 

    # 发送请求
    def send_request(self, url):
        try:
            response = requests.get(url=url, headers=self.headers)
            if response.status_code == 200:
                return response
        except Exception as e:
            print('URL:{},错误信息:{}'.format(url, e))
    
    # 获取数据
    def get_data(self):
        sql = "SELECT id,{} addr FROM {} WHERE {} IS NULL and {} is not null".format(self.addr_col,self.tb_name,self.location_col,self.addr_col)
        self.cursor.execute(sql)  
        return self.cursor.fetchall()  
    
    # 更新数据
    def update_data(self,id,location):
        sql = "UPDATE {} SET {} = '{}' WHERE ID ='{}'".format(self.tb_name,self.location_col,location,id)
        self.cursor.execute(sql)
    
    # 解析请求，更新数据
    def parase_content(self):
        rows = self.get_data()
        bd = bdapi(self.ak,self.sk)
        for index,row in enumerate(rows): 
            url = bd.get_url(self.city + row[1])                    #获取调用地图API的地址 
            try:
                bd_zb = bd.get_zb(url)                              #得到百度坐标 
                if bd_zb is not None:
                    wgs_zb = bd09_to_wgs84(bd_zb[0], bd_zb[1])      #将百度坐标转为WGS84坐标                
                    location = '{},{}'.format(str(wgs_zb[0]),str(wgs_zb[1]))
                    self.update_data(row[0],location)  
                    print('更新{}-地址：{}——坐标：{}'.format(self.city,row[1],location)) 
            except Exception as e:
                print('Error:',e) 
            if index%100 == 0:                                      #每100条提交一次                               
                self.conn.commit()
        print('更新{}全部地址坐标完成！'.format(self.city)) 
        self.conn.commit()                                          #执行完成统一提交一次

    def start(self):
        self.parase_content() 

if __name__ == "__main__":  
    print("主线程(%s)启动"%(threading.current_thread().name))
    start = time.time()
    
    city_list = ['沣西新城','沣东新城','秦汉新城','泾河新城','空港新城']
    for city in city_list:
        zbzh = ZuoBiaoZhuanHuan(city) 
        zbzh.start()
        
    end = time.time()
    print("主线程(%s)结束,总耗时：%0.6f秒"%(threading.current_thread().name,end-start)) 