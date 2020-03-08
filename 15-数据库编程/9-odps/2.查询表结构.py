#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-03-01 17:05:20 
# @Last Modified by: guojun 
# @Last Modified time: 2020-03-01 17:05:20 
# @Software: vscode 

from odps import ODPS
import cx_Oracle
import os
import xlsxwriter
import re
import time

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'  # 设置plsql客户端字符集

class Matedata_odps:
    def __init__(self):
        # 存储的odps的表名的位置
        self.conn = "cigproxy/cigproxy@172.21.246.244:15211/xe"
        # 登陆账号
        self.access_id = 'HWqOnIUpeYhyd7BR'
        # 登陆密码
        self.access_key = '0RG5GJpo2WjCCwpUkQzcwjGGzKX8Tn'
        # odps上的项目名称
        self.project = 'hzdn_mplc_dev'
        self.endpoint = 'http://service.cn-huzhou-hzdsj-d01.odps.ops.cloud.huzhou.gov.cn/api'   # 官方提供的接口
        self.rowcount = 100

        # 链接odps
        self.op = ODPS(access_id=self.access_id,
                       secret_access_key=self.access_key,
                       project=self.project,
                       endpoint=self.endpoint)

    # 获取odps上对应分区表的元数据信息
    def get_matedata(self, tables): 
        data = []
        for row in tables:
            table_name = row[0]                                 # 表名
            t = self.op.get_table(table_name)
            table_comment = t.comment                           # 表注释
            # schema = t.schema                                 #表架构信息
            schema = re.findall('(\w+)\s+(\w+)\s+#\s+(\S+)',
                                str(t.schema))                  # 此处将表架构信息转换成元组保存
            col = [(t[0],t[-1]) for t in schema]                # 列注释信息
            if '分区字段' in col[-1][-1]:                        # 分区字段在最后，不需要，删除之
                col.pop()
             
            l = ''  # 获取表的所有分区信息
            try:
                for par in t.partitions:  # 如果分区不存在会报错
                    l += (par.name+'\n')
            except Exception as e:
                pass 
            
            ddl_sql = self.get_oracle_ddl(table_name[0:30],table_comment,schema)
            data.append((table_name,table_comment,l,ddl_sql,col))
            print('查询:{}表({})结构[{}]成功！'.format(table_comment, table_name, l.replace('\n',' '))) 
        return data
    
    def get_oracle_ddl(self,table_name,table_comment,schema):  
        c_list = 'create table %s\n(\n'%table_name
        c_comm = ''
        for col in schema: 
            c_name = col[0][0:30]         #oracle列名
            if col[0]!='dt':
                c_list += '\t{} {},\n'.format(col[0],'varchar2(4000)')
                c_comm += 'comment on column {}.{} is \'{}\';\n'.format(table_name,col[0],col[2])
            
        c_list += '''\tcreate_date date default sysdate,\n\tcreate_user varchar2(100) default 'pyodps'\n);\n'''
        c_list += 'comment on table {} is \'{}\';\n'.format(table_name,table_comment)   
        return c_list+c_comm

    def write_excel(self,data):    
        dir = r'backup\ODPS表结构.xlsx'  
        book = xlsxwriter.Workbook(dir)   
        sheet = book.add_worksheet("表信息") 
        sheet2 = book.add_worksheet("列信息") 
        bold = book.add_format({'bold': True}) 
        sheet.set_column("A:A", 35)  
        sheet.set_column("B:B", 20)  
        sheet.set_column("C:C", 15)   
        sheet.set_column("D:D", 30)  
        sheet.set_column("E:E", 100)   
        sheet.write('A1', 'ODPS表名', bold)
        sheet.write('B1', 'ODPS表注释', bold)
        sheet.write('C1', 'ODPS分区名称', bold)
        sheet.write('D1', 'Oracle表名', bold)
        sheet.write('E1', 'Oracle建表语句', bold) 
        
        sheet2.set_column("A:A", 35)  
        sheet2.set_column("B:B", 20)  
        sheet2.set_column("C:C", 15)   
        sheet2.set_column("D:D", 30)   
        sheet2.write('A1', 'ODPS表名', bold)
        sheet2.write('B1', 'ODPS列名', bold)
        sheet2.write('C1', 'ORACLE表名', bold)
        sheet2.write('D1', 'ORACLE列名', bold) 
           
        rowindex = 0   
        subindex = 0
        for item in data:
            table_name,table_comment,par,ddl_sql,col = item
            rowindex += 1
            sheet.write(rowindex, 0, table_name) 
            sheet.write(rowindex, 1, table_comment) 
            sheet.write(rowindex, 2, par) 
            sheet.write(rowindex, 3, table_name[0:30]) 
            sheet.write(rowindex, 4, ddl_sql) 
            
            for c in col:
                subindex += 1 
                sheet2.write(subindex, 0, table_name) 
                sheet2.write(subindex, 1, c[0]) 
                sheet2.write(subindex, 2, table_name[0:30]) 
                sheet2.write(subindex, 3, c[0][0:30]) 

        book.close()

    # 获取所有存储的odps的表名，并将样例数据写入excel
    def start(self):
        sql = 'SELECT distinct "推送后的表名" table_name FROM test."BASE_表结构0228" WHERE "推送后的表名" is not null'
        conn = cx_Oracle.connect(self.conn)
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()  
        self.write_excel(self.get_matedata(rows))
        cursor.close()
        conn.close() 

if __name__ == '__main__':
    start = time.time()
    mate = Matedata_odps()
    mate.start()
    end = time.time()
    print("获取odps数据表结构完成！！！""总耗时：%0.6fs" % (end - start))
