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
from 坐标转换 import bd09_to_wgs84 
import threading,time

#获取事件百度坐标并更新
def update_zb(index):
    start = str(500*(index-1))
    end = str(500*(index))

    os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
    conn = cx_Oracle.connect('cigwbj','esri@123','10.21.198.126:15214/xe')
    cursor = conn.cursor() 
    sql =  ("select * from zz_event_zuobiao where wgs84 is null and rn<="+end+" and rn>"+start)  
    #print(sql)
    cursor.execute(sql);
    
    rows = cursor.fetchall()  # 得到所有数据集
    param = [] 
    for row in rows:
        lng,lat = row[1].split(',');   
        #sql2 = "insert into zz_event_zuobiao2(ID,WGS84) values('"+row[0]+"','"+str(bd09_to_wgs84(float(lng), float(lat)))+"')"  
        sql2 = "update zz_event_zuobiao set wgs84 ='"+str(bd09_to_wgs84(float(lng), float(lat)))+"' where id='" +row[0]+"'"  
        #print(sql2);
        cursor.execute(sql2)
        # rown = cursorObj.execute(None, {'ID':row[0],'WGS84':bd09_to_wgs84(float(lng), float(lat))})

        #bd09_to_wgs84(lng, lat)
        #li.append({"name":row[0],"card_num":row[1],"gender":row[2],"age":row[3],"addr":row[4],"URL":row[7],"FILENAME":row[8]}); 
    conn.commit() 
    cursor.close()
    conn.close()  
    print("第%s条-第%s条更新完成..."%(start,end));

if __name__ == "__main__": 
    #任何进程默认就会启动一个线程，成为主线程，主线程就可以启动新的子线程
    #current_thread(): 返回当前线程的实例
    print("主线程(%s)启动"%(threading.current_thread().name))
    start = time.time()

    ThreadList = []

    #创建子线程
    for x in range(1,200):
        ThreadList.append(threading.Thread(target=update_zb,name="rootThread"+str(x),args=(x,)))
    #启动子线程
    for thread in ThreadList:
        thread.start() 
    #等待线程结束
    for thread in ThreadList:
        thread.join()  
    
    end = time.time()
    print("主线程(%s)结束,总耗时：%0.6f秒"%(threading.current_thread().name,end-start)) 