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
 
town_list = ['雷甸镇','舞阳街道','莫干山镇','德清县','阜溪街道','新市镇','新安镇','武康街道','下渚湖街道','乾元镇','洛舍镇','禹越镇','钟管镇']
zd_list = ['特困儿童','留守人员','临时救助','低保人员','刑满释放人员','社区矫正人员','精神病人','吸毒人员','信访人员','重点青少年']

#town_list = ['新市镇']
#zd_list = ['精神病人']

#获取重点人员
def get_person():
    os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
    conn = cx_Oracle.connect('cigproxy','cigproxy','172.21.188.219:15223/orcl')
    cursor = conn.cursor() 
 
    for town in town_list:
        for zd in zd_list:
            sql =  ("""
                    SELECT * FROM (
                        SELECT name AS 姓名 ,CARD_NUM 身份证,decode(GENDER,'1','男','2','女') 性别,TRUNC((to_char(sysdate, 'yyyyMMdd') - to_char(BIRTH_DATE, 'yyyyMMdd')) /10000) as 年龄,
                            d_addr 户籍地址,R_ADDR 现住地址,DECODE(PERSON_TYPE,'1','户籍人口','2','流动人口') 人口类型,   replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(    
                                replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(person_tab,'301','残疾人'),
                                '302',	'特困儿童'),
                                '303',	'留守人员'),
                                '304',	'老年人'),
                                '305',	'临时救助'),
                                '306',	'低保人员'),
                                '307','寄递业从业人员'),
                                '308', '失业人员'),
                                '309', '育龄妇女'),
                                '201',	'刑满释放人员'),
                                '202',	'社区矫正人员'),
                                '203',	'精神病人'),
                                '204',	'吸毒人员'),
                                '205',	'艾滋病危险人员'),
                                '206',	'信访人员'),
                                '207',	'重点青少年'),
                                '208',	'邪教人员'),
                                '209', '传销人员'),
                                '210', '其他人员'),
                                '211', '危险品从业人员') 重点类型,DISPLAYNAME 所属网格,
                            CASE D_LEVEL 
                                WHEN 1 THEN '德清县' 
                                when 2 then TO_CHAR(DISPLAYNAME)
                                else TO_CHAR(SUBSTR(DISPLAYNAME,0,instr(DISPLAYNAME,'/')-1)) 
                            END 乡镇, 
                            CASE D_LEVEL 
                                WHEN 1 THEN null 
                                when 2 then null
                                when 3 then TO_CHAR(SUBSTR(DISPLAYNAME,instr(DISPLAYNAME,'/')+1)) 
                                when 4 then TO_CHAR(SUBSTR(DISPLAYNAME,instr(DISPLAYNAME,'/')+1,instr(DISPLAYNAME,'/',-1)-instr(DISPLAYNAME,'/')-1)) 
                            END 村社区 , 
                            CASE D_LEVEL 
                                WHEN 4 THEN TO_CHAR(SUBSTR(DISPLAYNAME,instr(DISPLAYNAME,'/',-1)+1))  
                                else null
                            END 四级网格
                        FROM CIGPROXY.ZZ_PERSON_0224 TA
                        JOIN A4_SYS_DEPARTMENT_0220 TB ON TA.G_ID=TB.DEPARTMENTID
                        where G_ID is not null and del_flag=0 and PERSON_TAB is not null
                        order by g_id
                    ) WHERE 乡镇="""+"'{}' and 重点类型 like '%{}%'".format(town,zd)) 
            
            cursor.execute(sql);
            rows = cursor.fetchall()  # 得到所有数据集
            save_excel(rows,town,zd)
                
            print("已导出{}-{}人员数量: {}人".format(town,zd,cursor.rowcount))

    cursor.close()
    conn.close()

def save_excel(rows,town,zd):    
    dir = r'backup\德清重点人口'
    # 然后创建一个目录:
    if not os.path.exists(dir): 
        os.mkdir(dir) 
        
    subdir = dir+'\\'+town
    if not os.path.exists(subdir): 
        os.mkdir(subdir) 
        
    book = xlsxwriter.Workbook(subdir+'\\'+zd+'.xlsx')  #新建excel表
    sheet = book.add_worksheet(zd)

    # Write some data headers. 带自定义粗体blod格式写表头
    bold = book.add_format({'bold': True})

    sheet.set_column("A:A", 10)  
    sheet.set_column("B:B", 20)  
    sheet.set_column("C:D", 6)   
    sheet.set_column("E:F", 22)  
    sheet.set_column("G:G", 10)  
    sheet.set_column("H:I", 28)   
    sheet.set_column("J:L", 12)    
    sheet.write('A1', '姓名', bold)
    sheet.write('B1', '身份证号', bold)
    sheet.write('C1', '性别', bold)
    sheet.write('D1', '年龄', bold)
    sheet.write('E1', '户籍地址', bold)
    sheet.write('F1', '现住地址', bold)
    sheet.write('G1', '人口类型', bold)
    sheet.write('H1', '重点类型', bold)
    sheet.write('I1', '所属网格', bold)
    sheet.write('J1', '乡镇', bold)
    sheet.write('K1', '村社区', bold)
    sheet.write('L1', '四级网格', bold)

    rowindex = 0 
    for row in rows:
        rowindex = rowindex+1  
        for i in range(12):
            sheet.write(rowindex, i, row[i]) 

    book.close(); 

if __name__ == "__main__":   
    start = time.time()
    get_person()
    end = time.time() 
    print("")
    print("导出重点人口数据完成！！！""总耗时：%0.6fs"%(end -start)); 
    
