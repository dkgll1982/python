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

def get_person():
    os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
    conn = cx_Oracle.connect('cigproxy','cigproxy','172.21.188.219:15223/orcl')
    cursor = conn.cursor() 
 
    for town in town_list:
        sql =  (""" SELECT * FROM (
                        SELECT PLACE_NAME 场所登记名称,OLD_PLACE_NAME 场所名称,PLACE_ADDR 场所地址,tb.TYPE_MAX_NAME 场所大类,
                        tb.TYPE_NAME 场所小类,
                            decode(TA.IS_KEY_PLACE,'1','重点场所','一般场所') 是否重点,
                            listagg(to_char(TD.VALUE),',') within group(order by td.key) over(partition by ta.id) AS 平安检查类型,DISPLAYNAME 所属网格,
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
                        FROM ZZ_PLACE_COMMON ta
                            left join view_place_type  tb on ta.place_type=tb.PLACE_TYPE and ta.PLACE_TYPE_MAX=tb.PLACE_TYPE_MAX
                            LEFT JOIN ZZ_PLACE_TYPE_MAP TC ON TA.ID=TC.PLACE_ID
                            LEFT JOIN DOMAINS TD ON TC.SAFE_CHECK_TYPE=TD.key AND TD.DOMAINNAME='safeCheckType'
                            LEFT JOIN A4_SYS_DEPARTMENT TE ON TA.DEPARTMENT_ID=TE.DEPARTMENTID
                        WHERE TA.IS_CLAIM=0 order by DEPARTMENT_ID
                    )                     
                    WHERE 乡镇="""+"'{}'".format(town)) 
            
        cursor.execute(sql);
        rows = cursor.fetchall()  # 得到所有数据集
        save_excel(rows,town)
                
        print("已导出{}-场所数量: {}".format(town,cursor.rowcount))

    cursor.close()
    conn.close()

def save_excel(rows,town):    
    dir = r'backup\德清认领场所'
    # 然后创建一个目录:
    if not os.path.exists(dir): 
        os.mkdir(dir) 
        
    subdir = dir+'\\'+town
    if not os.path.exists(subdir): 
        os.mkdir(subdir) 
        
    book = xlsxwriter.Workbook(subdir+'\\'+'场所.xlsx')  #新建excel表
    sheet = book.add_worksheet('场所')

    # Write some data headers. 带自定义粗体blod格式写表头
    bold = book.add_format({'bold': True})

    sheet.set_column("A:B", 25)  
    sheet.set_column("C:C", 35)  
    sheet.set_column("D:F", 12)   
    sheet.set_column("G:G", 15)   
    sheet.set_column("H:H", 28)   
    sheet.set_column("I:K", 12)    
    sheet.write('A1', '场所登记名称', bold)
    sheet.write('B1', '场所名称', bold)
    sheet.write('C1', '场所地址', bold)
    sheet.write('D1', '场所大类', bold)
    sheet.write('E1', '场所小类', bold)
    sheet.write('F1', '是否重点', bold)
    sheet.write('G1', '平安检查类型', bold)
    sheet.write('H1', '所属网格', bold) 
    sheet.write('I1', '乡镇', bold)
    sheet.write('J1', '村社区', bold)
    sheet.write('K1', '四级网格', bold)

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
    print("导出场所数据完成！！！""总耗时：%0.6fs"%(end -start)); 
    
