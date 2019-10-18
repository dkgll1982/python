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
import json 
import datetime 
import sys,os  
 
from db  import *

#测试连接
def getconn(db):
    os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
    try:
        conn = cx_Oracle.connect(db.userid,db.pwd,db.ip+':'+db.port+'/'+db.sid)
        return True
    except:
        return False

#获取查询的数据列表
def get_data(db,sqltext):
    os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
    conn = cx_Oracle.connect(db.userid,db.pwd,db.ip+':'+db.port+'/'+db.sid)
    cursor = conn.cursor() 
 
    #执行查询的语句，返回游标结果集
    cursor.execute(sqltext);    
    data = cursor.fetchall()  # 得到所有数据集

    #获取表的列名
    title = [i[0] for i in cursor.description] 
    data.insert(0,title) 

    conn.commit() 
    cursor.close()
    conn.close()   
    return data