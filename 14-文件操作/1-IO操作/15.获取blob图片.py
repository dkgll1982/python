#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-04-27 15:06:54 
# @Remark: 人生苦短，我用python！

import cx_Oracle
import time
import datetime
from concurrent.futures import ThreadPoolExecutor
import os
import sys
from threading import Thread,currentThread
import hashlib 

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

class BlobSpider():
    def __init__(self):
        super().__init__()
        self.base_dir = r'C:\Data\证照库\ODPS'
        self.thread_count = 15            #线程数量
        self.rowcount = 1000              #每次取数据行数 
        self.db_server = "cigproxy/cigproxy@172.21.246.244:15211/xe"
    
    # 获取照片数据列表
    def get_data(self,pageindex,threadname):  
        conn = cx_Oracle.connect(self.db_server)
        cursor = conn.cursor()
        start_index = pageindex * self.rowcount
        end_index =  (pageindex+1) * self.rowcount
        print('线程{}正在下载第{}页：{}-{}条数据...'.format(threadname,pageindex+1,start_index,end_index))
        
        sql = '''SELECT XH,photo_id,photo,SUBSTR(PHOTO_ID,17) WZ FROM test.DWS_PERSON_PHOTO_MPSB_M ta
                    WHERE XH>{} and XH<={} AND NOT EXISTS(
                        SELECT * FROM test.BASE_PHOTO TB WHERE TB.XH=TA.XH and tb.state='1'
                )'''.format(start_index,end_index)  
        cursor.execute(sql)  
        data = cursor.fetchall()  
        self.parse_data(data,conn,cursor)  
        conn.commit() 
        cursor.close()
        conn.close()    
        
    #将blob字段转化为图片并保存到相应目录
    def parse_data(self,data,conn,cursor):        
        for row in data: 
            photo = row[2]
            if photo == '':
                continue 
            # 目录不存在则创建一个目录:
            dir = os.path.join(self.base_dir,row[3])  
            if not os.path.exists(dir): 
                os.mkdir(dir) 

            content = photo.read()
            
            #计算md5值
            m = hashlib.md5() 
            m.update(content) 
            md5 = m.hexdigest()
            
            self.write_content(os.path.join(dir,row[1]+'.png'),content)  
            self.update_state((row[0],datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),"1",md5),conn,cursor)
            print('下载照片{}-{}-md5值:{}成功！'.format(row[0],row[1]+'.png',md5))
    
    #写入文件
    def write_content(self,path,content): 
        with open(path,"wb") as f:
            f.write(content)  
    
    #更新数据状态
    def update_state(self,params,conn,cursor):    
        sql = 'insert into test.base_photo(xh,create_date,state,md5) values(:1,:2,:3,:4)' 
        cursor.execute(sql,params)  
    
    def start(self):    
        for x in range(200):    
            ThreadList = []   
            for i in range(self.thread_count): 
                pageindex = x*self.thread_count + i
                threadname = str(i+1)+'(第%d次)'%(x+1)
                ThreadList.append(Thread(target=self.get_data,args=(pageindex,threadname,)))
            
            #启动子线程
            for thread in ThreadList:
                thread.start() 
                
            #等待线程结束
            for thread in ThreadList:
                thread.join()   
            time.sleep(2)
            
if __name__ == "__main__":
    print("主线程(%s)启动"%(currentThread().name))
    start = time.time() 
    bs = BlobSpider()
    bs.start()
    end = time.time()
    print("主线程(%s)结束,总耗时：%0.6f秒"%(currentThread().name,end-start)) 