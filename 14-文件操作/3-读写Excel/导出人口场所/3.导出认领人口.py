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
'南浔古镇旅游度假区']

def get_person():
    os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
    conn = cx_Oracle.connect('cigproxy','Htzhcig_5873','172.21.244.81:15227/orcl')
    cursor = conn.cursor() 
 
    for town in town_list:
        sql =  (""" SELECT 身份证号码,姓名,性别,出生日期,户籍地址,现住地址,联系方式,NVL(乡镇,'德清县') 乡镇,NVL(所属网格,'德清县') 所属网格,nvl(网格层级,1) 网格层级,NVL(认领网格,'德清县') 认领网格 FROM (
                        SELECT CARD_NUM 身份证号码,NAME 姓名,DECODE(GENDER,'1','男','2','女') 性别,TO_CHAR(BIRTH_DATE,'YYYY-MM-DD') 出生日期,
                            R_ADDR 现住地址,D_ADDR 户籍地址,PHONE 联系方式,DECODE(PERSON_TYPE,'1','户籍人口','2','流动人口') 人口类型,
                            CASE INSTR(tb.DISPLAYNAME,'/') when 0 THEN tb.DISPLAYNAME ELSE SUBSTR(tb.DISPLAYNAME,1,INSTR(tb.DISPLAYNAME,'/')-1) END 乡镇,
                            tc.DISPLAYNAME 认领网格,
                            TB.DISPLAYNAME 所属网格,TB.D_LEVEL 网格层级 FROM ZZ_PERSON TA
                        LEFT JOIN A4_SYS_DEPARTMENT TB ON TA.G_ID=TB.DEPARTMENTID AND TB.STATE=1
                        LEFT JOIN A4_SYS_DEPARTMENT TC ON TA.CLAIM_G_ID=TC.DEPARTMENTID AND TB.STATE=1
                        WHERE DEL_FLAG=0
                    ) where 网格层级<>4 and 乡镇='{}'
                    order by 乡镇,网格层级,所属网格,身份证号码""".format(town)) 
            
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
    sheet.write('I1', '所属网格', bold)
    sheet.write('J1', '网格层级', bold)
    sheet.write('K1', '认领网格', bold)

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
    
