#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-06-30 11:05:49 
# @Remark: 人生苦短，我用python！
# cx_oracle导入数据编码错误解决办法:https://blog.csdn.net/liaolijin/article/details/38039065

import cx_Oracle
import os
import urllib.request
import xlsxwriter
import time
 
town_list = ['南浔区','开发区','双林镇','和孚镇','菱湖镇']

def get_person():
    os.environ['NLS_LANG'] = 'AMERICAN_AMERICA.AL32UTF8'
    # os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
    # 如果报错：UnicodeDecodeError: 'utf-8' codec can't decode byte 0xed in position 27: invalid continuation byte，
    # 去掉上边一行先试试,或者改为SIMPLIFIED CHINESE_CHINA.ZHS16GBK！！！
    conn = cx_Oracle.connect('cigproxy','cigproxy','172.21.244.81:15227/orcl')
    cursor = conn.cursor() 
 
    for town in town_list:
        sql =  (""" SELECT 身份证号码,姓名,性别,出生日期,户籍地址,现住地址,联系方式,NVL(乡镇,'南浔区') 乡镇,NVL(村社区,'南浔区') 村社区,NVL(四级网格,'南浔区') 四级网格,NVL(网格全称,'南浔区') 网格全称,nvl(网格层级,1) 网格层级,人口类型 FROM (
                        SELECT CARD_NUM 身份证号码,NAME 姓名,DECODE(GENDER,'1','男','2','女') 性别,TO_CHAR(BIRTH_DATE,'YYYY-MM-DD') 出生日期,
                            R_ADDR 现住地址,D_ADDR 户籍地址,PHONE 联系方式,DECODE(PERSON_TYPE,'1','户籍人口','2','流动人口') 人口类型,
                            CASE INSTR(tb.DISPLAYNAME,'/') when 0 THEN tb.DISPLAYNAME ELSE SUBSTR(tb.DISPLAYNAME,1,INSTR(tb.DISPLAYNAME,'/')-1) END 乡镇,
                            CASE INSTR(tb.DISPLAYNAME,'/') when 0 THEN tb.DISPLAYNAME ELSE SUBSTR(tb.DISPLAYNAME,INSTR(tb.DISPLAYNAME,'/')+1,INSTR(tb.DISPLAYNAME,'/',-1)-INSTR(tb.DISPLAYNAME,'/')-1) END 村社区,
                            TB.DEPARTMENTNAME 四级网格,TB.DISPLAYNAME 网格全称,TB.D_LEVEL 网格层级 FROM ZZ_PERSON TA
                        LEFT JOIN A4_SYS_DEPARTMENT TB ON TA.G_ID=TB.DEPARTMENTID AND TB.STATE=1
                        WHERE DEL_FLAG=0
                    ) where NVL(乡镇,'南浔区')='{}'
                    order by 乡镇,村社区,网格层级,网格全称,身份证号码""".format(town)) 
            
        cursor.execute(sql)
        rows = cursor.fetchall()  
        
        save_excel(rows,town)
                
        print("已导出{}-人口数量: {}".format(town,cursor.rowcount))

    cursor.close()
    conn.close()

def save_excel(rows,town):    
    dir = r'backup\南浔实有人口'
    # 然后创建一个目录:
    if not os.path.exists(dir): 
        os.mkdir(dir) 
        
    # subdir = dir+'\\'+town
    # if not os.path.exists(subdir): 
    #     os.mkdir(subdir) 
        
    book = xlsxwriter.Workbook(dir + '\\' + town + '.xlsx')  #新建excel表
    sheet = book.add_worksheet('人口')

    # Write some data headers. 带自定义粗体blod格式写表头
    bold = book.add_format({'bold': True})
    bold.set_align("left")          #设置对齐方式
    
    sheet.set_column("A:A", 18)  
    sheet.set_column("B:C", 10)   
    sheet.set_column("D:D", 12)   
    sheet.set_column("E:F", 30)    
    sheet.set_column("G:J", 15)     
    sheet.set_column("K:K", 30)     
    sheet.set_column("L:M", 12)    
    sheet.write('A1', '身份证号码', bold)
    sheet.write('B1', '姓名', bold)
    sheet.write('C1', '性别', bold)
    sheet.write('D1', '出生日期', bold)
    sheet.write('E1', '户籍地址', bold)
    sheet.write('F1', '现住地址', bold)
    sheet.write('G1', '联系方式', bold)
    sheet.write('H1', '乡镇', bold) 
    sheet.write('I1', '村社区', bold) 
    sheet.write('J1', '四级网格', bold) 
    sheet.write('K1', '网格全称', bold)
    sheet.write('L1', '网格层级', bold)
    sheet.write('M1', '人口类型', bold)

    rowindex = 0 
    for row in rows:
        rowindex = rowindex+1  
        for i in range(13):
            sheet.write(rowindex, i, row[i]) 

    book.close(); 

if __name__ == "__main__":   
    start = time.time()
    get_person()
    end = time.time() 
    print("")
    print("导出人口数据完成！！！""总耗时：%0.6fs"%(end -start)); 
    
