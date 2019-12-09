#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-10-22 20:29:53 
# @Last Modified by: guojun 
# @Last Modified time: 2019-10-22 20:29:53 
# @Software: vscode  

import cx_Oracle
import os
import urllib.request
import xlsxwriter
import os,time,random 

api_token = "fklasjfljasdlkfjlasjflasjfljhasdljflsdjflkjsadljfljsda"

#获取查询的数据集
def get_data(conn,tablename,comment,sql):
    cursor = conn.cursor() 
    cursor.execute(sql);
    rows = cursor.fetchall()  # 得到所有数据集
    li =[];
    for row in rows:
        li.append(row)

    print("Number of %s(%s) returned: %d" %(tablename,comment,cursor.rowcount-1))

    cursor.close() 
    return  li; 

#将数据按照行列保存到Excel中
def save_excel(li,dirname,sheetname):
    book = xlsxwriter.Workbook(r'backup\样例数据'+'\\'+dirname+'.xlsx')
    sheet = book.add_worksheet(sheetname)

    # Write some data headers. 带自定义粗体blod格式写表头
    bold = book.add_format({'bold': True})
    tu = li[0]
    
    rowindex = 0
    colindex = 0
    for row in li:            #行
        for col in row:         #列 
            sheet.write(rowindex, colindex, col) 
            colindex+=1
        rowindex+=1
        colindex=0

    book.close();

#获取查询的SQL语句
def get_sql():
    os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
    conn = cx_Oracle.connect('test','esri@123','172.21.246.244:15211/xe')
    cursor = conn.cursor() 
    
    #获取查询的SQL语句("""或者'''控制多行输出)
    sql =  ("""SELECT TA.TABLE_NAME,trim(replace(replace(replace(replace(replace(TA.COMMENTS,chr(10)),CHR(32)),chr(13)),chr(9)),' ')) COMMENTS ,replace(TA.COLLIST,', FROM DUAL',' FROM DUAL')||' UNION ALL '||SQLTEXT SQLTEXT FROM (
                SELECT ta.TABLE_NAME,TC.COMMENTS,'SELECT '||xmlagg(xmlparse(content ''''||to_char(NVL(TA.COMMENTS,TA.COLUMN_NAME))||''' AS '||TA.COLUMN_NAME||',' wellformed) order by tb.column_id).getclobval()||' FROM DUAL' AS COLLIST 
                    FROM USER_COL_COMMENTS TA
                        JOIN USER_TAB_COLUMNS TB ON TA.TABLE_NAME=TB.TABLE_NAME AND TA.COLUMN_NAME=TB.COLUMN_NAME  
                        JOIN  USER_TAB_COMMENTS TC ON TC.TABLE_NAME=TB.TABLE_NAME
                    WHERE TA.TABLE_NAME like 'STG%' group  by TA.TABLE_NAME,TC.COMMENTS   
                ) TA ,(
                select DISTINCT TA.TABLE_NAME,TC.COMMENTS,'SELECT '||LISTAGG(TO_CHAR(COLUMN_NAME),',') WITHIN GROUP(ORDER BY COLUMN_ID) OVER(PARTITION BY TA.TABLE_NAME) ||' FROM '||TA.TABLE_NAME||' WHERE ROWNUM<=100' AS SQLTEXT 
                    FROM USER_TAB_COLUMNS TA
                    JOIN  USER_TAB_COMMENTS TC ON TC.TABLE_NAME=TA.TABLE_NAME
                    WHERE TA.TABLE_NAME like 'STG%'
                ) TB WHERE TA.TABLE_NAME=TB.TABLE_NAME
            """);  

    cursor.execute(sql);
    #rows = cursor.fetchall()  # 得到所有数据集 
    for row in cursor:
        #li.append({"TABLE_NAME":row[0],"COMMENTS":row[1],"SQL":row[2].read()});
        li = get_data(conn,row[0],row[1],row[2].read()) 
        save_excel(li,row[1],row[0])

    print("Number of SQL_rows returned: %d\n\n" % cursor.rowcount)

    cursor.close()
    conn.close() 
  
def run(): 
    start = time.time()
    get_sql();
    end = time.time() 
    print("查询数据完成！！！""总耗时：%0.6fs"%(end -start)); 

if __name__ == "__main__":   
    run(); 
