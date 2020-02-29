#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: guojun
# @Company: 航天神舟智慧系统技术有限公司
# @Site: https://user.qzone.qq.com/350606539/main
# @Date: 2020-02-29 09:26:57
# @Last Modified by: guojun
# @Last Modified time: 2020-02-29 09:26:57
# @Software: vscode
from odps import ODPS
import cx_Oracle
import os
import openpyxl
from openpyxl.cell.cell import ILLEGAL_CHARACTERS_RE
import re
import time

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'                                        #设置plsql客户端字符集

class Matedata_odps:
    def __init__(self):
        self.conn = "cigproxy/cigproxy@172.21.246.244:15211/xe"                                 # 存储的odps的表名的位置
        self.access_id = 'HWqOnIUpeYhyd7BR'                                                     # 登陆账号
        self.access_key = '0RG5GJpo2WjCCwpUkQzcwjGGzKX8Tn'                                      # 登陆密码
        self.project = 'hzdn_mplc_dev'                                                          # odps上的项目名称
        self.endpoint = 'http://service.cn-huzhou-hzdsj-d01.odps.ops.cloud.huzhou.gov.cn/api'   # 官方提供的接口
        self.rowcount = 2

        # 链接odps
        self.op = ODPS(access_id=self.access_id,
                       secret_access_key=self.access_key,
                       project=self.project,
                       endpoint=self.endpoint)

    # 获取odps上对应分区表的元数据信息
    def get_matedata(self, tables):
        for row in tables:
            table_name = row[0]                          #表名  
            t = self.op.get_table(table_name)            
            table_comment = t.comment                    #表注释
            #schema = t.schema                           #表架构信息  
            schema = re.findall('(\w+)\s+(\w+)\s+#\s+(\S+)',str(t.schema)) #此处将表架构信息转换成元组保存
            col_comment = [t[-1] for t in schema]        #列注释信息
            if '分区字段' in col_comment[-1]:             #分区字段在最后，不需要，删除之
                col_comment.pop()
                
            l = []                                       #获取表的所有分区信息   
            try:  
                for par in t.partitions:                 #如果分区不存在会报错
                    l.append(par.name)
            except Exception as e: 
                pass 
            l = None if l == [] else l[-1]
            print(table_name,table_comment)
            try:
                data = [value for value in self.op.read_table(  
                        table_name, start = 0, limit = self.rowcount, partition = l)] 
                self.write_excel(data,col_comment,table_comment[0:30],table_name[0:30])    
                print(data)
                print('导出:{}表({})分区[{}]成功！'.format(table_comment,table_name,l))
            except Exception as e:      
                print('查询:{}表({})分区[{}]错误！'.format(table_comment,table_name,l))
    
    # 将数据写入excel
    def write_excel(self,data,colname,workbook_name,sheet_name): 
        data = self.illegal_char_rm(data)                   # 写入前进行非法字符处理
        workbook = openpyxl.Workbook()                      # 创建工作簿workbook
        sheet = workbook.active                             # 创建工作表sheet，默认使用active页
        sheet.title = sheet_name                            # 给工作表赋名
        #list(data[0]._name_indexes.keys())                 # 取sql查询结果的字段名 
        sheet.append(colname)    
        for record in data:
            sheet.append(record.values)                     # 取每条记录
        workbook.save(r'backup\样例数据\\'+workbook_name+'.xlsx')                # 保存工作薄并命名
        
    # 定义处理非法字符的方法
    def illegal_char_rm(self,l):
        la = list()
        for record in l:  # 遍历每条表记录
            # 遍历记录的每一列的值，record.values类型为list，取list的index和value需要用enumerate，不然会报错
            for index, value in enumerate(record.values):
                record[index] = ILLEGAL_CHARACTERS_RE.sub('', value) if isinstance(
                    value, str) else value  # 如果值类型为字符串，替换为空，否则保留原值
            la.append(record)
        return la 

    # 获取所有存储的odps的表名，并将样例数据写入excel
    def start(self):
        sql = 'SELECT "推送后的表名" table_name FROM test."BASE_表结构0228" WHERE ("推送后的表名") LIKE \'%dws_evt_subsistence_allowances%\''
        conn = cx_Oracle.connect(self.conn)
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()  
        self.get_matedata(rows)
        cursor.close()
        conn.close()
    
if __name__ == '__main__':  
    start = time.time()
    mate = Matedata_odps()
    mate.start()
    end = time.time()
    print("导出样例数据完成！！！""总耗时：%0.6fs"%(end -start)); 