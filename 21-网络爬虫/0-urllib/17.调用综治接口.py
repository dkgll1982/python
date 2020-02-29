#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-02-21 19:20:37 
# @Last Modified by: guojun 
# @Last Modified time: 2020-02-21 19:20:37 
# @Software: vscode 
from urllib import request
import http.cookiejar as cookielib
import urllib
import json
import urllib.parse
import os,cx_Oracle
import threading,time,datetime
 
#每次取数据行数
rowcount = 50
#循环次数
xhcount = 15

class ZongZhiSpider():
    def __init__(self):
        host = 'http://jczl.giscloud.cx/'
        login_url = host + "iam/saml/login"
        self.inter_url = host + "healthWeb/front/index/healthQuery"
        userpwd = {"userid":"admin", "password":"DFYOPS1RrpdVlu2U"}  
        
        # 通过CookieJar()类构建一个cookieJar()对象，用来保存cookie的值
        cookie = cookielib.CookieJar()
        # 通过HTTPCookieProcessor()处理器类构建一个处理器对象，用来处理cookie
        # 参数就是构建的CookieJar()对象
        cookie_handler = request.HTTPCookieProcessor(cookie)
        opener = request.build_opener(cookie_handler)

        # 自定义opener的addheadders的参数，可以赋值HTTP报头参数
        opener.addheaders = [("Content-type","application/json;charset=UTF-8"),("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36")]
  
        # 通过urlencode()转码
        postdata = urllib.parse.urlencode(userpwd).encode('utf8')

        # 构建Request请求对象，包含需要发送的用户名和密码
        req = request.Request(login_url, data = postdata)

        # 通过opener发送这个请求，并获取登录后的Cookie值，
        response = opener.open(req)  

        # 可以按标准格式将保存的Cookie打印出来
        cookieStr = ""
        for item in cookie:
            cookieStr = cookieStr + item.name + "=" + item.value + ";"

        # 舍去最后一位的分号(此处取到cookie值)
        self.cookieStr = cookieStr[:-1]   
        
    def send_request(self,data):  
        headers = {
            "Host":'jczl.giscloud.cx',
            "Content-type":"application/json;charset=UTF-8",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36",
            "Cookie":self.cookieStr
        } 
 
        form_data = bytes(json.dumps(data), 'utf8')
 
        req = request.Request(self.inter_url,headers = headers, method='POST')
        response = urllib.request.urlopen(req,data = form_data)

        return response.read().decode('utf-8') 
        
    def write_content(self,content):
        pass 
    
    def start(self):
        os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
        conn = cx_Oracle.connect('cigproxy','cigproxy','172.21.188.219:15223/orcl')
        cursor = conn.cursor()  
        
        sql1 = """ SELECT * FROM (
            SELECT * FROM (  
               select DISTINCT 身份证号 sfzh, '绿码' mzt,'湖州市' mffd,1 SORT_TYPE from BASE_jkm0302 WHERE 身份证号 NOT IN
                (
                select A from excel_table WHERE TYPE='jkm2' AND d='绿码'
                ) and length(身份证号)=18  
                UNION ALL
               select DISTINCT 身份证号 sfzh,'红码' mzt,'湖州市' mffd,2 from BASE_jkm0302 WHERE 身份证号 IN
                (
                select A from excel_table WHERE TYPE='jkm2' AND d='绿码' AND TO_SINGLE_BYTE(JSON_VALUE(b,'$.msg'))='查询失败' 
                ) 
                AND 身份证号 NOT IN
                (
                    select A from excel_table WHERE TYPE='jkm2' AND d='红码'
                ) and length(身份证号)=18  
                UNION ALL
               select DISTINCT 身份证号 sfzh,'黄码' mzt,'湖州市' mffd,3 from BASE_jkm0302 WHERE 身份证号 IN
                (
                select A from excel_table WHERE TYPE='jkm2' AND d='红码' AND TO_SINGLE_BYTE(JSON_VALUE(b,'$.msg'))='查询失败' 
                ) 
                AND 身份证号 NOT IN
                (
                    select A from excel_table WHERE TYPE='jkm2' AND d='黄码'
                ) and length(身份证号)=18  
            ) ORDER BY SORT_TYPE 
        ) WHERE ROWNUM<""" + str(rowcount)
        sql2 = ""

        cursor.execute(sql1)  
        rows = cursor.fetchall()  # 得到所有数据集
        for row in rows:  
            data = {"sfzh":row[0],"mzt":row[1],"mffd":row[2]}
            jsonstr = self.send_request(data)
            print('获取%s健康码（%s）成功!'%(row[0],row[1]))
            sql2 = "INSERT INTO excel_table(TYPE,A,B,C,D) VALUES('jkm2','%s','%s','%s','%s')"%(row[0],jsonstr,datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),row[1])
            cursor.execute(sql2)
          
        conn.commit() 
        cursor.close()
        conn.close()   
    
if __name__ == '__main__':
    zzs = ZongZhiSpider()  
    
    print("主线程(%s)启动"%(threading.current_thread().name))
    start = time.time() 
    
    for x in range(xhcount):
        zzs.start() 
        print("循环调用第%d次调用完毕！"%(x+1))
        time.sleep(0.1)
        
    end = time.time()
    print("主线程(%s)结束,总耗时：%0.6f秒"%(threading.current_thread().name,end-start)) 