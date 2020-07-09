#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-07-08 09:17:45 
# @Remark: 人生苦短，我用python！

import aiohttp
import asyncio
import time
import datetime
import cx_Oracle
import socket
import os
import sys

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

# 获取查询的数据列表 
def get_data(): 
    conn = cx_Oracle.connect('cigwbj', 'esri@123', '10.21.198.126:15214/xe')
    cursor = conn.cursor() 
    sql1 = "select * from(select * from VIEW_BASE_GWY order by decode(mzt,'绿码','1','黄码','2','3'),dbms_random.value) where rownum<=10"
    cursor.execute(sql1)
    rows =  cursor.fetchall()                 
    cursor.close() 
    conn.close() 
    return rows

# 将查询的数据存到单独的表里
def save_data(row): 
    conn = cx_Oracle.connect('cigwbj', 'esri@123', '10.21.198.126:15214/xe')
    cursor = conn.cursor()      
    sql = 'INSERT INTO BASE_GWY_RESULT(CARD_NUM,MZT,MFFD,RESULT) values(:1,:2,:3,:4)'
    cursor.execute(sql,row)  
    conn.commit()         
    cursor.close() 
    conn.close() 
 
#判断是否工作时间
def is_worktime():
    # 范围时间(晚上9点终止运行)
    d1_time =  datetime.datetime.strptime(str(datetime.datetime.now().date())+'6:20', '%Y-%m-%d%H:%M') 
    d2_time =  datetime.datetime.strptime(str(datetime.datetime.now().date())+'6:50', '%Y-%m-%d%H:%M')   
    # 当前时间
    c_time = datetime.datetime.now()
    # 判断当前时间是否在范围时间内
    return True if c_time >d1_time and c_time <d2_time else False
            
async def get_page(data):
    async with aiohttp.ClientSession(timeout = aiohttp.ClientTimeout(total = 20)) as session:   #10s超时  
        try:
            async with await session.get(url=data[1]) as res: 
                if res.status == 200:
                    page_text = await res.text()   # read()  json() 
                    print('%s-接口:%s,结果:%s'%(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'),data[0],page_text[2:100]))                      
                    save_data((data[3],data[4],data[5],page_text))  
                else:
                    print("{}-Error: {}".format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'),res))
        except Exception as e:
            print("{}-请求超时错误{}".format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'),e))
                
start = time.time()

while True:
    if is_worktime():
        print('非工作时间，停止运行！')
        break    
    rows = get_data()
    if len(rows) > 0:
        tasks = []
        loop = asyncio.get_event_loop()
        for row in rows: 
            c = get_page(row)
            task = asyncio.ensure_future(c)
            tasks.append(task)
        loop.run_until_complete(asyncio.wait(tasks))
    else:
        print('所有数据已全部查询完毕，终止运行！')
        break

print('总耗时：', time.time()-start)
