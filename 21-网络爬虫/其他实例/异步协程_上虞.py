#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-06-13 10:45:55 
# @Remark: 人生苦短，我用python！

import aiohttp
import asyncio
import time
import datetime
import cx_Oracle
import socket
import os
import sys  
import json
from DBUtils.PooledDB import PooledDB

endtime = os.getenv("endtime")
if endtime is None:
    endtime = '18:30' 
    
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

#数据库连接参数/连接池
user='cigproxy'
password='cigproxy'
host='10.23.179.64'
port='15223'
sid='orcl'
dsn = cx_Oracle.makedsn(host,port,sid)
pool = PooledDB(cx_Oracle,
                mincached = 20,
                blocking = True,
                user = user,
                password = password,
                dsn = dsn)

# 获取查询的数据列表 
def get_data(): 
    conn = pool.connection()
    cursor = conn.cursor()    
    sql1 = "select * from view_set_cardphoto"  
    cursor.execute(sql1)
    row = cursor.fetchall()                    # 得到所有数据集
    cursor.close() 
    conn.close()
    return row
 
#保存结果 
def save_data(key,cardnum,code,msg,dataCount,data): 
    conn = pool.connection()
    cursor = conn.cursor()  
    params = [key,key,cardnum,code,msg,dataCount,data]     
    sql = "INSERT INTO base_spt_xtdj_tb(ID,TYPE_ID,KEY,PARA1,CODE,MSG,DATA_COUNT,BODY,STATE,CREATE_USER,CREATE_DATE) values(SYS_GUID(),:1,:2,:3,:4,:5,:6,:7,'1','ADMIN',SYSDATE)"
    cursor.execute(sql,params)
    conn.commit() 
    cursor.close()
    conn.close()

#判断是否工作时间
def is_worktime():
    # 范围时间(晚上9点终止运行)
    d1_time =  datetime.datetime.strptime(str(datetime.datetime.now().date())+'8:30', '%Y-%m-%d%H:%M') 
    d2_time =  datetime.datetime.strptime(str(datetime.datetime.now().date())+'18:48', '%Y-%m-%d%H:%M')   
    # 当前时间
    c_time = datetime.datetime.now()
    # 判断当前时间是否在范围时间内
    return True if c_time <d1_time and c_time >d2_time else False
            
async def get_page(data):
    async with aiohttp.ClientSession(timeout = aiohttp.ClientTimeout(total = 20)) as session:   #10s超时  
        try: 
            async with await session.get(url=data[2]) as res: 
                if res.status == 200:
                    page_text = await res.text()   # read()  json()                     
                    result = json.loads(page_text)
                    code = result["code"] 
                    ret = json.dumps(result['datas']  if code == '00' else result,
                        indent=4,
                        ensure_ascii=False)            
                    print('%s-接口:%s,结果:%s'%(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'),data[1],page_text[2:100]))                      
                    save_data(data[0],data[1],code,result['msg'],result["dataCount"],ret)
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
