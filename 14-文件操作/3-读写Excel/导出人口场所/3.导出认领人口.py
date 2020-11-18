#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-02-26 19:08:19 
# @Last Modified by: guojun 
# @Last Modified time: 2020-02-26 19:08:19 
# @Software: vscode  

import cx_Oracle
import os
import urllib.request
import xlsxwriter
import time
 
town_list = ['开发区',
'南浔镇',
'练市镇',
'双林镇',
'菱湖镇',
'和孚镇',
'旧馆镇',
'石淙镇',
'善琏镇',
'千金镇',
'南浔古镇旅游度假区','南浔区']

def get_person():
    os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
    conn = cx_Oracle.connect('cigproxy','Htzhcig_5873','172.21.244.81:15227/orcl')
    cursor = conn.cursor() 
 
    for town in town_list:
        sql =  (""" 
                SELECT 身份证号码,姓名,性别,出生日期,户籍地址,现住地址,联系方式,乡镇,认领级别,认领网格,人口类型 FROM (
                    SELECT 身份证号码,姓名,性别,出生日期,户籍地址,现住地址,联系方式,乡镇,认领级别,NVL(认领网格,所属网格) 认领网格,人口类型 
                    FROM (
                        SELECT CARD_NUM 身份证号码,NAME 姓名,DECODE(GENDER,'1','男','2','女') 性别,TO_CHAR(BIRTH_DATE,'YYYY-MM-DD') 出生日期,
                            R_ADDR 现住地址,D_ADDR 户籍地址,PHONE 联系方式,DECODE(PERSON_TYPE,'1','户籍人口','2','流动人口') 人口类型,
                            NVL(tc.l2_departmentname,'南浔区') 乡镇,
                            tc.departmentfullname 认领网格,NVL(TB.departmentfullname,'南浔区') 所属网格,CLAIM_level 认领级别 
                        FROM ZZ_PERSON TA
                        LEFT JOIN SYS_FULL_DEPT TB ON TA.G_ID=TB.DEPARTMENTID  
                        LEFT JOIN SYS_FULL_DEPT TC ON TA.CLAIM_G_ID=TC.DEPARTMENTID 
                        WHERE IS_CLAIM=0 and CLAIM_level IS NOT NULL and BITAND(3377699720527872, CLAIM_G_ID) =1125899906842624
                    ) 
                ) WHERE 乡镇='{}'
                order by 乡镇,认领级别,认领网格,身份证号码""".format(town)) 
            
        cursor.execute(sql);
        rows = cursor.fetchall()  # 得到所有数据集
        save_excel(rows,town)
                
        print("已导出{}-认领人口数量: {}".format(town,cursor.rowcount))

    cursor.close()
    conn.close()

def save_excel(rows,town):    
    dir = r'backup\南浔认领人口'
    # 然后创建一个目录:
    if not os.path.exists(dir): 
        os.mkdir(dir) 
        
    # subdir = dir+'\\'+town
    # if not os.path.exists(subdir): 
    #     os.mkdir(subdir) 
        
    book = xlsxwriter.Workbook(dir+'\\'+town + '认领人口.xlsx')  #新建excel表
    sheet = book.add_worksheet('人口')

    # Write some data headers. 带自定义粗体blod格式写表头
    bold = book.add_format({'bold': True})

    sheet.set_column("A:A", 18)  
    sheet.set_column("B:D", 12)   
    sheet.set_column("E:F", 30)    
    sheet.set_column("G:H", 15)     
    sheet.set_column("I:I", 20)      
    sheet.set_column("J:J", 12)      
    sheet.set_column("K:K", 20)   
    sheet.write('A1', '身份证号码', bold)
    sheet.write('B1', '姓名', bold)
    sheet.write('C1', '性别', bold)
    sheet.write('D1', '出生日期', bold)
    sheet.write('E1', '户籍地址', bold)
    sheet.write('F1', '现住地址', bold)
    sheet.write('G1', '联系方式', bold)
    sheet.write('H1', '乡镇', bold) 
    sheet.write('I1', '认领级别', bold)
    sheet.write('J1', '认领网格', bold)
    sheet.write('K1', '人口类型', bold)

    rowindex = 0 
    for row in rows:
        rowindex = rowindex+1  
        for i in range(11):
            sheet.write(rowindex, i, row[i]) 

    book.close(); 

if __name__ == "__main__":   
    start = time.time()
    get_person()
    end = time.time() 
    print("")
    print("导出认领人口数据完成！！！""总耗时：%0.6fs"%(end -start)); 
    
