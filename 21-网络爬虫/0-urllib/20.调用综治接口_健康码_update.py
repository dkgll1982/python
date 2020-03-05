#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-02-21 19:20:37 
# @Last Modified by: guojun 
# @Last Modified time: 2020-02-21 19:20:37 
# @Software: vscode 
# @Describe：健康码查询

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
        self.dbuser = 'cigproxy'
        self.dbpwd = 'cigproxy'
        self.dbserver = '172.21.246.244:15211/xe'
        self.datatype = 'jkm_person'
        self.city = '湖州市'  
    
    #导出结果到Excel
    def imp_excel(self): 
        conn = cx_Oracle.connect(self.dbuser, self.dbpwd, self.dbserver,encoding="UTF-8") 
        cursor = conn.cursor()  
        
        xz_list = ['吕山乡','和平镇','太湖街道','夹浦镇','小浦镇','李家巷镇','林城镇','水口乡','泗安镇','洪桥镇','煤山镇','画溪街道','虹星桥镇','长兴县公安局城东派出所','长兴县公安局水口派出所','雉城街道','龙山街道']
        for xz in xz_list:
            #查询结果
            sql = """select DISTINCT TA.XH 序号,TA.A 县区 ,TA.B 乡镇街道,TA.C 村社区,TA.D 小区路,TA.E 出生日期,TA.F 公民身份证号,TA.G 姓名,
                TO_SINGLE_BYTE(JSON_VALUE(TB.B,'$.data.mzt' )) 健康码状态,
                TO_SINGLE_BYTE(JSON_VALUE(TB.B,'$.data.hmcmyy' )) 红黄码原因,
                TO_SINGLE_BYTE(JSON_VALUE(TB.B,'$.data.scsqsj' )) 首次申请时间,
                TO_SINGLE_BYTE(JSON_VALUE(TB.B,'$.data.scffsj' )) 首次发放时间,
                TO_SINGLE_BYTE(JSON_VALUE(TB.B,'$.data.scffsj' )) 最近更新时间
            from excel_table ta 
            join ( 
                select a,b from (
                    select a,b,c,row_number() over (partition by a order by to_date(c,'YYYY-MM-DD HH24') desc) rn from excel_table where type='jkm'
                ) where rn=1
            ) tb on ta.F=tb.a and ta.TYPE='jkm_person' and ta.z='5791d23f5d7deb635438fdd035c5d776' 
            where ta.b='{}'  
            order by ta.xh""".format(xz)
            
            cursor.execute(sql)  
            rows = cursor.fetchall()  # 得到所有数据集 
            
            book = xlsxwriter.Workbook(xz+'.xlsx') 
            sheet = book.add_worksheet('户籍人口')

            # Write some data headers. 带自定义粗体blod格式写表头
            bold = book.add_format({'bold': True})
        
            #获取表的列名
            title = [i[0] for i in cursor.description]   
            sheet.write_row('A1',title)  
                
            rn = 1     
            for row in rows: 
                rn += 1
                sheet.write_row('A%d'%rn,row) 
                
            book.close()
            print('导出%s完成！'%(xz))
            
        cursor.close()
        conn.close()  
        
if __name__ == '__main__':  
    print("主线程(%s)启动"%(threading.current_thread().name))
    start = time.time()  
    jkm = JKMSpider()   
    jkm.imp_excel() 
    end = time.time()
    print("主线程(%s)结束,总耗时：%0.6f秒"%(threading.current_thread().name,end-start))  