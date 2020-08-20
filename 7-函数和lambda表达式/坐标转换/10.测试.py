#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-08-14 15:38:25 
# @Last Modified by: guojun 
# @Last Modified time: 2019-08-14 15:38:25 
# @Software: vscode  
# 2020-8-20：计算江都企业/场所网格

import cx_Oracle
import os
import urllib.request 
from 坐标转换 import bd09_to_wgs84,bdapi 
import threading,time
import urllib.request
import json
import datetime 
import sys

#百度ak,sk
ak = "ZRyBcN55hT7nYsWUta0hfyTkn3NeBNNG"
sk = "NGKBzEx1Qv66aq8xjvE2V6AXgr5oyinZ"
#坐标计算网格服务
geoserver = 'https://jd.spacecig.com/CIGService/rest/services/0/intersectFeaturesByXY';

#地址前缀
city = ''

#线程数量
threadcount = 1
#数据分段区间
pagecount = 1000
#每次取数据行数
rowcount = 10001
#线程循环次数
xhcount = 1

# 大致计算公式如下
# 公式1：线程循环次数 = 数据分段区间/每次取数据行数，如5000/100=50，即需要约50次循环才能跑完区间的所有的数据 
# 公式2：最终处理数据量 = 线程数量*数据分段区间，如20*5000=100000
# 由公式1也可得公式3：最终处理数据量 = 线程数量*每次取数据行数*线程循环次数，如20*100*50=100000

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
    
#获取查询的数据列表
def get_zb(index,biao):
    os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
    conn = cx_Oracle.connect('cigproxy','cigproxy','127.0.0.1:1521/orcl')
    cursor = conn.cursor() 

    #取数据起始位置
    start = str(pagecount*(index-1))
    #取数据结束位置
    end = str(pagecount*(index))
    #查询数据的sql
    sql1 =  "SELECT 序号,replace('江苏省'||企业名称,'101#') dr FROM BASE_CS where result IS NULL and 企业名称 is not  null"

    cursor.execute(sql1);    
    rows = cursor.fetchall()  # 得到所有数据集

    update_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    g = bdapi(ak,sk)
    row_index = 0
    for row in rows: 
        url =g.get_url(row[1])
        try:
            bd_zb = g.get_zb(url)                                                               #得到百度坐标
            if bd_zb is not None:
                wgs_zb =  bd09_to_wgs84(bd_zb[0], bd_zb[1])                                     #将百度坐标转为WGS84坐标                
                bd_x,bd_y,wgs_x,wgs_y = str(bd_zb[0]),str(bd_zb[1]),str(wgs_zb[0]),str(wgs_zb[1])
                geo = geoserver+"?x="+wgs_x+"&y="+wgs_y
                result = request_data(geo) 
                print("子线程(%s)处理；百度：%s；WGS84：%s；获取网格地址：%s"%(threading.current_thread().name,bd_zb,wgs_zb,geo)) 
                sql2 = "update BASE_CS set RESULT='%s' where 序号=%s"%(str(result),row[0]) 
            #else:       
            #    sql2 = "update "+ biao+" set update_date=to_date('%s','YYYY-MM-DD HH24:MI:SS') where GRID_ADDR='%s'"%(update_date,row[0])            
            cursor.execute(sql2)
        except Exception as e:
            print('Error:',e)
        finally:
            row_index = row_index + 1
            if row_index%100 == 0:
                conn.commit()
                
    conn.commit() 
    cursor.close()
    conn.close()    

if __name__ == "__main__":  
    args = sys.argv 
    biao = "BASE_CS"
    print(biao)
    print("主线程(%s)启动"%(threading.current_thread().name))
    start = time.time() 

    for x in range(xhcount):
        #任何进程默认就会启动一个线程，成为主线程，主线程就可以启动新的子线程
        #current_thread(): 返回当前线程的实例 
        ThreadList = []

        #创建子线程
        for x in range(threadcount):
            ThreadList.append(threading.Thread(target=get_zb,name="Thread"+str(x),args=(x,biao)))
        #启动子线程
        for thread in ThreadList:
            thread.setDaemon(True)#守护线程  
            thread.start() 
        #等待线程结束
        for thread in ThreadList:
            thread.join()  

        time.sleep(2)
        
    end = time.time()
    print("主线程(%s)结束,总耗时：%0.6f秒"%(threading.current_thread().name,end-start)) 