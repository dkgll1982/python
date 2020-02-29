#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-03-03 11:21:23 
# @Last Modified by: guojun 
# @Last Modified time: 2020-03-03 11:21:23 
# @Software: vscode 

import xlrd 
import cx_Oracle
import sys
import hashlib
import os.path
 
class ExcelToDb():
    def __init__(self,file_name):
        self.dbuser = 'cigproxy'
        self.dbpwd = 'cigproxy'
        self.dbserver = '172.21.246.244:15211/xe'
        self.datatype = 'jkm_person'
        self.file_name = file_name
        self.filemd5 = self.getfilemd5()
        
    #获取文件md5值
    def getfilemd5(self): 
        md5 = ''
        if os.path.isfile(self.file_name):
            with open(self.file_name,'rb') as f:
                contents = f.read()
                f.close()
                md5 = hashlib.md5(contents).hexdigest()
        return md5 
    
    #读取excel，保存到db
    def savedb(self):  
        # 1. 打开文件
        work_book = xlrd.open_workbook(self.file_name) 

        # 2 通过sheet页索引创建sheet页对象
        work_sheet = work_book.sheet_by_index(0)

        # 3.获取excel文件sheet页 行列数
        num_rows = work_sheet.nrows
        num_cols = work_sheet.ncols
        print("Excel文件的行数为:{}行".format(work_sheet.row_values(0))) 

        db_conn=cx_Oracle.connect(self.dbuser, self.dbpwd, self.dbserver,encoding="UTF-8")
        db_cursor = db_conn.cursor()

        col = ''
        for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXY'[0:num_cols]: 
            col = col +',:' + letter 
        col = ':TYPE,:Z' + col    
        
        sql_del = "delete from excel_table where type='{}' and z='{}'".format(self.datatype,self.filemd5)
        sql_cmd = 'insert into excel_table({}) values ({})'.format(col.replace(':',''),col)
        db_cursor.execute(sql_del) 

        for curr_row in range(num_rows):
            row = work_sheet.row_values(curr_row)
            row.insert(0,self.datatype)
            row.insert(1,self.filemd5) 
            db_cursor.execute(sql_cmd, row) 

        db_conn.commit() 
        db_cursor.close()
        db_conn.close()
        
if __name__ == '__main__': 
    args = sys.argv 
    if len(args) > 1: 
        file_name = args[1]
        if os.path.isfile(file_name):
            t = ExcelToDb(file_name)
            t.savedb()
        else:
            print('Waring!!!,excel file path is not exist.') 
    else:
        print('Erorr!!!,please enter excel file path.') 
     