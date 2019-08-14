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


#获取事件百度坐标并更新
def update_zb(index):
    os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
    conn = cx_Oracle.connect('cigwbj','esri@123','10.21.198.126:15214/xe')
    cursor = conn.cursor() 
    sql =  ("select * from zz_event_zuobiao where id not in(select id from zz_event_zuobiao2) and rownum<=1000") 
    
    cursor.execute(sql);
    
    rows = cursor.fetchall()  # 得到所有数据集
    param = [] 
    for row in rows:
        lng,lat = row[1].split(',');   
        sql2 = "insert into zz_event_zuobiao2(ID,WGS84) values('"+row[0]+"','"+str(bd09_to_wgs84(float(lng), float(lat)))+"')"  
        #print(sql2);
        cursor.execute(sql2)
        # rown = cursorObj.execute(None, {'ID':row[0],'WGS84':bd09_to_wgs84(float(lng), float(lat))})

        #bd09_to_wgs84(lng, lat)
        #li.append({"name":row[0],"card_num":row[1],"gender":row[2],"age":row[3],"addr":row[4],"URL":row[7],"FILENAME":row[8]});
     #   print("%s, %s, %s, %s, %s, %s, %s" % (row[0], row[1], row[2], row[3], row[4], row[7], row[8]))
    print("当前添加%d条！"%((index+1)*10))
    conn.commit() 
    cursor.close()
    conn.close() 

if __name__ == "__main__":
    for x in range(78):
        update_zb(x) 