#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-03-29 10:41:44 
# @Remark: 人生苦短，我用python！

import cx_Oracle
import os

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

class db_operate():
    def __init__(self):
        super().__init__()
        
    def inser_rows(self): 
        #ORACLE连接参数
        conn = cx_Oracle.connect('cigproxy','cigproxy','localhost/orcl')
        cursor = conn.cursor()     
        
        #单个列表
        params = ['1','2','3','test']        
        sql = 'INSERT INTO excel_table(a,b,c,type) values(:1,:2,:3,:4)'
        cursor.execute(sql,params)
        
        #单个元组
        params = ('88','99','100','test')   
        sql = 'INSERT INTO excel_table(a,b,c,type) values(:1,:2,:3,:4)'
        cursor.execute(sql,params)
        
        #单个字典(绑定变量)
        params = {"a":'100',"b":"200","c":300,"type":'test'}   
        sql = 'INSERT INTO excel_table(a,b,c,type) values(:a,:b,:c,:type)'
        cursor.execute(sql,params)
        
        #多个列表
        params = [['1','2','3','test'],['11','22','33','test']]        
        sql = 'INSERT INTO excel_table(a,b,c,type) values(:1,:2,:3,:4)'
        cursor.executemany(sql,params)
        
        #多个元组
        params = [('88','99','100','test'),('881','992','1003','test')]
        sql = 'INSERT INTO excel_table(a,b,c,type) values(:1,:2,:3,:4)'
        cursor.executemany(sql,params)
        
        #多个字典(绑定变量)
        params = [{"a":'100',"b":"200","c":300,"type":'test'},{"a":'1100',"b":"2200","c":3300,"type":'test'}]   
        sql = 'INSERT INTO excel_table(a,b,c,type) values(:a,:b,:c,:type)'
        cursor.executemany(sql,params)       
        
        conn.commit()
        cursor.close()
        conn.close()

if __name__ == "__main__":
    dbop = db_operate()
    dbop.inser_rows()