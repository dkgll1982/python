#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-08-21 16:21:20 
# @Last Modified by: guojun 
# @Last Modified time: 2019-08-21 16:21:20 
# @Software: vscode 
 
import cx_Oracle
import os
import urllib.request 
import requests
import json
import os,sys,base64 
import datetime
from dbutils.pooled_db import PooledDB

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

#上传地址 
url = "http://hangzhou-sy-jczl.spacecig.com/zhzlbackend/common/uploadFile"
#测试发现：Accept、User-Agent这俩必不可少,不行再加host
head={
    'Host':'hangzhou-sy-jczl.spacecig.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    #'Accept-Language':'zh-CN,zh;q=0.9,und;q=0.8,en;q=0.7',
    #'Accept-Encoding':'gzip, deflate', 
    #'Connection':'keep-alive',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    "Cookie": "passport=7690cf65-fac9-4880-b707-3a56bad528d5; CIGUserid=ADMIN; ASP.NET_SessionId=npht1wwvlgkbph24vz4mkksm; CIGServiceProvider=AE167AEEB616038DF13CB13345FEE63CA4069CDFF296A518FB2B7AF0312B5469E8D5664450A46D48B11F7C6BD5659D23CABC8207258AA8AF9D579C7CC03095BBD24BEFAB1EC450485B0D67C128614603AA55F62195D0DD83CA9BEA20A09D12AB62599226; CIGToken=de6ad04e-fc75-46f4-b4db-23d1edb6b762; CIGUsername=%E7%AE%A1%E7%90%86%E5%91%98"
}

#更新附件表
def update_bid(cardnum,id1,id2):
    conn = pool.connection()
    cursor = conn.cursor()  
    
    sql = "update cigproxy.zz_attachment set file_type='per-image',B_ID=(select id from cigproxy.zz_person where card_num='"+cardnum+"' and rownum=1) where id = '" +id1+"' or id='"+id2+"'"
    cursor.execute(sql) 
    conn.commit() 
    print("{}-上传{}照片成功！".format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'),cardnum))
    cursor.close()
    conn.close()   

# 获取查询的数据列表 
def get_data(): 
    conn = pool.connection()
    cursor = conn.cursor()    
    sql1 = '''select para1 CARD_NUM,body from base_spt_xtdj_tb TA
                JOIN zz_person TB ON TA.para1=TB.CARD_NUM AND type_id='PersonalIdentityInfo' 
              where TB.ID NOT IN(
                    SELECT B_ID FROM cigproxy.zz_attachment TC WHERE file_type='per-image' AND B_ID IS NOT NULL
              ) AND LENGTH(BODY)>10 
              AND ROWNUM<10'''  
    cursor.execute(sql1)
    row = cursor.fetchall()                    # 得到所有数据集
    cursor.close() 
    conn.close()
    return row

#base64转成本地图片
def base64toimg(cardnum,data):    
    with open(r"{}.jpg".format(cardnum),'wb') as f:
        f.write(data)
        f.close()

#上传照片到服务器
def upload_img(row):
    cardnum = row[0]
    #lob字转成字符串类型，否则报“TypeError: the JSON object must be str, bytes or bytearray, not LOB”的错误
    try:
        #zp字段值可能为空，为空则进行异常捕获
        zp = base64.b64decode(json.loads(row[1].read())[0]['zP'])
        
        base64toimg(cardnum,zp)
        
        files = {'file': open(r"{}.jpg".format(cardnum),'rb')}
        r = requests.post(url, files=files,headers=head)  
        response = r.json()
        print(response)
        try:
            update_bid(cardnum,response["data"]["id"],response["data"]["thumbnail"]["id"])
        except Exception as e:
            print("{}-上传{}照片出错，{}".format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'),cardnum,e))
    except Exception as e:
        print("{}-上传{}照片出错，{}".format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'),cardnum,e))
    

if __name__ == "__main__":   
    rows = get_data()
    for row in rows:
        upload_img(row)