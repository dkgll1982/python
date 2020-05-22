#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-05-19 17:31:23 
# @Remark: 人生苦短，我用python！

from urllib import request
import http.cookiejar as cookielib
import urllib
import json
import urllib.parse
import os,cx_Oracle,sys
import threading,time,datetime
import hashlib
import xlrd,xlsxwriter 
import math

class JKMSpider():
    def __init__(self):
        os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
        self.dbuser = 'cigwbj'
        self.dbpwd = 'esri@123'
        self.dbserver = '10.21.198.126:15214/xe'
        self.datatype = 'jkm_ldrk'
        self.city = '杭州市'
        self.mzt = '绿码'
        
        self.pagecount = 10        #每次取数据行数
        self.totalcount = 49000      #总行数
                
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
    
    #查询人口数据，调用接口 
    def get_data(self): 
        conn = cx_Oracle.connect(self.dbuser, self.dbpwd, self.dbserver,encoding="UTF-8") 
        cursor = conn.cursor()  
        
        #查询人口数据
        sql1 = """select SFZH,xm from gat_hj_biz_024 
                      where SFZH not in (
                      select A from excel_table where TYPE='{}' 
                  ) and LENGTH(SFZH)=18 and ROWNUM<{}""".format(self.datatype,str(self.pagecount)) 
        sql2 = "" 
        
        cursor.execute(sql1)  
        rows = cursor.fetchall()  # 得到所有数据集
        rowindex = 0
        for row in rows:  
            rowindex = rowindex + 1  
            data = {"sfzh":row[0],"mzt":self.mzt,"mffd":self.city}
            jsonstr = self.send_request(data)
            print('获取第%d条身份证：%s健康码（%s）成功!'%(rowindex,row[0],row[1]),jsonstr)
            sql2 = "INSERT INTO excel_table(TYPE,A,B,C,D) VALUES(:1,:2,:3,:4,:5)"
            params = (self.datatype,row[0],jsonstr,datetime.datetime.now().strftime('%Y-%m-%d %H'),row[1])
            cursor.execute(sql2,params)
          
        conn.commit() 
        cursor.close()
        conn.close()  
        
if __name__ == '__main__': 
    print("主线程(%s)启动"%(threading.current_thread().name))
    start = time.time()  
            
    jkm = JKMSpider()  
    pagesize = math.ceil(jkm.totalcount/jkm.pagecount)+1
    for x in range(1,pagesize): 
        jkm.get_data()
        print('第%d遍查询完毕！'%(x+1))
                
    end = time.time()
    print("主线程(%s)结束,总耗时：%0.6f秒"%(threading.current_thread().name,end-start)) 