#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-03-07 16:28:44 
# @Last Modified by: guojun 
# @Last Modified time: 2020-03-07 16:28:44 
# @Software: vscode 
# 参考链接：https://blog.csdn.net/magic_engine/article/details/79275341 
#采用多线程进行文件拷贝

import cx_Oracle
import os
import urllib.request 
import time
import openpyxl  
from threading import Thread     

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8' 

#获取户籍人员
def get_person(page_index):
    start = time.time() 
    conn = cx_Oracle.connect('test','esri@123','10.21.198.127:15223/XE')
    cursor = conn.cursor()   
    
    total_count = 100000                       #总行数
    page_size = 1000                           #每页行记录数,1000
    total_page = int(total_count/page_size)    #总页数 

    workbook = openpyxl.Workbook(write_only=True)
    sheet = workbook.create_sheet()
    
    for i in range(100):  
        rn_start,rn_end = page_size*(i)+100000*page_index,page_size*(i+1)+100000*page_index
        sql = """select * FROM (SELECT row_number() over(order by card_num) as rn,CARD_NUM 身份证号码,NAME 姓名,D_ADDR 户籍地址,
                    R_ADDR 现住地址,DISPLAYNAME 网格全称,DEPARTMENTNAME 网格,DECODE(GENDER,'1','男','2','女') 性别,BIRTH_DATE 出生日期 
                FROM CIGPROXY.ZZ_PERSON ta
                join CIGPROXY.a4_sys_department tb on ta.g_id=tb.departmentid) WHERE RN>{} AND RN<={}""".format(rn_start,rn_end)
    
        cursor.execute(sql) 
        person_list = cursor.fetchall()         
        
        print('线程{}查询第{}-{}条数据'.format(page_index+1,rn_start,rn_end))      
        for x in person_list:
            sheet.append(x) 
        
    workbook.save(r'backup\excel\人口\户籍_{}_{}.xlsx'.format(100000*page_index,100000*(page_index+1)))
    workbook.close()
    workbook = None 
                    
    end = time.time() 
    print("线程-%d：已导出第%d-%d页人员数量: %d人,当前页耗时：%0.2fs"%(page_index+1,100000*page_index,100000*(page_index+1),100000,end-start))

    cursor.close()
    conn.close()
 
if __name__ == "__main__":   
    start = time.time()
    
    ThreadList = []
    
    for x in range(8): 
        ThreadList.append(Thread(name=x, target=get_person, args=(x,)))

    for tr in ThreadList:
        tr.start()

    for tr in ThreadList:
        tr.join()
 
    end = time.time()   
    print('')
    print("导出全部户籍人口数据完成！！！""总耗时：%0.2fs"%(end -start)); 
    
