#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-08-14 15:38:25 
# @Last Modified by: guojun 
# @Last Modified time: 2019-08-14 15:38:25 
# @Software: vscode  

import cx_Oracle
import os
import urllib.request  
import threading,time
import urllib.request
import json
import datetime 
import sys
from 坐标转换 import bd09_to_wgs84,bdapi 
  
#调用api返回json数据
def request_data(urt):
    #测试发现：Accept、User-Agent这俩必不可少
    head={
        #'Host':'jczl.giscloud.cx',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
        #'Accept-Language':'zh-CN,zh;q=0.9,und;q=0.8,en;q=0.7',
        #'Accept-Encoding':'gzip, deflate', 
        #'Connection':'keep-alive',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Cookie':"passport=4e38dcf2-4665-49db-a8e8-f3ee5bee23b3; CIGToken=27277f9d-1d7a-4037-8791-37c87add8269; CIGUsername=%E5%90%B4%E5%85%B4%E7%AE%A1%E7%90%86%E5%91%98; CIGUserid=WX-ADMIN"
    }      
    request = urllib.request.Request(url=urt,headers=head) 
    response = urllib.request.urlopen(request)
    s = response.read().decode('utf-8')  #一定要解码！！！！ 
    #jsonData = json.loads(s)
    return s 

if __name__ == "__main__":  
    #坐标计算网格服务
    geoserver = 'http://huzhou-jczl.spacecig.com/CIGService/rest/services/0/intersectFeaturesByXY';
    #地址前缀
    city = ''
    #百度ak,sk
    ak = "LKnE67ysMkrG0LHwyG2GHPlc00LtMfSW"
    sk = "3hPe7iy3Ydq003v6wYbKn6pq7sHgGCRj"
    g = bdapi(ak,sk);
    url = g.get_url(city+"浙江省湖州市吴兴区东湖街3号附近")
    print(url)
    bd_zb = g.get_zb(url)
    wgs_zb =  bd09_to_wgs84(bd_zb[0], bd_zb[1])
    print("百度：%s,WGS84：%s"%(bd_zb,wgs_zb))    
    
    geo = f"{geoserver}?x={str(wgs_zb[0])}&y={str(wgs_zb[1])}";  
    result = request_data(geo) 
    dict = json.loads(result)
    print("获取网格地址：%s"%(dict))