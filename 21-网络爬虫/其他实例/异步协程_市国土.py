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
from DBUtils.PooledDB import PooledDB

endtime = os.getenv("endtime")
if endtime is None:
    endtime = '18:30' 
    
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
app_key = 'ccd1d2a835c246788f54a177395f6ca6'
userId= "cc0689a0-d286-43f3-ba91-658f1bc1f125";
privateKey = "MIICdwIBADANBgkqhkiG9w0BAQEFAASCAmEwggJdAgEAAoGBANql8gtIgx+LJGmV024PzHJJ/qO5Fvj5aaXXC1ZVyTsxbOMylU65jc3u1ig83M8y/iCHrvbLzQ1D0GY15ywepJAkykUZxaQhA1/hnSGMwQA1IvSk7xsRfzM4CgNtPqJgfY6Q5/wRfa+90vvHnzPf6/NgKCf4RJ3UOL2i6JT6jA/PAgMBAAECgYEAo6xjkyS121AKcuuQOSyka82OS7sLQldaSaW/u+I94AywqSa9dBAc4dJvB/H/jS9r4qgPRnnrRonEIC8rnPBXWJmmMJRYt96cvCRcmWfHcv8G2yg+3Zq48ImduIhfRwgABZz+2mFJVtO7cef3mV/9CWV+rkvVGHO+dMBZM+YT/WECQQDvO2kulclJrHvcHOnVKzyMgPn5TMavicpYOo6N+gU90DNcjgjQWazPK3LuTyejiOD9pMERJLHyv45cZVtBL1xxAkEA6fkxyWXB/t06wLc+rnQzs5on+BtXMom3B5e3AdhIH8vj19iFZRMf70YjfP/+VjRclGjM9ord+Eha9pnpt5FQPwJAeTAAbV/lctPUfsGK1rirWIWxm89/ysajYSRwuI1SAGkqy5UL8/epad0ZwI0KiHY7e2Hth7CuEElnZXjWzGOgkQJBAK09KsTxSFO6YH9C7vFi7skj8kY9kDHGUDQZ/JIsHzMT128BTbvKDlIvP6WVMi+H86ibdG9z4OiuQlPnIGsf+CcCQGm7E8gzp/KCtDMsa797yapJOfCKlE3B9LKnu04li2fDAvS20ULVk+vZHHUhlCuav4cL+sJKAWQNZ5iuLh+6Xbg=";

#jvm = r'C:\Program Files\Java\jre1.8.0_181\bin\server\jvm.dll'  #jvm.dll启动成功 
jvm = getDefaultJVMPath()  # 直接获取环境变量的jvm
#jpype.startJVM(jvm, "-Djava.class.path=D:\\data\\gtapi.jar")    #jar包的位置
jpype.startJVM(jvm, "-Djava.class.path=/opt/gtapi.jar")         #jar包的位置
pdf = JClass('testrsr.PdfControllerTest')                       #java的类名

row_count = 1               #每次查询数量
dept = 'wx'                 #区县标记

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

url = 'http://59.202.115.11/gateway/api/001008005007017/dataSharing/LQ2aKKb7t6bb90cd.htm'
params = {
    "appKey": app_key
}

#数据库连接参数/连接池
user='cigwbj'
password='esri@123'
host='10.21.198.126'
port='15214'
sid='xe'
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
                    select * from (
                        select PARA1 ZJH,PARA2 NAME,PARA3 XZQBM from base_spt_para  where type_id='gtfw' AND PARA1 NOT IN(
                            SELECT PARA1 FROM BASE_SPT_XTDJ_TB WHERE TYPE_ID='gtfw'
                        ) and DATA_FROM = '{}' order by dbms_random.value()
                    ) where rownum=1
                ) TB""".format(app_key,dept)  
    cursor.execute(sql1)
    row = cursor.fetchall()                    # 得到所有数据集
    cursor.close() 
    conn.close()
    return row
 
#保存结果 
def save_data(code,msg,zjh,name,data,datacount): 
    conn = pool.connection()
    cursor = conn.cursor()  
    params = [zjh,name,code,msg,data,datacount]     
    sql = "INSERT INTO BASE_SPT_XTDJ_TB(ID,TYPE_ID,KEY,NAME,PARA1,PARA2,PARA3,PARA4,CODE,MSG,BODY,STATE,CREATE_USER,CREATE_DATE,DATA_COUNT) values(SYS_GUID(),'gtfw','gtfw','国土房屋查询',:1,:2,null,null,:3,:4,:5,'1','ADMIN',SYSDATE,:6)"
    cursor.execute(sql,params)
    conn.commit() 
    cursor.close()
    conn.close()

#判断是否工作时间
def is_worktime():
    # 范围时间
    d1_time =  datetime.datetime.strptime(str(datetime.datetime.now().date())+'8:00', '%Y-%m-%d%H:%M') 
    d2_time =  datetime.datetime.strptime(str(datetime.datetime.now().date())+endtime, '%Y-%m-%d%H:%M')   
    # 当前时间
    c_time = datetime.datetime.now()
    # 判断当前时间是否在范围时间内（8:00——18:30停止运行）
    return True if c_time >d1_time and c_time <d2_time else False
            
async def get_page(url,params,zjh,name):
    async with aiohttp.ClientSession(timeout = aiohttp.ClientTimeout(total = 15)) as session:   #10s超时  
        try:
            async with await session.get(url = url,params = params) as res: 
                if res.status == 200:
                    page_text = await res.text()   # read()  json() 
                    result = json.loads(page_text)
                    code = result["code"]
                    data = json.dumps(
                        json.loads(result['datas'])['fwxxlist'] if code == '00' else result,
                        indent=4,
                        ensure_ascii=False)
                    print('国土-接口:%s,人口:%s-%s,结果:%s'%(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'),zjh,name,data.replace('\n','').replace(' ','')[2:50]))     
                    save_data(code,result["msg"],zjh,name,data,result["dataCount"])
                else:
                    print("国土-接口:{},人口:{}-{},Error:{}".format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'),zjh,name,res))
        except Exception as e:
            print("国土-接口:{},人口:{}-{},请求超时错误{}".format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'),zjh,name,e))
                
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
        obj = json.dumps(JsonObject)
        
        try: 
            #获取加密后的值
            params["encryptEntity"] = pdf.GetEncrypResult(userId,privateKey,obj)
            params["sign"] = row[0]
            params["requestTime"] = row[1]
            params["additional"] = "{\"powerMatters\":\"许可-00757-000\",\"subPowerMatters\":\"许可-00757-001\",\"accesscardId\":\"sjgl\",\"materialName\":\"机动车驾驶证初学申领\",\"sponsorName\":\"大数据管理中心\"}"            
        except Exception:
            print("获取加密结果超时错误！")
            break        
        
        c = get_page(url,params,row[2],row[3])
        task = asyncio.ensure_future(c)
        tasks.append(task)
        
    loop.run_until_complete(asyncio.wait(tasks))

print('总耗时：', time.time()-start)
shutdownJVM()