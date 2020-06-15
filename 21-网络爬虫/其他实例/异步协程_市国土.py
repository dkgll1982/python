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
from jpype import *
import jpype 
import json

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
app_key = 'ccd1d2a835c246788f54a177395f6ca6'
row_count = 500

JsonObject = {
    "isAllCity":"0",
    "cdbh":"" ,
    "name":"",
    "zjh":"",
    "xzqbm":"",
    "isShowXzxx":"1",
    "sm":"查询范围:{0}.",
    "cxfw":"湖州市区",
    "cdyt":"无房证明",
    "jgmc":"政法委",
    "bjsy":"湖州不动产权属查询",
    "cxbt":"湖州市不动产登记信息查询记录",
    "qyca":"0"
}

# 获取查询的数据列表 
def get_data(): 
    conn = cx_Oracle.connect('cigwbj', 'esri@123', '10.21.198.126:15214/xe')
    cursor = conn.cursor() 
    sql1 = """  SELECT TA.*,TB.*,'zfw'||to_char(sysdate,'yyyymmdd')||'-'||lpad(CIG_API_SEQ.NEXTVAL,7,'0') cdbh FROM (
                    SELECT lower(utl_raw.cast_to_raw(DBMS_OBFUSCATION_TOOLKIT.MD5(INPUT_STRING => TB.KEY||TD.SERC||td.CREATE_DATE))) sign,
                        td.CREATE_DATE requestTime
                    FROM BASE_SPT_INTERFACE TA
                    JOIN BASE_SPT_SERC TB ON ','||TB.INTERFACE||',' LIKE '%,'||TA.KEY||',%' 
                    JOIN BASE_SPT_QLSX TC ON ','||tC.deptID2||',' like '%,'||tb.deptid||',%' and tC.zxmc is not null and tC.zxbm is not null 
                    JOIN (
                        select to_char((SYSDATE - TO_DATE('1970-1-1 8', 'YYYY-MM-DD HH24')) * 86400000 + TO_NUMBER(TO_CHAR(SYSTIMESTAMP(3), 'FF'))) create_date,SERC,app_key from (
                            select create_date,row_number() over(partition by app_key order by create_date desc nulls last) rn,requestsecret SERC,app_key from base_spt_keysecret 
                        ) 
                        where rn=1 and APP_KEY='{}'
                    ) TD ON TD.APP_KEY=TB.KEY
                ) TA,(
                    select PARA1 ZJH,PARA2 NAME from base_spt_para  where type_id='gtfw' AND PARA1 NOT IN(
                        SELECT PARA1 FROM BASE_SPT_XTDJ_TB WHERE TYPE_ID='gtfw'
                    )
                ) TB
                WHERE ROWNUM<{}""".format(app_key,row_count)
    cursor.execute(sql1)
    return cursor.fetchone()                    # 得到所有数据集
 
#判断是否工作时间
def is_worktime():
    # 范围时间(晚上9点终止运行)
    d1_time =  datetime.datetime.strptime(str(datetime.datetime.now().date())+'6:20', '%Y-%m-%d%H:%M') 
    d2_time =  datetime.datetime.strptime(str(datetime.datetime.now().date())+'6:50', '%Y-%m-%d%H:%M')   
    # 当前时间
    c_time = datetime.datetime.now()
    # 判断当前时间是否在范围时间内
    return True if c_time >d1_time and c_time <d2_time else False
            
async def get_page(name,url):
    async with aiohttp.ClientSession(timeout = aiohttp.ClientTimeout(total = 10)) as session:   #10s超时  
        try:
            async with await session.get(url=url) as res: 
                if res.status == 200:
                    page_text = await res.text()   # read()  json() 
                    print('%s-接口:%s,结果:%s'%(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'),name,page_text[2:23]))    
                else:
                    print("{}-Error: {}".format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'),res))
        except Exception as e:
            print("{}-请求超时错误{}".format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'),e))
                
start = time.time()

while True:
    if is_worktime():
        print('非工作时间，停止运行！')
        break
    
    tasks = []
    loop = asyncio.get_event_loop()
    rows = get_data()
    for row in rows: 
        JsonObject["zjh"] = row[2]
        JsonObject["name"] = row[3]
        JsonObject["xzqbm"] = row[4]
        JsonObject["cdbh"] = row[5]
        c = get_page(row[0],row[1])
        task = asyncio.ensure_future(c)
        tasks.append(task)
    loop.run_until_complete(asyncio.wait(tasks))

print('总耗时：', time.time()-start)
