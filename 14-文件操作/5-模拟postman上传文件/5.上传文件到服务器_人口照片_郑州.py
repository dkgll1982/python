#!/usr/bin/env python 
# -*- coding:utf-8 -*-  
# @Author: suixin 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd  
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-12-18 11:52:18 
# @Remark: Life is short, I use python！
 
import cx_Oracle
import os
import urllib.request 
import requests
import json
import os,sys,base64 
import datetime,time
#2.0的写法是
from dbutils.pooled_db import PooledDB
#1.3的写法是
#from DBUtils.PooledDB import PooledDB
#如果报错：ModuleNotFoundError: No module named ‘DBUtils‘，可参考：https://blog.csdn.net/harry_haiwei/article/details/109510971

class PostPhoto(object):    
    def __init__(self):
        os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

        #数据库连接参数/连接池
        user='cigproxy'
        password='cigproxy'
        host='172.17.217.17'
        port='15227'
        sid='xe'
        dsn = cx_Oracle.makedsn(host,port,sid)
        self.pool = PooledDB(cx_Oracle,
                        mincached = 20,
                        blocking = True,
                        user = user,
                        password = password,
                        dsn = dsn)

        self.session = requests.Session()
        #登录地址        
        self.login_url = "http://zfw-zhzl.z.digitalcnzz.com/iam/saml/login"
        #上传地址 
        self.url = "http://zfw-zhzl.z.digitalcnzz.com/zhzlbackend/common/uploadFile"        
        self.header = {
            "Host":"zfw-zhzl.z.digitalcnzz.com", 
            "Referer":"http://zfw-zhzl.z.digitalcnzz.com/zhzl-frames/navigation-zz.html",
            "Content-Length":"31048",
            #"Content-type":"multipart/form-data; boundary=----WebKitFormBoundaryi2DoXCWBCO6ZqBne",   #去掉此项不然上传报错
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
        }
        self.param = {
            "userid":"admin", 
            "password":"DFYOPS1RrpdVlu2U"
        }  
        self.session.post(self.login_url,data = self.param)  
        # 可以按标准格式将保存的Cookie打印出来
        cookieStr = ""
        for item in self.session.cookies:
            cookieStr = cookieStr + item.name + "=" + item.value + ";"
        ## 舍去最后一位的分号 
        print(f"本次登录会话的Cookie：{cookieStr[:-1]}")
        self.header["Cookie"] = cookieStr

        
    #用户登录，保持会话
    def login(self):
        self.session.post(self.login_url,data = self.param)  
        # 可以按标准格式将保存的Cookie打印出来
        cookieStr = ""
        for item in self.session.cookies:
            cookieStr = cookieStr + item.name + "=" + item.value + ";"
        ## 舍去最后一位的分号 
        print(f"本次登录会话的Cookie：{cookieStr[:-1]}")
        self.header["Cookie"] = cookieStr

    #更新附件表
    def update_bid(self,cardnum,id1,id2):
        conn = self.pool.connection()
        cursor = conn.cursor()  
        
        sql = "update cigproxy.zz_attachment set file_type='per-image',B_ID=(select id from cigproxy.zz_person where card_num='"+cardnum+"' and rownum=1) where id = '" +id1+"' or id='"+id2+"'"
        cursor.execute(sql) 
        conn.commit() 
        print("{}-上传{}照片成功！".format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'),cardnum))
        cursor.close()
        conn.close()   

    # 获取查询的数据列表 
    def get_data(self): 
        conn = self.pool.connection()
        cursor = conn.cursor()    
        sql1 = '''select para1 CARD_NUM,body from base_spt_xtdj_tb TA
                  where key='zfw_zz_rkxx_1' AND NOT EXISTS(
                    SELECT * FROM cigproxy.zz_attachment TB WHERE file_type='per-image' AND Tb.B_ID=TA.COLUMN1 
                  ) 
                  AND ROWNUM<=100'''  
        cursor.execute(sql1)
        row = cursor.fetchall()                    # 得到所有数据集
        cursor.close() 
        conn.close()
        return row
    

    def createFile(self,filePath):
        if os.path.exists(filePath):
            #print('%s:存在'%filePath)
            pass
        else:
            try:
                os.mkdir(filePath)
                print('新建文件夹：%s'%filePath)
            except Exception as e:
                os.makedirs(filePath)
                print('新建多层文件夹：%s' % filePath)

    #base64转成本地图片
    def base64toimg(self,cardnum,data):
        dt = datetime.datetime.now().strftime('%Y%m%d%H')    
        path = f"backup\\img\\{dt}"
        self.createFile(path)
        file_name = f"{path}\\{cardnum}.jpg"
        with open(file_name,'wb') as f:
            f.write(data)
            f.close()
        return file_name
    
    #上传照片到服务器
    def upload_img(self,row):
        cardnum = row[0]
        #lob字转成字符串类型，否则报“TypeError: the JSON object must be str, bytes or bytearray, not LOB”的错误
        try:
            #zp字段值可能为空，为空则进行异常捕获
            zp = base64.b64decode(eval(row[1].read())['sgats_2_zp'])
            
            file_name = self.base64toimg(cardnum,zp)
            
            files = {'file': open(file_name,'rb')}
            r = requests.post(self.url, files = files,headers = self.header)  
            if r.status_code == 200:
                response = r.json()
                if True if "errMsg" not in response else True if response["errMsg"] == 'null' else False:     #为空表示上传成功
                    print(f'{cardnum}照片上传信息：{response}')
                    try:
                        self.update_bid(cardnum,response["data"]["id"],response["data"]["thumbnail"]["id"])
                    except Exception as e:
                        print("{}-上传{}照片出错，{}".format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'),cardnum,e))            
                else:    #重登录   
                    self.login()
                    self.upload_img(row)        
            else:
                print('URL：{}，状态码：{}'.format(self.url, r.status_code))                   
        except Exception as e:
            print("{}-上传{}照片出错，{}".format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'),cardnum,e))
        
    def start(self):
        while True:
            rows = self.get_data()
            if len(rows) ==0:           #数据上传完毕，退出循环
                break
            else:
                for row in rows:
                    self.upload_img(row)
            time.sleep(0.1)
                    
if __name__ == "__main__":   
    start = time.time()
        
    pt = PostPhoto()
    pt.start()

    end = time.time() 
    print("上传照片数据完成！！！""总耗时：%0.2fs"%(end -start)); 
    